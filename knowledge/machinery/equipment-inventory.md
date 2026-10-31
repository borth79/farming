---
title: Equipment inventory
domain: machinery
last_reviewed: 2026-10-31
review_cadence: annual
confidence: low
sources:
  - Operator records (to be supplied)
used_by_agents:
  - machinery-and-logistics
  - finance-controller
  - orchestrator-planner
---

# Equipment inventory

> STUB. Fill one row per machine. Financing detail goes in `equipment-financing.md`;
> cost-per-hour and per-acre figures go in `machinery-costs.md`.

## Register

| ID | Category | Make / model | Year | Size / capacity | Hours or miles | Condition | Ownership | Purchase price | Purchase date | Market value | Insured value | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | Combine | | | class / header width | | | owned / financed / leased / shared / custom | | | | | |
| H1 | Header | | | ft, type | | | | | | | | |
| T1 | Tractor | | | hp, drive | | | | | | | | |
| P1 | Planter or drill | | | rows / ft | | | | | | | | |
| S1 | Sprayer | | | boom ft, tank gal | | | | | | | | |
| G1 | Grain cart | | | bu | | | | | | | | |
| TR1 | Truck / trailer | | | bu or GVW | | | | | | | | |
| TL1 | Tillage | | | ft | | | | | | | | |
| B1 | Bins / dryer / augers | | | bu, bu/hr | | | | | | | | |

Ownership codes: owned outright · financed (see financing file) · leased · shared with
another operation · custom-hired (not owned; see `own-vs-lease-vs-custom.md`).

## Annual fixed-cost summary
Filled from `equipment-financing.md` and `machinery-costs.md`.

| Item | Depreciation | Interest / lease | Insurance | Housing / tax | Total fixed / yr |
|---|---|---|---|---|---|

## Capacity check against 1,000 acres
Acres per workable day for planting, spraying and harvest, versus the window for each
crop. Gaps indicate where custom hire or a second machine is needed.

## Change log
- 2026-10-31: stub created.
