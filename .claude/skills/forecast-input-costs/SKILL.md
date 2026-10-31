---
name: forecast-input-costs
description: Refresh fertilizer and fuel price forecasts with current market data and geopolitical scenario weights; output P10/P50/P90 by month and per-acre input costs by crop.
---

# Forecast input costs

Run monthly, and immediately after any flagged energy or fertilizer shock.

## Steps
1. **Refresh data.** Run `python3 scripts/fetch_eia_prices.py` (needs `EIA_API_KEY`).
   Record any manually gathered quotes (local co-op, supplier diesel) in
   `data/processed/input_prices.csv` using the schema in `data/reference/input-price-schema.md`.
2. **Read context.** Load the input knowledge files and the two geopolitics files;
   note current scenario probabilities and any indicators past their thresholds.
3. **Baseline.** For each product compute current price, trailing 12-month average,
   3-year percentile, and the seasonal index for the coming months.
4. **Drivers.** Note Henry Hub and TTF (nitrogen), WTI/ULSD curve and crack (diesel),
   benchmark trend (P/K). State the direction and size each implies.
5. **Scenarios.** Apply the scenario overlay from `models/input-price-forecast-model.md`
   to produce P10/P50/P90 per product per month for 18 months.
6. **Translate to the farm.** Cost per lb nutrient and per gallon delivered; cost per
   acre per crop using the input programs in `knowledge/crops/`.
7. **Flags.** Apply decision rules; list buy/defer/fill recommendations with the rule.
8. **Write.** Save to `plans/<season>/input-price-forecast.md` with date, assumptions,
   tables, and flags. Update `last_reviewed` in any knowledge file you corrected.

## Output
A dated forecast file and a short chat summary with the recommendations and any
knowledge-file updates needed.
