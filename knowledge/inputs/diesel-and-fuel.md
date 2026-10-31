---
title: Diesel and fuel — cost drivers, markets, and management
domain: inputs
last_reviewed: 2026-10-31
review_cadence: weekly
confidence: medium
sources:
  - EIA Weekly Retail On-Highway Diesel Prices, Midwest (PADD 2)
  - EIA Gasoline and Diesel Fuel Update; WTI and Brent spot
  - CME NYMEX ULSD (HO) and WTI (CL) futures
  - OPIS / Magellan Group 3 rack pricing (subscription)
  - K-State Farm Management Guides — fuel use per acre by operation
  - Kansas Department of Revenue — dyed (off-road) diesel exemption rules
used_by_agents:
  - input-cost-analyst
  - machinery-and-logistics
  - finance-controller
  - geopolitical-analyst
---

# Diesel and fuel

## Summary
Diesel is the second most volatile input after nitrogen and is used by every field
operation, hauling, and (if irrigated) some pumping. Kansas is supplied from the
Mid-Continent (Group 3) pipeline and rack system, with refineries in McPherson KS,
El Dorado KS, and Oklahoma. Price follows crude oil plus the diesel crack spread, with
seasonal and geopolitical shocks on top. Management is a mix of consumption reduction,
on-farm storage, forward contracts with the supplier, and optional futures hedging.

## Consumption model
Fuel use per acre by operation (K-State reference values; replace with farm records):
| Operation | Gal/acre (typical range) |
|---|---|
| No-till planting / drilling | 0.4–0.7 |
| Spraying | 0.1–0.2 |
| Anhydrous application | 0.6–1.0 |
| Vertical tillage / light tillage | 0.5–0.9 |
| Chisel / heavy tillage | 1.0–1.8 |
| Combine harvest, wheat | 1.0–1.5 |
| Combine harvest, corn/sorghum | 1.5–2.5 |
| Grain cart and hauling | 0.3–0.8 |
| Irrigation (diesel engine) | per acre-inch; depends on lift and pressure |
Annual farm total = sum over planned operations × acres, plus trucking and overhead.
At 1,000 acres of a wheat/sorghum/soybean mix, expect low thousands of gallons per
season before hauling; corn-heavy and tilled systems use more.

## Price structure
Delivered farm price = crude oil + diesel crack spread + pipeline/rack basis (Group 3)
+ distributor margin and delivery − excise tax exemption (dyed off-road diesel).
- Crude: WTI/Brent, driven by OPEC+, demand, sanctions, inventories.
- Crack spread: refinery capacity, outages, distillate inventories, exports.
- Seasonal: distillate demand peaks in winter (heating oil) and at harvest; spring
  refinery maintenance tightens supply.
- Renewable diesel and biodiesel blending policy (RFS, RINs, 45Z) affects price.

## Indicators
| Indicator | Source | Cadence |
|---|---|---|
| EIA Midwest retail diesel | EIA (API series available) | weekly |
| WTI front month and 12-mo strip | CME / EIA | daily |
| NYMEX ULSD front month | CME | daily |
| Distillate inventories (PADD 2 and US) | EIA Weekly Petroleum Status Report | weekly |
| Diesel crack spread (ULSD − WTI) | computed | weekly |
| Group 3 rack diesel, Wichita area | OPIS or supplier | weekly |
| Supplier delivered quote, dyed diesel | phone | before purchase |
| Geopolitical shock flags | `knowledge/geopolitics/energy-geopolitics.md` | as needed |

## Management levers
- Reduce consumption: no-till, fewer passes, right-sizing tractors to implements,
  engine maintenance, tire pressure, reduced idling, route planning for hauling.
- Storage: size on-farm tanks to cover a full season's peak (planting, harvest) so
  purchases can be timed; mind tank regulations and fuel quality (water, microbes).
- Forward contracts: fixed-price or capped-price contracts with the fuel supplier for
  a portion of the season's volume.
- Futures/options: NYMEX ULSD contract is 42,000 gal; too large for most of this
  operation's single purchases, but a single contract or options on it can hedge
  harvest-season volume. Basis risk between NYMEX and Group 3 remains.
- Fuel tax: ensure off-road use is dyed, exempt diesel; keep records for audits.

## Decision rules (draft)
- Keep storage at least 50% full when price is below its 12-month average; fill when
  below the 25th percentile of the trailing 3 years.
- Forward-contract 40–60% of harvest-season volume by late spring if the forward curve
  is flat or backwardated and no supply shock is flagged.
- On a flagged geopolitical shock (Hormuz, major refinery outage, sanctions step), fill
  storage before the retail price fully responds, typically within 1–2 weeks.
- Reassess tillage passes whenever diesel exceeds a set threshold per gallon.

## Open questions
- On-farm tank capacity and condition.
- Current supplier and whether they offer fixed-price contracts.
- Irrigation engine fuel type, if irrigated.

## Change log
- 2026-10-31: created.
