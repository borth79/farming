---
title: Input procurement strategy
domain: inputs
last_reviewed: 2026-10-31
review_cadence: seasonal
confidence: medium
sources:
  - Operator preferences (to be ratified)
  - Retailer program terms (to be collected)
used_by_agents:
  - input-cost-analyst
  - finance-controller
  - orchestrator-planner
---

# Input procurement strategy

## Summary
The goal is to lower the average cost of inputs and cap downside without locking in
too early or tying up cash. Each input has a different volatility and shelf life, so
the rules differ. Fertilizer and fuel are handled with layered buying; seed and
chemicals mostly with early-pay discounts.

## Layered buying framework
| Input | Volatility | Storable | Prepay / contract options | Default layering |
|---|---|---|---|---|
| Nitrogen | very high | yes (anhydrous, liquid tanks) | prepay, price-later | 30–50% summer, 25% fall, remainder spot |
| P and K | high | yes (dry) | prepay | build when cheap, defer when dear |
| Diesel | very high | yes (tanks) | fixed-price contract, futures/options | 40–60% forward, storage timing |
| Propane | high | yes | summer fill | 100% summer fill of expected need |
| Seed | low | no | early-pay discounts | lock by discount deadlines |
| Herbicides | medium | yes (shelf life) | early-pay, volume | buy generics early; branded by program |
| Fungicide / insecticide | medium | yes | early-pay | buy only what thresholds justify |

## Cash and credit interaction
- Prepaying shifts cash out of the operating cycle; compare the discount or expected
  price saving against the operating-line interest for the prepay period.
- Prepaid expenses can carry tax timing benefits; coordinate with `knowledge/finance/tax-planning.md`.
- Counterparty risk: prepaying a retailer is an unsecured loan to them; limit exposure
  per supplier.

## Process each season
1. Build the input requirement from the draft crop plan (quantities by product).
2. Pull current prices and the forecast from `models/input-price-forecast-model.md`.
3. Apply the decision rules in each input file and this layering table.
4. Record every purchase in `data/processed/input_purchases.csv` with date, product,
   quantity, unit, price, supplier, and the rule that triggered it.
5. Review realized versus forecast after the season in the post-harvest review.

## Change log
- 2026-10-31: created.
