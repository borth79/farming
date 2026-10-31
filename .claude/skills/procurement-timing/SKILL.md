---
name: procurement-timing
description: Decide how much fertilizer or fuel to buy now versus later, using the current forecast, storage, cash position and the layering rules; log the purchase decision.
---

# Procurement timing

Invoke when a buy/defer flag fires, when the supplier offers a prepay or contract, or
before each seasonal buying window (summer N fill, late-spring fuel contracting,
pre-harvest fuel fill, propane summer fill).

## Steps
1. Read `knowledge/inputs/input-procurement-strategy.md` and the relevant input file.
2. Read the latest `plans/<season>/input-price-forecast.md`; if older than 30 days or a
   shock has occurred since, run `forecast-input-costs` first.
3. Determine requirement: quantity needed for the current draft crop plan, less
   quantity already purchased (`data/processed/input_purchases.csv`) and in storage.
4. Check constraints: storage capacity, cash and operating-line headroom (from
   `knowledge/finance/cash-flow-and-credit.md`), supplier counterparty limit, and the
   maximum prepaid share before the crop plan is fixed.
5. Apply the layering rule for the input and the current percentile/flag. Compute the
   recommended quantity and acceptable price, and the expected value versus waiting
   using P10/P50/P90.
6. Recommend: buy X units now at up to $Y, contract Z%, or defer with a re-check date
   and trigger price. State what would change the recommendation.
7. On execution, append the purchase to `input_purchases.csv` with the rule that
   triggered it. Set a re-check reminder for the next layer.

## Output
A decision record in `plans/<season>/procurement-log.md` and a one-paragraph summary.
