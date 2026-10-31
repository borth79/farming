---
title: Propane, natural gas, and grain drying
domain: inputs
last_reviewed: 2026-10-31
review_cadence: seasonal (monthly Aug–Nov)
confidence: medium
sources:
  - EIA propane spot (Mont Belvieu, Conway KS) and weekly residential propane
  - EIA Henry Hub natural gas
  - K-State grain drying cost guides
used_by_agents:
  - input-cost-analyst
  - machinery-and-logistics
---

# Propane, natural gas, and grain drying

## Summary
Drying is a minor cost on this operation unless corn acres grow. Wheat and sorghum are
normally harvested dry enough to store. Propane for corn drying is priced off the
Conway, Kansas hub, which is local and usually trades at a discount to Mont Belvieu.

## Cost model
Drying cost per bushel ≈ (points of moisture removed × gallons propane per point per
bushel × propane price) + electricity for fans + shrink. Typical propane use is about
0.02 gal per point per bushel; verify against the dryer's specification.

## Indicators
| Indicator | Source | Cadence |
|---|---|---|
| Conway propane spot | EIA / OPIS | weekly in season |
| US propane inventories | EIA WPSR | weekly |
| Natural gas Henry Hub | EIA | weekly |
| Supplier summer-fill price | phone | Jun–Aug |

## Decision rules (draft)
- Summer-fill propane tanks when planning corn; the seasonal low is usually Jun–Aug.
- If expected drying cost exceeds the market's harvest-moisture discount schedule,
  consider field dry-down or selling wet to a buyer with drying capacity.

## Change log
- 2026-10-31: created.
