---
title: In-field water capture and moisture conservation
domain: water
last_reviewed: 2026-11-16
review_cadence: annual; after each drought season review results
confidence: medium (practice effects are ranges from Plains research; site effects come from the farm's own terrain analysis and yield maps)
sources:
  - K-State Research and Extension: no-till and residue management research (Hays, Garden City, Tribune); terrace and conservation structure guidance (MF publications)
  - USDA NRCS Conservation Practice Standards: Terrace (600), Water and Sediment Control Basin (638), Grassed Waterway (412), Contour Farming (330), Residue and Tillage Management No-Till (329), Pond (378), Cover Crop (340)
  - USDA-ARS Bushland TX and Oklahoma State University furrow-diking and tied-ridge research (Southern Plains dryland)
  - Kansas Department of Agriculture, Division of Water Resources: dam and pond permitting thresholds; water appropriation rules
  - Kansas Data Access and Support Center (DASC) LiDAR DEM; USGS 3DEP 1 m DEM
  - USDA NRCS SSURGO soil survey (available water capacity, hydrologic group)
  - K-State and Kansas Geological Survey playa and depression research
used_by_agents:
  - water-management
  - agronomist
  - orchestrator-planner
---

# In-field water capture and moisture conservation

## Summary
In dryland south-central Kansas, water is the first yield limit, and in a drought season
the difference between a 20 and a 40 bushel sorghum crop is often two to three inches of
stored soil water. Rain falls unevenly across a field and runs off from slopes to
depressions and waterways. The goal of this file is to find where water concentrates or
leaves each field, keep it in the root zone, and match crop and population to each
field's water. Structural capture (terraces, basins, ponds) is a one-time investment with
NRCS cost share; management capture (residue, no-till, furrow diking, early canopy) costs
little and applies everywhere. Terrain analysis from LiDAR plus yield maps shows which
areas pay.

## Where water goes in a field
| Landscape position | Water behavior | Yield pattern | Opportunity |
|---|---|---|---|
| Summit and shoulder | sheds water; thin topsoil | lowest in drought | residue, no-till, lower population, contour or terrace to slow runoff |
| Backslope | runoff and erosion; water passes through | moderate, variable | terraces, contour farming, strip cropping; keep residue |
| Footslope and toeslope | receives runoff and sediment; deeper soil | highest in drought, may pond in wet years | highest population and fertility; keep drainage for wet years |
| Depressions and playas | ponding, slow infiltration on clay | drowned in wet years, best in dry | manage as separate zone; consider basin or shallow water storage |
| Waterways and draws | concentrated flow, gully risk | poor, often lost acres | grassed waterway or WASCOB; stop farming the gully |
| Field edges along roads and terraces | compaction, water diversion | variable | fix compaction; check terrace outlets |

## Practices, ranked for this operation
| Rank | Practice | What it captures | Typical effect | Cost | Cost share | Rule |
|---|---|---|---|---|---|---|
| 1 | No-till with full residue retention | infiltration up, evaporation down, snow catch | 1–3 in extra stored water/yr; +5–15% dryland yield in dry years | planter and sprayer only | EQIP 329 | default on every acre |
| 2 | Crop residue height and standing stubble (strip cut wheat high) | snow and wind protection, lower evaporation | 0.5–1.5 in extra stored water into the next crop | none | — | cut wheat 12–18 in where sorghum or corn follows |
| 3 | Early canopy and population by zone | shades soil, less evaporation; population matched to water | +3–8% yield; seed savings on dry zones | VRT planter | — | set population by water zone |
| 4 | Terraces and contour farming on slopes > 2–3% | slows runoff, holds water on backslopes | runoff cut 30–60%; erosion cut sharply; yield +0–10% on slope | $0.75–2.00 per linear ft (verify) | EQIP 600, 330 | rebuild or maintain existing; new where terrain analysis shows runoff loss |
| 5 | Water and sediment control basins (WASCOB) in draws | stops gullies, holds runoff to infiltrate | recovers farmed draw acres; local infiltration | $3,000–15,000 each (verify) | EQIP 638 | where flow accumulation is high and a gully is forming |
| 6 | Grassed waterways | safe conveyance, stops gullies | protects downstream acres | $1,000–4,000 per acre of waterway (verify) | EQIP 412 | where concentrated flow cannot be held |
| 7 | Furrow diking or tied ridges in row crops | small dams in furrows hold rain in place | Southern Plains research: +0–15% sorghum and cotton in dry years, nil in wet | diker attachment $5–15k; one pass | — | trial on sloping sorghum fields |
| 8 | Fallow and crop sequence for water (e.g. wheat–sorghum–fallow where needed) | banks water across seasons | fallow stores 20–40% of precipitation under residue | lost crop year | — | only on the driest, poorest fields; usually beaten by continuous no-till |
| 9 | Cover crops, grazed or terminated early | structure and infiltration; but uses water | mixed in dryland Kansas; can cost yield in dry years | $15–35/acre | EQIP 340 | only where erosion or grazing value justifies; terminate early |
| 10 | Farm ponds and small reservoirs | stores runoff for livestock or limited irrigation | localized; permit and water right rules apply | $10,000–100,000+ | EQIP 378; DWR permit | only with a defined use and permit |
| 11 | Playa and depression management | let natural depressions recharge; farm or retire by economics | drought-year yield island; wet-year loss | none or retire | CRP, EQIP | zone it; consider retiring chronic losers |
| 12 | Compaction relief on headlands and traffic lanes | restores infiltration | local recovery 10–30% | controlled traffic, occasional deep ripping | — | after mapping |

## Terrain analysis method
1. Obtain a 1 m or 2 m LiDAR DEM for each field (Kansas DASC or USGS 3DEP). Clip to the
   field boundary with a buffer.
2. Run `scripts/terrain_water_analysis.py` to compute slope, D8 flow accumulation,
   topographic wetness index (TWI), and relative elevation. The script outputs rasters and
   a CSV of candidate sites: concentrated-flow points (basin or waterway candidates),
   high-TWI zones (water-receiving areas), and high-slope zones (runoff-shedding areas).
3. Overlay SSURGO soil data: available water capacity, hydrologic group, depth to
   restrictive layer. A high-TWI area on a deep loam is a drought-year yield island; on a
   claypan it is a wet-year drown-out.
4. Overlay yield maps for at least one dry and one wet year. Confirm which zones gain in
   drought.
5. Classify each field into water zones: shedding, transmitting, receiving, ponding,
   conveying. Record acreage per zone in `data/processed/field_water_zones.csv`.
6. Match the practice table to each zone. Cost each structural option with NRCS and local
   contractor rates; estimate yield gain from the zone's drought-year yield gap.
7. Write the field water plan and hand population and fertility by zone to the
   agronomist, structures to the capital plan, and cost-share applications to the
   compliance officer.

## Kansas rules to check
- Terraces, basins and waterways on cropland generally need no water permit, but dams
  above Division of Water Resources size thresholds (height, storage) require a permit,
  and storing water for irrigation requires a water right. Verify thresholds with KDA-DWR.
- Altering drainage that affects neighbors can create liability; check before diverting
  concentrated flow.
- Wetland and highly erodible land compliance (NRCS) applies to structural changes if
  farm program benefits are received.
- NRCS EQIP and CSP cost share require an approved conservation plan; apply the season
  before construction.

## Drought-season playbook
- Before planting: use the water-zone map to lower population on shedding zones, hold or
  raise on receiving zones; keep all residue standing; consider sorghum over corn on
  shedding zones.
- In season: no tillage passes; control weeds early (each large weed costs water); for
  wheat, graze-out or hay decision by first hollow stem if the profile is empty.
- After harvest: leave stubble tall; weed-free fallow period stores the most water;
  record stored soil water by zone (probe or gravimetric) to set next year's yield goal.

## Decision rules
1. Every field gets a terrain analysis and water-zone map before the first seasonal plan.
2. Structural practices are proposed only where the analysis shows concentrated flow or
   runoff loss and the drought-year yield gap times affected acres pays back within the
   structure's life at cost-share rates.
3. Management practices ranked 1–3 apply to every acre without further justification.
4. Furrow diking and cover crops go through a strip trial before whole-field use.
5. Any practice that affects neighbors' drainage or needs a permit is cleared by the
   compliance officer first.

## Change log
- 2026-11-16: created.
