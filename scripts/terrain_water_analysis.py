#!/usr/bin/env python3
"""Terrain water analysis for a field from a DEM GeoTIFF.

Computes slope (%), D8 flow direction and flow accumulation, topographic wetness index
(TWI), and relative elevation; classifies cells into water zones (shedding, transmitting,
receiving, ponding, conveying); writes rasters and a candidates CSV of concentrated-flow
points suitable for basins or waterways.

Usage:
  python3 scripts/terrain_water_analysis.py <dem.tif> --field F1 [--out data/processed/terrain]
         [--min-accum-acres 5] [--slope-terrace 3]

Requires numpy and rasterio (pip install rasterio). DEM should be projected in meters
(e.g. UTM 14N for Sedgwick County) at 1–3 m resolution. Flat or noisy LiDAR benefits from
a light smoothing pass (--smooth).
"""
import argparse
import csv
import sys
from pathlib import Path

import numpy as np

try:
    import rasterio
    from rasterio.transform import xy
except ImportError:  # pragma: no cover
    print("rasterio is required: pip install rasterio", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SQM_PER_ACRE = 4046.86

# D8 neighbor offsets (row, col) and distance factors
D8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
DIST = np.array([1, np.sqrt(2), 1, np.sqrt(2), 1, np.sqrt(2), 1, np.sqrt(2)])


def fill_pits(z, iterations=50):
    """Simple iterative pit fill: raise single-cell pits to lowest neighbor."""
    z = z.copy()
    for _ in range(iterations):
        pad = np.pad(z, 1, mode="edge")
        nmin = np.full_like(z, np.inf)
        for dr, dc in D8:
            nmin = np.minimum(nmin, pad[1 + dr:1 + dr + z.shape[0], 1 + dc:1 + dc + z.shape[1]])
        pits = z < nmin
        if not pits.any():
            break
        z[pits] = nmin[pits] + 1e-3
    return z


def slope_pct(z, res):
    dzdx = np.gradient(z, res, axis=1)
    dzdy = np.gradient(z, res, axis=0)
    return np.hypot(dzdx, dzdy) * 100.0


def d8_direction(z, res):
    pad = np.pad(z, 1, mode="edge")
    best = np.full(z.shape, -1, dtype=np.int8)
    best_drop = np.zeros(z.shape)
    for i, (dr, dc) in enumerate(D8):
        nb = pad[1 + dr:1 + dr + z.shape[0], 1 + dc:1 + dc + z.shape[1]]
        drop = (z - nb) / (DIST[i] * res)
        better = drop > best_drop
        best[better] = i
        best_drop[better] = drop[better]
    return best


def flow_accumulation(z, direction):
    """Cells sorted high to low; each passes its accumulated count downslope."""
    rows, cols = z.shape
    acc = np.ones(z.shape, dtype=np.float64)
    order = np.argsort(z.ravel())[::-1]
    for idx in order:
        r, c = divmod(int(idx), cols)
        d = direction[r, c]
        if d < 0:
            continue
        dr, dc = D8[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            acc[nr, nc] += acc[r, c]
    return acc


def classify(slope, twi, acc_acres, rel_elev, slope_terrace, min_accum_acres):
    """Zones: 1 shedding, 2 transmitting, 3 receiving, 4 ponding, 5 conveying."""
    zone = np.full(slope.shape, 2, dtype=np.uint8)
    zone[(slope >= slope_terrace) | (rel_elev > 0.6)] = 1
    hi_twi = twi >= np.nanpercentile(twi, 80)
    zone[hi_twi] = 3
    zone[hi_twi & (slope < 0.5) & (rel_elev < 0.15)] = 4
    zone[(acc_acres >= min_accum_acres) & (slope >= 0.5)] = 5
    return zone


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dem")
    ap.add_argument("--field", required=True)
    ap.add_argument("--out", default=str(ROOT / "data" / "processed" / "terrain"))
    ap.add_argument("--min-accum-acres", type=float, default=5.0, help="contributing area to flag concentrated flow")
    ap.add_argument("--slope-terrace", type=float, default=3.0, help="slope %% above which terrace/contour is considered")
    ap.add_argument("--smooth", action="store_true", help="3x3 mean smoothing before analysis")
    a = ap.parse_args()

    out = Path(a.out) / a.field
    out.mkdir(parents=True, exist_ok=True)
    with rasterio.open(a.dem) as src:
        z = src.read(1).astype(np.float64)
        nodata = src.nodata
        profile = src.profile
        res = float(abs(src.res[0]))
        transform = src.transform
    if nodata is not None:
        z[z == nodata] = np.nan
    valid = ~np.isnan(z)
    z_fill = np.where(valid, z, np.nanmax(z))
    if a.smooth:
        pad = np.pad(z_fill, 1, mode="edge")
        z_fill = sum(pad[1 + dr:1 + dr + z.shape[0], 1 + dc:1 + dc + z.shape[1]] for dr, dc in D8 + [(0, 0)]) / 9.0
    z_fill = fill_pits(z_fill)

    slope = slope_pct(z_fill, res)
    direction = d8_direction(z_fill, res)
    acc = flow_accumulation(z_fill, direction)
    cell_acres = res * res / SQM_PER_ACRE
    acc_acres = acc * cell_acres
    sca = acc * res  # specific catchment area (m)
    beta = np.arctan(np.maximum(slope / 100.0, 0.001))
    twi = np.log(sca / np.tan(beta))
    zmin, zmax = np.nanmin(z_fill[valid]), np.nanmax(z_fill[valid])
    rel_elev = (z_fill - zmin) / max(zmax - zmin, 1e-6)
    zone = classify(slope, twi, acc_acres, rel_elev, a.slope_terrace, a.min_accum_acres)
    zone[~valid] = 0

    profile.update(dtype="float32", count=1, nodata=-9999.0)
    for name, arr in {"slope_pct": slope, "flow_acc_acres": acc_acres, "twi": twi, "rel_elev": rel_elev}.items():
        arr = np.where(valid, arr, -9999.0).astype("float32")
        with rasterio.open(out / f"{name}.tif", "w", **profile) as dst:
            dst.write(arr, 1)
    zprof = dict(profile, dtype="uint8", nodata=0)
    with rasterio.open(out / "water_zones.tif", "w", **zprof) as dst:
        dst.write(zone, 1)

    names = {1: "shedding", 2: "transmitting", 3: "receiving", 4: "ponding", 5: "conveying"}
    total_acres = valid.sum() * cell_acres
    print(f"field {a.field}: {total_acres:.1f} acres, {res:.1f} m cells, elevation range {zmax - zmin:.1f} m")
    print(f"{'zone':13}{'acres':>8}{'pct':>7}{'mean slope %':>14}{'mean TWI':>10}")
    summary = []
    for k, nm in names.items():
        m = zone == k
        if m.any():
            row = (nm, m.sum() * cell_acres, 100 * m.sum() / valid.sum(), float(slope[m].mean()), float(twi[m].mean()))
            summary.append(row)
            print(f"{row[0]:13}{row[1]:8.1f}{row[2]:7.1f}{row[3]:14.2f}{row[4]:10.2f}")

    # candidate concentrated-flow points: local maxima of accumulation above threshold, spaced out
    cand = []
    mask = (acc_acres >= a.min_accum_acres) & valid
    idxs = np.argwhere(mask)
    taken = np.zeros(z.shape, dtype=bool)
    spacing = max(int(30 / res), 3)
    for r, c in sorted(idxs.tolist(), key=lambda rc: -acc_acres[rc[0], rc[1]]):
        if taken[r, c]:
            continue
        x, y = xy(transform, r, c)
        kind = "waterway/WASCOB candidate" if slope[r, c] >= 0.5 else "ponding/basin candidate"
        cand.append(dict(field_id=a.field, row=r, col=c, x=round(x, 1), y=round(y, 1),
                         contributing_acres=round(acc_acres[r, c], 1), slope_pct=round(float(slope[r, c]), 2),
                         twi=round(float(twi[r, c]), 2), zone=names.get(int(zone[r, c]), "nodata"), kind=kind))
        taken[max(0, r - spacing):r + spacing + 1, max(0, c - spacing):c + spacing + 1] = True
        if len(cand) >= 25:
            break
    with (out / "candidates.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["field_id", "row", "col", "x", "y", "contributing_acres", "slope_pct", "twi", "zone", "kind"])
        w.writeheader(); w.writerows(cand)
    with (out / "zone_summary.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["field_id", "zone", "acres", "pct", "mean_slope_pct", "mean_twi"])
        for row in summary:
            w.writerow([a.field, row[0], round(row[1], 1), round(row[2], 1), round(row[3], 2), round(row[4], 2)])
    print(f"\n{len(cand)} concentrated-flow candidates (>= {a.min_accum_acres} acres contributing); outputs in {out}")
    for c in cand[:8]:
        print(f"  x={c['x']} y={c['y']} contributing {c['contributing_acres']} ac slope {c['slope_pct']}% {c['kind']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
