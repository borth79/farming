# Fertilizer price model

## Products modeled
Anhydrous ammonia, urea, UAN 32, MAP/DAP, potash — delivered Sedgwick County.

## Structure
Delivered price = benchmark (NOLA or Illinois retail) × pass-through + Plains basis.

### Nitrogen
- Core driver: natural gas. Fit ammonia benchmark against Henry Hub (US producer cost)
  and TTF (global marginal cost) with a 1–3 month lag; urea follows ammonia and the
  NOLA import price.
- Seasonal factor by month from history (summer low, spring high).
- Demand factor: expected US corn acres and the corn-to-N price ratio.
- Shock overlay: scenario probabilities from `knowledge/geopolitics/fertilizer-geopolitics.md`
  and `energy-geopolitics.md`, each with an impact size (percent move) and duration.

### Phosphate and potash
- Core driver: global benchmark (World Bank monthly or trade press weekly) with
  slow mean reversion; affordability (grain price index) as a demand damper.
- Shock overlay: export restrictions, sanctions, duty changes.

## Procedure
1. Refresh benchmark and local price history.
2. Compute seasonal indices (price in month / trailing 12-mo average, 5-year mean).
3. Update driver relationships (simple regression or ratio) on the latest data.
4. Project baseline P50 by month for 18 months from drivers' forward curves.
5. Apply scenario overlay: mixture distribution across scenarios to get P10 and P90.
6. Convert to cost per lb of N, P2O5, K2O and to cost per acre for each crop program.
7. Emit buy/defer flags per the decision rules in the input knowledge files.

## Known limitations
- Public weekly benchmarks (USDA AMS Illinois) are a proxy; Kansas basis must be
  calibrated from actual local quotes.
- Shock sizes are judgment-based until enough history exists to estimate them.

## Status
Specification only. Implementation planned in `scripts/` once price history is
accumulating in `data/processed/input_prices.csv`.
