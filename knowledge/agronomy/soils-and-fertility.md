---
title: Soils, soil testing, and fertility management
domain: agronomy
last_reviewed: 2026-11-16
review_cadence: annual (formulas), per sampling round (data)
confidence: medium (formulas follow K-State MF2586 structure; coefficients marked verify against the current edition)
sources:
  - K-State MF2586 "Soil Test Interpretations and Fertilizer Recommendations" (current edition; verify coefficients)
  - K-State MF734 "Soil Sampling" and MF2254 (grid/zone sampling guidance)
  - K-State Agronomy eUpdates 2025–2026 on nitrogen, phosphorus, potassium, chloride and sulfur
  - K-State soil test lab (Manhattan) analysis packages
  - USDA NRCS Web Soil Survey for Sedgwick County soil series
  - 4R Nutrient Stewardship framework (The Fertilizer Institute)
used_by_agents:
  - agronomist
  - input-cost-analyst
  - orchestrator-planner
---

# Soils, soil testing, and fertility management

## Summary
Soil testing is the cheapest input decision tool on the farm. A $25 to $40 sample per
20 to 40 acres sets the nitrogen, phosphorus, potassium, lime and sulfur program for the
field, and avoids both yield loss from deficiency and money wasted on nutrients the soil
already holds. This file sets the sampling protocol, the interpretation rules in K-State
form, and the build, maintain or drawdown strategy by nutrient. Field results live in
`data/processed/soil_tests.csv`; `scripts/soil_test_recommend.py` turns them into per-field
recommendations.

## Sedgwick County soils (fill from Web Soil Survey per field)
| Soil group | Typical series | Texture | Native pH | Notes |
|---|---|---|---|---|
| Arkansas River corridor | Canadian, Lincoln, Waldeck | sandy loam to sand | 6.5–7.8 | low water holding, low CEC, leaching risk, irrigation common |
| Uplands east and north | Irwin, Ladysmith, Goessel | silty clay loam, claypan | 6.0–7.0 | high CEC, slow drainage, strong K supply |
| Terraces and bottoms | Farnum, Shellabarger, Naron | loam, fine sandy loam | 6.0–7.2 | most productive dryland |
| High-pH spots | Tabler, Drummond, saline-sodic patches | | 7.5–8.5 | iron chlorosis in sorghum and soybeans |
Record series, slope, productivity index and CEC per field in `knowledge/land/soil-map-and-productivity.md`.

## Sampling protocol
- **When**: fall after harvest or early spring before fertilizing, same season each cycle.
  Profile nitrate (0–24 in) in late winter before wheat topdress and before corn or
  sorghum planting.
- **Depth**: 0–6 in for pH, P, K, organic matter, zinc; 0–24 in for nitrate, sulfate and
  chloride.
- **Pattern**: 2.5-acre grid where fields are variable or variable-rate application is
  planned; management zones (by soil series, yield map, elevation) otherwise; one
  composite per 20–40 acres minimum, 15–20 cores per composite.
- **Frequency**: pH, P, K every 2–3 years; nitrate, S, Cl annually where those crops need
  them; after lime, retest in 2 years.
- **Lab**: K-State Soil Testing Lab or a lab using the same methods (Mehlich-3 or Bray P1,
  ammonium acetate K, 1:1 water pH, buffer pH, LOI organic matter). Keep methods constant.
- **Log every result** in `data/processed/soil_tests.csv` with field ID, sample ID, date,
  depth, lab and method.

## Interpretation and recommendation rules (K-State form; verify coefficients)
### Nitrogen (lb N/acre)
| Crop | Formula | Credits |
|---|---|---|
| Corn | 1.6 × yield goal − 20 × %OM − profile NO3-N − credits | soybean previous crop 40; alfalfa 60–120 by stand; manure by analysis |
| Grain sorghum | 1.6 × yield goal − 20 × %OM − profile NO3-N − credits | same as corn; +30 lb for wheat after sorghum |
| Wheat | 2.4 × yield goal − 10 × %OM − profile NO3-N − credits | soybean 20–40; grazing adds 30–50 |
| Soybeans, alfalfa | none (fix N) | |
| Sunflower | 0.065 × yield goal (lb) − profile NO3-N | |
- Yield goal = 105% of the 3–5 year average for the field, not the best year.
- Cap recommendations at K-State maxima (corn 230–300 depending on system; verify).
- No-till: halve the organic-matter credit.
- Profile N above 80–100 lb/acre: topdress wheat minimally or not at all.

### Phosphorus (Bray P1 or Mehlich-3 ppm, 0–6 in)
| Soil test P | Category | Strategy |
|---|---|---|
| < 10 | very low | build: crop removal + 1.5–2× removal until 20 ppm |
| 10–20 | low to medium | build: removal + build increment (~18 lb P2O5 raises 1 ppm; verify) |
| 20–30 | optimum (critical 20 ppm) | maintain: replace removal; starter on corn/sorghum |
| 30–50 | high | drawdown: starter only or none; defer purchases when P is expensive |
| > 50 | very high | none |
Removal, lb P2O5 per bushel (verify current K-State values): corn 0.33, sorghum 0.40,
wheat 0.50, soybean 0.80, sunflower 0.015 per lb seed; alfalfa 12 per ton.

### Potassium (ammonium acetate ppm, 0–6 in)
| Soil test K | Category | Strategy |
|---|---|---|
| < 90 | low | build: removal + ~8 lb K2O per ppm (verify) |
| 90–130 | medium | build to 130 |
| 130–160 | optimum (critical 130 ppm) | maintain by removal |
| > 160 | high | none; most Sedgwick upland soils test here |
Removal, lb K2O per bushel: corn 0.26, sorghum 0.30, wheat 0.30, soybean 1.20; alfalfa 60 per ton.

### pH and lime
- Target pH 6.0–6.5 for wheat, sorghum, corn; 6.5+ for alfalfa and soybeans.
- Lime when pH < 5.8 (wheat/sorghum) or < 6.2 (alfalfa). Rate from buffer pH per
  K-State table, expressed as effective calcium carbonate (ECC); typical 1–3 tons ECC.
- Low pH is common after decades of ammonium fertilizer on upland soils; aluminum
  toxicity cuts wheat yield sharply below pH 5.5.
- High pH (> 7.5): no lime; manage iron chlorosis with tolerant hybrids and varieties,
  chelated iron seed treatment, banded acid-forming P.

### Sulfur, chloride, zinc
- Sulfur: sandy, low-OM soils and high-yield wheat, corn, alfalfa respond. K-State
  guideline roughly 10–20 lb S/acre where sulfate-S (0–24 in) is below 10 ppm; use
  ammonium sulfate or thiosulfate.
- Chloride: wheat and sorghum respond where profile Cl is below 30 lb/acre (0–24 in);
  10–20 lb Cl/acre as potash where potassium is not otherwise needed. Many Kansas soils
  are low.
- Zinc: corn and sorghum respond where DTPA Zn < 0.5–1.0 ppm, especially on high-pH,
  eroded or leveled soils; 1–2 lb Zn/acre banded or 5–10 lb broadcast lasts years.
- Boron: alfalfa only, where hot-water B < 0.5 ppm.

## Build, maintain, drawdown economics
- Maintenance replaces removal and holds soil tests steady. It is the default when tests
  are in the optimum range and prices are normal.
- Drawdown is justified when tests are above optimum; the soil pays the fertilizer bill
  for several years with no yield loss. It is the main lever when phosphate and potash
  prices spike (see `knowledge/inputs/fertilizer-phosphorus-potassium.md`).
- Build is justified when tests are below critical and the land is owned (this farm),
  since the investment stays with the owner.
- Variable-rate application by grid or zone pays where within-field test range spans two
  or more categories; otherwise a flat rate is fine.

## Decision rules
1. No fertilizer purchase without a soil test less than three years old for the field.
2. Nitrogen rate is set per field from the formula above with profile N measured, never
   from a flat rate per crop.
3. When P or K tests are above optimum and prices are in the top third of their 5-year
   range, draw down; when below critical and prices are in the bottom third, build.
4. Lime before any other correction when pH is below target; nothing else works well on
   acid soil.
5. Starter P on corn and sorghum on soils testing below 30 ppm or planted into cold soil
   regardless of broadcast P.
6. Re-test two years after lime or any build program to confirm the response.

## Change log
- 2026-11-16: created.
