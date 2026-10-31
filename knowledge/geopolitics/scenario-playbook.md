---
title: Scenario playbook
domain: geopolitics
last_reviewed: 2026-10-31
review_cadence: monthly
confidence: medium
sources:
  - knowledge/geopolitics/case-studies/2026-iran-war-lessons-learned.md
  - fertilizer-geopolitics.md, energy-geopolitics.md
used_by_agents:
  - geopolitical-analyst
  - input-cost-analyst
  - market-analyst
  - orchestrator-planner
---

# Scenario playbook

Pre-written scenarios with current probability, trigger indicators, expected impact on
this farm, and the actions to take without further deliberation. Probabilities are set
in the weekly scan. The crop plan carries each scenario's input and price effects.

| Scenario | Current probability (6 mo) | Triggers | Impact on this farm | Pre-committed actions |
|---|---|---|---|---|
| S1 Hormuz re-closure or sustained attacks | high while talks fail | insurance withdrawal, transit collapse, strikes resume | urea/UAN +40–80%, diesel +40–65%, P and sulfur tight later | fill fuel; forward-contract harvest diesel; buy N to 70% cap; favor anhydrous |
| S2 Hormuz durable reopening | medium | signed agreement with verified transit recovery | urea and diesel fall over weeks; P lags | buy the next layer on the dip; do not chase lower; keep contracts |
| S3 China sorghum/soybean tariff | medium | USTR or MOFCOM action | sorghum basis −$0.30 to −1.00/bu; soybean price down | hedge sorghum before planting; shift marginal sorghum acres to soybeans or wheat only if agronomy allows |
| S4 Black Sea wheat export disruption | medium | port strikes, export bans | HRW wheat up sharply, short-lived | sell incremental wheat into the rally per marketing plan |
| S5 Russia/Belarus fertilizer sanctions tightened | medium | OFAC/EU announcements | potash and urea up 15–40% | buy potash if soil test needs; accelerate N layering |
| S6 China urea/phosphate export restriction | medium | customs notices | urea +15–30%, DAP +20% | buy next-season P early; add N layer |
| S7 Mexico tariff dispute | low | USTR actions, USMCA review | wheat and corn basis weaker | hedging review; diversify buyers |
| S8 Gulf hurricane or Mississippi low water | seasonal medium | NOAA, USACE | N and P delivered cost +5–15% for weeks; grain basis weaker at harvest | pull fall purchases forward in Jul–Aug; pre-arrange storage |
| S9 Global recession / demand collapse | low–medium | PMIs, inventories | inputs and grain both down | slow purchases; protect price floors with options |
| S10 Domestic policy shock (biofuel cut, aid change) | medium | EPA, Congress | corn and soybean demand; cash flow | update demand outlook; do not plan on aid |

## Operating rules
- A scenario above "medium" probability must have its actions scheduled in the current
  season's plan with owner and date.
- When a trigger fires, the response is executed first and debated afterward.
- Every executed response is logged in `plans/<season>/procurement-log.md` or
  `marketing-log.md` with the scenario ID.

## Change log
- 2026-10-31: created.
