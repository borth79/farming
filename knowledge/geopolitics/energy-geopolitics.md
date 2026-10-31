---
title: Energy geopolitics — crude, diesel, natural gas
domain: geopolitics
last_reviewed: 2026-10-31
review_cadence: weekly scan
confidence: medium
sources:
  - EIA Short-Term Energy Outlook
  - IEA Oil Market Report
  - OPEC+ meeting communiqués
  - Shipping and insurance notices (Red Sea, Hormuz, Black Sea)
used_by_agents:
  - geopolitical-analyst
  - input-cost-analyst
---

# Energy geopolitics

## Summary
Energy feeds two of this farm's largest costs directly (diesel, and natural gas via
nitrogen) and a third indirectly (propane). This file tracks the events that move crude,
distillate and gas, and maps them to procurement actions.

## Exposure map
| Event class | Affects | Transmission | Lead time |
|---|---|---|---|
| OPEC+ production decisions | crude → diesel | global price | days |
| Sanctions on Russian/Iranian/Venezuelan oil | crude, distillate (Russia is a large diesel exporter) | global price and crack spread | days–weeks |
| Chokepoint disruption (Hormuz, Red Sea, Black Sea) | crude, LNG, urea | price spike, freight, insurance | days |
| US refinery outages, hurricanes (Gulf Coast) | diesel crack spread, Mid-Continent supply | regional | days–weeks |
| LNG export growth and European demand | Henry Hub | nitrogen production cost | months |
| US biofuel policy (RFS, 45Z, RIN prices) | diesel price, soybean oil demand | policy cycle | months |
| Pipeline or rail disruptions in Group 3 | local diesel basis | regional | days |

## Scenario register
| Scenario | Trigger indicators | Impact on this farm | Response |
|---|---|---|---|
| Hormuz closure or sustained attacks | shipping alerts, insurance withdrawal, Brent spike | diesel and urea up fast | fill fuel storage, buy N layer, lock forward contracts |
| OPEC+ supply cut | communiqué | crude up moderately | increase forward-contracted fuel share |
| Recession / demand collapse | PMI, inventories building | prices down | slow purchases, run storage down |
| Gulf Coast hurricane season | NOAA forecasts | crack spread up, N logistics | top up fuel in July |
| Henry Hub spike from LNG demand or cold winter | strip above threshold | ammonia cost up with lag | buy N before fertilizer market reprices |

## Thresholds (set and review each season)
- WTI, ULSD, Henry Hub and TTF trigger levels at which the input-cost analyst runs an
  unscheduled forecast update and the procurement skill is invoked.

## Change log
- 2026-10-31: created.
