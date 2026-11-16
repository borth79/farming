---
name: field-water-analysis
description: Map where water sheds, collects and runs off within a field from LiDAR elevation, soil survey and yield maps; classify water zones; recommend capture and moisture-conservation practices with cost, cost share and payback.
---

# Field water analysis

Run once per field before the first seasonal plan, and again after any structure is
built or when new yield maps arrive. Owner: water-management agent.

## Inputs
- Field boundary (shapefile, GeoJSON or corner coordinates).
- 1–2 m DEM GeoTIFF for the field area (Kansas DASC LiDAR or USGS 3DEP). Save under
  `data/raw/dem/<field_id>/`.
- SSURGO soil polygons or the soil series list for the field (Web Soil Survey export).
- Yield maps for a dry year and a wet year if available (`data/raw/yield/<field_id>/`).

## Steps
1. `python3 scripts/terrain_water_analysis.py data/raw/dem/<field_id>/<dem>.tif --field <field_id>`
   writes slope, flow accumulation, TWI and relative elevation rasters plus
   `candidates.csv` to `data/processed/terrain/<field_id>/` and prints zone acreage.
2. Read the zone summary; overlay soil series: deep loam receiving zones are drought
   islands, claypan ponding zones are wet-year losses.
3. Overlay yield maps; compute per-zone yield in the dry year and the wet year; record
   the drought-year yield gap between shedding and receiving zones.
4. For each concentrated-flow candidate, decide: grassed waterway, WASCOB, terrace outlet
   fix, or leave. For slopes above the terrace threshold, decide terrace or contour.
5. Cost each proposal (NRCS payment schedule, contractor quotes), estimate yield gain
   from the gap times affected acres, compute payback.
6. Set population and fertility adjustments by zone for the agronomist.
7. Check permits and neighbor drainage effects; note EQIP/CSP application timing.
8. Append zones to `data/processed/field_water_zones.csv`; write
   `plans/<season>/water-plan-<field_id>.md`.

## Output
The water plan file, the zones row(s), and a short summary: zones and acres, top
recommendations with payback, permits needed, data gaps.
