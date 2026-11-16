#!/usr/bin/env python3
"""Per-field fertility recommendations from data/processed/soil_tests.csv using K-State
style formulas (see knowledge/agronomy/soils-and-fertility.md; coefficients marked verify).

Usage:
  python3 scripts/soil_test_recommend.py --season 2027 [--crops wheat,sorghum,corn,soybean]
         [--yield-goals field_id:crop=bu,...] [--prices n=0.55,p2o5=0.80,k2o=0.45,lime=35]

Writes plans/<season>/soil-recommendations.csv and prints a summary. Uses the most
recent 0-6 in and 0-24 in samples per field. Yield goals default to the values in
DEFAULT_YIELD_GOALS; override per field with --yield-goals.
"""
import argparse
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "data" / "processed" / "soil_tests.csv"

# K-State-form coefficients (verify against current MF2586)
N_FORMULA = {  # crop: (lb N per bu yield goal, OM credit per %OM, cap)
    "corn": (1.6, 20, 240),
    "sorghum": (1.6, 20, 180),
    "wheat": (2.4, 10, 150),
    "sunflower": (0.065, 0, 120),  # yield goal in lb for sunflower
}
NO_N = {"soybean", "alfalfa"}
P_CRITICAL, K_CRITICAL = 20.0, 130.0
P_BUILD_LB_PER_PPM, K_BUILD_LB_PER_PPM = 18.0, 8.0  # verify
REMOVAL_P2O5 = {"corn": 0.33, "sorghum": 0.40, "wheat": 0.50, "soybean": 0.80, "sunflower": 0.015}
REMOVAL_K2O = {"corn": 0.26, "sorghum": 0.30, "wheat": 0.30, "soybean": 1.20, "sunflower": 0.01}
DEFAULT_YIELD_GOALS = {"corn": 110, "sorghum": 80, "wheat": 50, "soybean": 38, "sunflower": 1500}
PH_TARGET = {"wheat": 6.0, "sorghum": 6.0, "corn": 6.0, "soybean": 6.3, "sunflower": 6.0, "alfalfa": 6.5}
NO_TILL_OM_FACTOR = 0.5
DEFAULT_PRICES = {"n": 0.55, "p2o5": 0.80, "k2o": 0.45, "lime": 35.0, "s": 0.60, "cl": 0.30, "zn": 2.50}


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def latest_tests():
    by_field = defaultdict(dict)
    with TESTS.open(newline="") as f:
        for r in csv.DictReader(f):
            key = "top" if r["depth_in"].strip().startswith("0-6") else "profile"
            cur = by_field[r["field_id"]].get(key)
            if cur is None or r["sample_date"] > cur["sample_date"]:
                by_field[r["field_id"]][key] = r
    return by_field


def lime_rate(buffer_ph, ph, target):
    """Rough ECC tons/acre from buffer pH; replace with K-State table (verify)."""
    if ph is None or ph >= target - 0.2:
        return 0.0
    if buffer_ph is None:
        return 2.0
    return max(0.0, min(4.0, round((7.0 - buffer_ph) * 4.0, 1)))


def recommend(field, tests, crop, yg, prices, no_till=True):
    top, prof = tests.get("top", {}), tests.get("profile", {})
    ph, bph, om = num(top.get("ph_water")), num(top.get("buffer_ph")), num(top.get("om_pct"))
    p, k = num(top.get("p_ppm")), num(top.get("k_ppm"))
    no3 = num(prof.get("no3_n_lb_acre")) or 0.0
    s_ppm, cl, zn = num(prof.get("so4_s_ppm")), num(prof.get("cl_lb_acre")), num(top.get("zn_ppm"))
    notes = []
    # nitrogen
    if crop in NO_N:
        n_rec = 0.0
    else:
        a, b, cap = N_FORMULA[crop]
        om_credit = b * (om or 0) * (NO_TILL_OM_FACTOR if no_till else 1.0)
        n_rec = max(0.0, min(cap, a * yg - om_credit - no3))
        if no3 >= 80 and crop == "wheat":
            notes.append("profile N high: minimal topdress")
    # phosphorus
    removal_p = REMOVAL_P2O5[crop] * yg
    if p is None:
        p_rec, notes_p = removal_p, "no P test: maintenance only, sample"
    elif p < P_CRITICAL:
        p_rec, notes_p = removal_p + (P_CRITICAL - p) * P_BUILD_LB_PER_PPM / 4, "build (4-yr)"
    elif p <= 30:
        p_rec, notes_p = removal_p, "maintain"
    elif p <= 50:
        p_rec, notes_p = (15.0 if crop in ("corn", "sorghum") else 0.0), "drawdown; starter only"
    else:
        p_rec, notes_p = 0.0, "very high; none"
    notes.append(f"P {notes_p}")
    # potassium
    removal_k = REMOVAL_K2O[crop] * yg
    if k is None:
        k_rec, notes_k = removal_k, "no K test"
    elif k < K_CRITICAL:
        k_rec, notes_k = removal_k + (K_CRITICAL - k) * K_BUILD_LB_PER_PPM / 4, "build (4-yr)"
    elif k <= 160:
        k_rec, notes_k = removal_k, "maintain"
    else:
        k_rec, notes_k = 0.0, "high; none"
    notes.append(f"K {notes_k}")
    # lime, S, Cl, Zn
    lime = lime_rate(bph, ph, PH_TARGET.get(crop, 6.0))
    if ph is not None and ph > 7.5 and crop in ("sorghum", "soybean"):
        notes.append("high pH: iron chlorosis risk; tolerant genetics")
    s_rec = 15.0 if (s_ppm is not None and s_ppm < 10 and crop in ("wheat", "corn", "sunflower")) else 0.0
    cl_rec = 15.0 if (cl is not None and cl < 30 and crop in ("wheat", "sorghum")) else 0.0
    zn_rec = 1.5 if (zn is not None and zn < 0.8 and crop in ("corn", "sorghum")) else 0.0
    cost = (n_rec * prices["n"] + p_rec * prices["p2o5"] + k_rec * prices["k2o"] + lime * prices["lime"] / 3
            + s_rec * prices["s"] + cl_rec * prices["cl"] + zn_rec * prices["zn"])  # lime amortized 3 yr
    return dict(field_id=field, crop=crop, yield_goal=yg, ph=ph, om_pct=om, p_ppm=p, k_ppm=k, profile_no3_lb=no3,
                n_lb=round(n_rec), p2o5_lb=round(p_rec), k2o_lb=round(k_rec), lime_t_ecc=lime, s_lb=s_rec, cl_lb=cl_rec,
                zn_lb=zn_rec, fert_cost_per_acre=round(cost, 2), notes="; ".join(notes))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", required=True)
    ap.add_argument("--crops", default="wheat,sorghum,corn,soybean")
    ap.add_argument("--yield-goals", default="", help="field:crop=value,...")
    ap.add_argument("--prices", default="", help="n=0.55,p2o5=0.80,...  (USD per lb nutrient; lime per ton ECC)")
    ap.add_argument("--tilled", action="store_true", help="use full OM credit (conventional tillage)")
    a = ap.parse_args()
    prices = dict(DEFAULT_PRICES)
    for kv in filter(None, a.prices.split(",")):
        k, v = kv.split("="); prices[k] = float(v)
    overrides = {}
    for kv in filter(None, a.yield_goals.split(",")):
        fc, v = kv.split("="); overrides[tuple(fc.split(":"))] = float(v)
    tests = latest_tests()
    if not tests:
        print("no soil tests logged in", TESTS); return 1
    out_dir = ROOT / "plans" / a.season
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "soil-recommendations.csv"
    rows = []
    for field, t in sorted(tests.items()):
        for crop in a.crops.split(","):
            yg = overrides.get((field, crop), DEFAULT_YIELD_GOALS[crop])
            rows.append(recommend(field, t, crop, yg, prices, no_till=not a.tilled))
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(f"wrote {out} ({len(rows)} rows)")
    for r in rows:
        print(f"{r['field_id']:10} {r['crop']:9} N {r['n_lb']:>4} P2O5 {r['p2o5_lb']:>4} K2O {r['k2o_lb']:>4} lime {r['lime_t_ecc']:>3} $/ac {r['fert_cost_per_acre']:>7}  {r['notes']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
