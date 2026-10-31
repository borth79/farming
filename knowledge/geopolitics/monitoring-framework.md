---
title: Geopolitical and hostile-activity monitoring framework
domain: geopolitics
last_reviewed: 2026-10-31
review_cadence: framework annual; watchlist weekly
confidence: medium
sources:
  - Case study: knowledge/geopolitics/case-studies/2026-iran-war-lessons-learned.md
  - Lloyd's Joint War Committee listed areas; IEA, EIA, WTO trade trackers
used_by_agents:
  - geopolitical-analyst
  - input-cost-analyst
  - market-analyst
  - red-team-reviewer
---

# Geopolitical and hostile-activity monitoring framework

## Purpose
Identify, early and systematically, events anywhere in the world that could change
this farm's input costs, grain prices, export demand, freight, credit, or operating
ability. The framework defines what to watch, how to score it, and how a signal becomes
a planning action. The weekly `geopolitical-scan` skill runs it; results land in
`watchlist.md`, `geopolitical-risk-register.md`, and `data/processed/geopolitical_events.csv`.

## Exposure channels (what an event can touch)
| Channel | Farm cost or revenue line | Typical speed |
|---|---|---|
| C1 Nitrogen supply | urea, UAN, anhydrous | days (price), weeks (physical) |
| C2 Phosphate / sulfur / potash | MAP, DAP, potash | weeks–months |
| C3 Crude and distillate | diesel, propane | days |
| C4 Natural gas | nitrogen cost, drying | weeks |
| C5 Agrochemical actives | herbicides, fungicides, insecticides | months |
| C6 Grain export demand | wheat, sorghum, corn, soybean prices and basis | days–weeks |
| C7 Freight and insurance | delivered input cost, export basis | immediate |
| C8 Currency and rates | competitiveness, operating-line cost | weeks |
| C9 Machinery and parts | steel, components, tariffs | months |
| C10 Domestic policy | farm programs, biofuel policy, tariffs | policy cycle |
| C11 Cyber and infrastructure | co-op, elevator, rail, pipeline, payment systems | immediate |
| C12 Biosecurity | animal and plant disease, trade bans | weeks |

## Event categories to monitor
1. Armed conflict and military posture (state and non-state).
2. Maritime chokepoint disruption, piracy, and shipping attacks.
3. Sanctions, embargoes, and financial restrictions.
4. Export bans, quotas, and licensing on fertilizer, grain, or chemicals.
5. Tariffs, trade disputes, and trade agreements.
6. Energy supply decisions (OPEC+, pipeline politics, LNG).
7. Political instability, coups, elections in exporter or buyer nations.
8. Cyberattacks on agriculture, logistics, energy, or finance.
9. Infrastructure failures and strikes (ports, rail, canals, rivers).
10. Pandemics, animal disease outbreaks, and plant quarantine actions.
11. Extreme weather and crop failure in competitor or buyer regions.
12. Domestic policy shifts (farm bill, RFS/45Z, immigration and labor, water law).

## Watch regions and actors (starter set; detail in `watchlist.md`)
| Region / actor | Why it matters to Sedgwick County | Primary channels |
|---|---|---|
| Iran, Gulf states, Strait of Hormuz | quarter of world urea, Gulf diesel, LNG, sulfur | C1 C2 C3 C4 C7 |
| Russia, Ukraine, Black Sea | wheat export competitor, urea and ammonia, potash via Belarus, diesel exports | C1 C2 C3 C6 |
| Belarus | potash | C2 |
| China | sorghum and soybean buyer; urea and phosphate export controls; agrochemical actives; diesel export limits | C1 C2 C5 C6 |
| Mexico | top buyer of Kansas wheat and corn; USMCA | C6 C10 |
| India | urea tenders set global nitrogen tone; wheat and rice policy | C1 C6 |
| Morocco (OCP) | phosphate | C2 |
| Canada | potash, rail strikes | C2 C7 |
| Brazil, Argentina, Australia, EU | grain export competitors; currency moves | C6 C8 |
| Red Sea / Suez, Panama Canal, Bosporus, Taiwan Strait | freight routing and insurance | C7 |
| Gulf of Mexico and Mississippi River | import logistics for fertilizer; export logistics for grain; hurricanes; low water | C1 C2 C7 |
| US federal policy | tariffs, sanctions, farm programs, biofuels, EPA labels | C5 C10 |
| OPEC+ | crude supply | C3 |

## Scoring
Each event or developing situation gets:
- **Probability** (next 6 months): low <15%, medium 15–50%, high >50%.
- **Impact** on each channel: 0 none, 1 minor (<5% price), 2 material (5–20%), 3 severe (>20%).
- **Lead time**: days, weeks, months.
- **Exposure score** = probability band × max impact; anything medium/2 or higher
  enters the risk register with a named response.

## From signal to action
1. Detect: automated feeds (GDELT, news RSS, trade trackers, price feeds) plus manual
   weekly scan.
2. Classify: category, region, channels, score.
3. Log: append to `data/processed/geopolitical_events.csv`.
4. Decide: if the exposure score crosses the threshold, update scenario probabilities
   in `scenario-playbook.md`, notify the input-cost analyst and market analyst, and
   invoke `procurement-timing` or `hedging-decision` as the playbook specifies.
5. Review: monthly, compare flagged events with realized price moves; adjust impact
   estimates.

## Lessons embedded from the 2026 Iran war
Price moves precede physical shortage; de-escalations are buying windows, not
all-clears; diesel shocks outlast nitrogen shocks; grain rarely rallies enough to offset
input spikes. See the case study for detail.

## Change log
- 2026-10-31: created.
