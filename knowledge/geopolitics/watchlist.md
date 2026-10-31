---
title: Geopolitical watchlist (live)
domain: geopolitics
last_reviewed: 2026-10-31
review_cadence: weekly
confidence: medium
sources:
  - Updated by the geopolitical-scan skill
used_by_agents:
  - geopolitical-analyst
  - input-cost-analyst
  - market-analyst
---

# Geopolitical watchlist

Living table. One row per situation. Scores follow `monitoring-framework.md`.

| ID | Situation | Region | Status | Probability (6 mo) | Channels | Max impact | Lead | Indicators to watch | Response if triggered | Last update |
|---|---|---|---|---|---|---|---|---|---|---|
| W-001 | Iran war / Strait of Hormuz disruption continues or re-escalates | Gulf | active, unresolved; strait partially open per conflicting reports | high | C1 C2 C3 C4 C7 | 3 | days | transit counts, war-risk premiums, talks status, Brent and ULSD crack, TTF | execute Hormuz response in case study | 2026-10-31 |
| W-002 | Structural Middle East and Russian diesel export decline | global | active | high | C3 | 2 | months | IEA OMR, S&P distillate export data, PADD 2 inventories | forward-contract diesel; cut passes | 2026-10-31 |
| W-003 | Sulfur and phosphate tightness from Gulf disruption | global | active | medium | C2 | 2 | months | World Bank DAP, sulfur benchmarks, NOLA DAP | soil-test driven P deferral or early buy | 2026-10-31 |
| W-004 | China sorghum or soybean tariff action | China | watch | medium | C6 | 3 | days | USTR and MOFCOM announcements, Chinese purchase pace | hedge sorghum; review sorghum acres | 2026-10-31 |
| W-005 | Black Sea wheat export disruption or Russian export tax changes | Russia/Ukraine | watch | medium | C6 C1 | 2 | days | port attacks, export quota decrees | marketing-plan trigger review | 2026-10-31 |
| W-006 | Sanctions changes on Russian or Belarusian fertilizer | Russia/Belarus | watch | medium | C1 C2 | 2 | weeks | OFAC, EU packages | buy K and N layers if soil tests need | 2026-10-31 |
| W-007 | Chinese export controls on urea, phosphate, or agrochemical intermediates | China | watch | medium | C1 C2 C5 | 2 | weeks | customs notices, quota news | buy next-season P; early chemical purchases | 2026-10-31 |
| W-008 | Mexico trade dispute or USMCA review friction | Mexico | watch | low | C6 C10 | 3 | weeks | USTR, USMCA review calendar | wheat and corn hedging review | 2026-10-31 |
| W-009 | Gulf Coast hurricane or Mississippi low water | US | seasonal | medium (Aug–Oct) | C1 C2 C7 | 2 | days | NOAA NHC, USACE river stages | pull fall purchases forward | 2026-10-31 |
| W-010 | Red Sea / Suez shipping attacks | Red Sea | watch | medium | C7 | 1 | days | UKMTO alerts, insurance | freight cost in delivered N | 2026-10-31 |
| W-011 | OPEC+ supply decision | OPEC+ | recurring | medium | C3 | 1 | days | meeting calendar | adjust fuel contract share | 2026-10-31 |
| W-012 | Canadian rail or port strike | Canada | watch | low | C2 C7 | 1 | weeks | union notices | potash timing | 2026-10-31 |
| W-013 | Cyberattack on co-op, elevator, rail or fuel distribution | US | watch | low | C11 | 2 | immediate | CISA advisories, sector news | cash and paper backup; alternate suppliers | 2026-10-31 |
| W-014 | US biofuel policy change (RFS volumes, 45Z) | US | watch | medium | C3 C6 C10 | 2 | months | EPA, Treasury rulemaking | soybean and corn demand outlook | 2026-10-31 |
| W-015 | Avian influenza or livestock disease affecting feed demand | US | watch | medium | C6 C12 | 1 | weeks | USDA APHIS | sorghum and corn feed demand | 2026-10-31 |

Retired items move to `data/processed/geopolitical_events.csv` with an outcome note.

## Change log
- 2026-10-31: created with starter set.
