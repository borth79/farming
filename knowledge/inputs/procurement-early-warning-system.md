---
title: Procurement early-warning system — buying ahead of price shocks
domain: inputs
last_reviewed: 2026-11-16
review_cadence: weekly signal run; quarterly review of thresholds; after every shock, a post-mortem
confidence: medium (structure and lead times from the 2026 Iran war case study and prior shocks; thresholds are starting values to calibrate)
sources:
  - knowledge/geopolitics/case-studies/2026-iran-war-lessons-learned.md (price moved in days, retail lagged NOLA 1–3 weeks, physical lag 6–10 weeks)
  - knowledge/inputs/fertilizer-nitrogen.md, fertilizer-phosphorus-potassium.md, diesel-and-fuel.md, input-procurement-strategy.md
  - knowledge/geopolitics/monitoring-framework.md, watchlist.md, scenario-playbook.md
  - 2022 Russia–Ukraine fertilizer and energy shock; 2008 fertilizer spike; 2021–22 supply chain (general industry record; add citations as case studies are written)
  - EIA, USDA AMS, CME forward curves (data sources in data/reference/free-apis.md)
used_by_agents:
  - input-cost-analyst
  - geopolitical-analyst
  - finance-controller
  - orchestrator-planner
---

# Procurement early-warning system

## Summary
The farm's edge is not predicting wars. It is reacting to leading indicators days to
weeks before the local co-op reprices and before most farmers act. In 2026 the Gulf
urea price moved within days of 28 February; Kansas retail followed in one to three
weeks; the physical shortage arrived six to ten weeks later. A farm that filled nitrogen
and fuel on the first signal paid 40 to 80 percent less than one that waited for the
quote. This file defines the indicator ladder, the thresholds that trigger a purchase,
how much to buy, and the limits that keep a wrong signal from becoming a cash problem.
`scripts/procurement_signal.py` runs the ladder weekly.

## The lag chain to exploit
| Stage | Typical lag from event | Who sees it |
|---|---|---|
| Event or credible threat (strike, blockade, sanction draft, export-quota rumor, gas spike) | 0 | news, GDELT volume, trade press, prediction markets |
| Futures and benchmark prices (crude, ULSD, Henry Hub, TTF, NOLA urea) | hours to 2 days | anyone watching the screens |
| Insurance, freight, vessel behavior | 1–5 days | shipping trackers, trade press |
| Wholesale and import-parity fertilizer, rack diesel | 3–10 days | distributors |
| Local retail quotes to farmers | 1–3 weeks | farmers who call |
| Physical availability at the co-op | 4–10 weeks | everyone |
Buy between stage 1 and stage 4, at retail prices that have not yet moved.

## Indicator ladder (longest lead first)
| Tier | Indicator | Lead time | Source | Threshold (starting values; calibrate) | Inputs affected |
|---|---|---|---|---|---|
| A structural | Global capacity, trade policy drafts, sanctions packages in negotiation, El Niño/La Niña outlook, planting intentions | months | watchlist, USDA, CPC | scenario probability moves to "medium" | all |
| B macro | Natural gas 12-month strip (Henry Hub, TTF), crude strip, USD index, interest rates | weeks to months | EIA, CME, FRED | strip up >15% in 30 days | N, diesel, propane |
| C geopolitical | Force posture, talks collapsing, chokepoint incidents, export-license rumors, India tender pricing | days to weeks | geopolitical scan, GDELT, trade press | watchlist item to "high" or incident confirmed | N, P, S, diesel, agchem |
| D market | Front-month futures and benchmarks: WTI, ULSD, Henry Hub, NOLA urea, Tampa ammonia, DAP, potash | hours to days | EIA, CME, trade press | +8% in 5 trading days, or above trailing-12-mo 75th percentile and rising | by product |
| E logistics | War-risk insurance, freight rates, Mississippi stage, Gulf hurricane track, rail service alerts | days | Lloyd's lists, USACE, NOAA, railroads | insurance or freight +25%; river below low-water threshold; hurricane cone over Gulf terminals | N, P, diesel |
| F local | Co-op quote vs benchmark gap, dealer "price-later" withdrawn, prepay deadlines, neighbor buying surge | days | weekly calls | retail unchanged while benchmark up >10% = buying window | by product |
Seasonal overlay: the normal lows (N and propane in June–August, P and K in summer,
diesel before spring maintenance season) are the default tranche windows regardless of
signals.

## Signal to action
Each week the signal script scores every input:
- **Price position**: current price percentile against trailing 3 years, and 30-day
  momentum.
- **Driver pressure**: tier B and D moves in the input's drivers.
- **Scenario pressure**: probability-weighted expected move from the scenario playbook
  (probability × impact for each live scenario touching the input).
- **Retail lag**: benchmark move not yet reflected in the local quote.
Combined into one of four calls:
| Call | Meaning | Action |
|---|---|---|
| BUY-SHOCK | leading indicators fired and retail has not repriced | buy to the storage and prepaid caps within 48 hours; lock forward diesel |
| BUY-TRANCHE | seasonal window or price below 25th percentile, no adverse signal | buy the scheduled tranche |
| HOLD | no edge either way | keep schedule; re-check next week |
| DEFER | price above 75th percentile with easing drivers or de-escalation likely | delay non-essential purchases; buy only to agronomic minimum |
A de-escalation (ceasefire, agreement) during an unresolved conflict is a BUY-TRANCHE
window, not a DEFER, per the 2026 lesson.

## How much to buy: sizing rules
1. **Requirement** = next-season need from the draft crop plan, by product, minus
   inventory and purchases already made.
2. **Caps**: never exceed on-farm storage plus contracted supplier storage; never exceed
   70% of requirement prepaid before the crop plan is fixed; never exceed one supplier's
   counterparty limit; never breach the operating-line headroom set by the finance
   controller.
3. **Tranches**: default 25–35% per tranche across the seasonal windows; BUY-SHOCK
   collapses remaining tranches into one purchase up to the caps.
4. **Bulk discounts**: compare per-unit saving from a larger lot against carrying cost
   (interest on prepaid cash, storage losses, product shelf life) using the model's
   expected price path; buy the larger lot when the expected saving exceeds carrying cost
   by a margin of at least 5%.
5. **Flexibility reserve**: keep 30% of nitrogen unbought until planting intentions are
   firm, unless a BUY-SHOCK fires, because a crop switch to soybeans is itself a hedge.
6. **Fuel**: fill storage to capacity on any BUY-SHOCK; forward-contract 40–60% of
   harvest volume by late spring in normal years.

## Storage as a strategic asset
Buying ahead requires somewhere to put it. Each bin, tank or contracted space converts a
price signal into a saving. Size on-farm storage to hold at least one full season of
nitrogen (liquid or anhydrous), a full season of diesel, and dry fertilizer for one
application. Price storage additions against the saving they enabled in the last shock,
not against normal years. Record capacities in `data/reference/procurement-config.csv`.

## Guardrails against false alarms
- A BUY-SHOCK on a signal that fades costs carrying interest and some flexibility, not the
  farm. A missed shock costs 40–80% on the largest variable input. The asymmetry favors
  acting, within the caps.
- Log every signal and action in `data/processed/procurement_signals.csv` with the
  outcome recorded after 90 days. Calibrate thresholds yearly from hit and false-alarm
  rates.
- Two independent tiers firing (for example C and D) beats one; a single tier-D price
  move without a driver or scenario behind it is a HOLD unless it crosses the percentile
  threshold.

## Weekly routine
1. Run `python3 scripts/fetch_eia_prices.py` and log local quotes.
2. Run the geopolitical scan; update scenario probabilities in
   `data/processed/scenario_probabilities.csv`.
3. Run `python3 scripts/procurement_signal.py`; read the calls.
4. For any BUY call, run the `procurement-timing` skill and execute within the window.
5. Append signals and decisions to the log.

## Decision rules
1. Any BUY-SHOCK call is acted on within 48 hours up to the caps; discussion comes after.
2. No input is ever 100% bought before the crop plan is fixed, except fuel to storage.
3. Thresholds are changed only at the quarterly review or after a shock post-mortem.
4. Storage expansion is evaluated after every shock using the saving it would have made.

## Change log
- 2026-11-16: created.
