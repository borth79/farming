---
title: Nitrogen fertilizer — cost drivers, markets, and management
domain: inputs
last_reviewed: 2026-10-31
review_cadence: monthly (weekly during Sep–Apr buying season)
confidence: medium
sources:
  - USDA AMS Illinois Production Cost Report (weekly fertilizer prices) — verify current
  - EIA Henry Hub natural gas spot and futures
  - DTN weekly retail fertilizer survey
  - K-State Extension nitrogen recommendations (MF-2586 and successors)
  - Green Markets / Argus / ICIS fertilizer price assessments (subscription)
used_by_agents:
  - input-cost-analyst
  - agronomist
  - finance-controller
  - geopolitical-analyst
---

# Nitrogen fertilizer

## Summary
Nitrogen is the largest variable input cost for wheat, corn and sorghum on this
operation and the most volatile. Price is driven by natural gas (the feedstock),
global urea trade, import dependence at the Gulf, and seasonal demand. Wichita sits
next to a major domestic producer (Koch Fertilizer), which affects local basis but not
the global price. The management task is to buy the right form at the right time and
size the rate to expected yield and price.

## Products used here
| Product | Analysis | Typical use on this farm | Form | Loss risk |
|---|---|---|---|---|
| Anhydrous ammonia | 82-0-0 | Pre-plant corn/sorghum, fall or spring | gas/liquid | low if sealed; needs soil moisture |
| Urea | 46-0-0 | Topdress wheat, pre-plant | dry | volatilization if surface-applied without rain/incorporation |
| UAN 28 / 32 | 28-0-0 / 32-0-0 | Topdress wheat, streamed or dribbled; starter blends | liquid | moderate |
| Ammonium sulfate | 21-0-0-24S | Where sulfur is needed | dry | low |
Always compare on cost per pound of actual N, including application cost.

## Price drivers, in order of impact
1. Natural gas price (Henry Hub for US producers; TTF Europe and Asian LNG for global
   marginal producers). Gas is 70–90% of ammonia production cost.
2. Global urea trade: Middle East, Russia, China export policy, India tender timing.
3. US Gulf (NOLA) import price and barge/rail freight to the Plains.
4. Seasonal demand: fall anhydrous, spring pre-plant, wheat topdress (Feb–Mar).
5. Corn price expectations (demand pull; the corn-to-nitrogen price ratio).
6. Sanctions, tariffs, export bans (see `knowledge/geopolitics/fertilizer-geopolitics.md`).
7. Plant outages, hurricanes on the Gulf Coast, river levels.

## Indicators to track (feed `data/processed/input_prices.csv`)
| Indicator | Source | Cadence | Why |
|---|---|---|---|
| Henry Hub spot and 12-mo strip | EIA / CME | weekly | feedstock cost, 2–3 month lead on ammonia |
| TTF natural gas | ICE | weekly | European production curtailment signal |
| NOLA urea barge | Argus/Green Markets or trade press | weekly | import parity price |
| Tampa ammonia contract | trade press | monthly | US ammonia benchmark |
| Illinois retail anhydrous/urea/UAN | USDA AMS | weekly | nearest public retail benchmark |
| Local co-op cash quote (Sedgwick County) | phone/email | weekly in season | actual price paid |
| India urea tender dates and volumes | trade press | as announced | global demand shock |
| China urea export quota news | trade press | as announced | supply shock |
| Corn Dec futures | CME | daily | demand-side and affordability ratio |

## Seasonal pattern (typical, not guaranteed)
- Summer (Jun–Aug): usually the seasonal low for anhydrous and urea; fill programs.
- Fall (Sep–Nov): rises with fall application demand.
- Winter (Dec–Feb): firm; wheat topdress demand begins.
- Spring (Mar–May): typically the seasonal high; shortages possible.
Buying a share of needs at the summer low is the default; see decision rules.

## Local supply picture
- Koch Fertilizer (Wichita HQ) operates nitrogen production in the region; local
  availability is usually good, but pricing follows NOLA plus freight, not local cost.
- Co-ops and independent retailers serve Sedgwick and surrounding counties; obtain at
  least three quotes per purchase.
- Rail and truck freight from the Gulf add to delivered cost; river closures or rail
  disruptions raise Plains basis.

## Agronomic management levers
- Rate: use yield-goal and soil-test based recommendations (K-State), soil profile
  nitrate test, and credits from legumes and manure.
- Timing and placement: split applications and incorporation reduce loss.
- Stabilizers and inhibitors: evaluate cost versus expected loss conditions.
- Economic optimum rate falls when N is expensive relative to grain; recompute each
  season with current N cost and expected grain price.

## Decision rules (draft, to be ratified)
- Buy 30–50% of next season's N when price is at or below the 3-year seasonal average
  for that month, typically Jun–Aug.
- Add 25% on any confirmed supply shock indicator (export ban, major outage, gas spike)
  if price has not yet fully responded.
- Never hold more than 70% prepaid before the crop plan is fixed; keep flexibility for
  crop switches.
- If N cost per lb exceeds a set ratio to expected grain price, cut rate to the
  recomputed economic optimum and shift acres toward soybeans or lower-N crops.
- Compare anhydrous vs urea vs UAN on delivered cost per lb N plus application cost
  every purchase.

## Open questions
- Current storage capacity for liquid N and anhydrous on farm.
- Which retailers offer prepay and price-later contracts.

## Change log
- 2026-10-31: created.
