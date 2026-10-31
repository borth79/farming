---
name: geopolitical-scan
description: Weekly scan of conflicts, sanctions, trade policy, chokepoints, cyber, biosecurity and policy events worldwide; score exposure to the farm, update the watchlist, scenario probabilities and event log, and hand off triggered actions.
---

# Geopolitical scan

Run weekly (Monday) and immediately when a major event breaks.

## Steps
1. **Pull automated feeds.** Run `python3 scripts/fetch_gdelt_events.py` to collect
   recent article volume and headlines for each watch topic (no API key needed).
   Review price feeds already in `data/processed/input_prices.csv` for moves beyond
   thresholds in `energy-geopolitics.md`.
2. **Search by category.** For each of the twelve categories in
   `monitoring-framework.md`, run targeted web searches for the past seven days across
   the watch regions. Note anything new, escalated, or de-escalated.
3. **Check chokepoints.** Hormuz, Red Sea, Black Sea, Panama, Mississippi: transit
   status, insurance notices, incidents.
4. **Score.** For each new or changed situation assign probability, channel impacts,
   lead time; compute exposure score.
5. **Update files.** Edit `watchlist.md` rows (status, probability, last update); add or
   retire rows. Update probabilities in `scenario-playbook.md`. Append events to
   `data/processed/geopolitical_events.csv` per `data/reference/geopolitical-event-schema.md`.
6. **Trigger handoffs.** For any scenario whose trigger fired, write the pre-committed
   action and invoke `procurement-timing` or notify the market analyst.
7. **Record.** Save `plans/<season>/geo-scan-YYYY-MM-DD.md` with headline risks,
   changes, actions, and sources.

## Output
The dated scan file and a short chat summary: top three risks, what changed, actions
triggered.
