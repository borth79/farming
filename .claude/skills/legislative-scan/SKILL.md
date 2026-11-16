---
name: legislative-scan
description: Monthly (weekly in session) scan of federal and Kansas bills, rules, program notices and court actions affecting the farm; score effect and probability; update the policy watch list, calendar deadlines and plan assumptions.
---

# Legislative scan

Owner: policy-analyst agent. Monthly year-round; weekly January–May (Kansas session) and
whenever Congress is moving a farm bill, tax or trade package.

## Steps
1. **Federal rules.** `python3 scripts/fetch_federal_register.py --days 31` pulls recent
   Federal Register documents from USDA agencies, EPA, Treasury and USTR matching farm
   keywords into `data/raw/federal_register/<date>/` and prints a summary.
2. **Federal bills.** Check farm bill, appropriations, tax and trade bills on Congress.gov
   (API key if set, else web search); note committee action and floor schedule.
3. **Kansas bills.** Query the Kansas Legislature API (or site) by subjects: agriculture,
   water, taxation, alcoholic beverages, pesticides, property; during session read the
   weekly summaries from Kansas Farm Bureau, Kansas Grain and Feed, Kansas Livestock,
   Renew Kansas, Kansas Wheat.
4. **Agencies and courts.** USDA FSA/RMA/NRCS program notices and deadlines; EPA pesticide
   decisions and ESA strategies; KDA notices; court actions (dicamba, WOTUS, right to
   repair).
5. **Score.** For each new or changed item: status, key date, probability of enactment,
   effect direction and estimate with units, affected crops or verticals, action.
6. **Update.** `data/processed/policy_watch.csv`; the status snapshot table in
   `knowledge/regulatory/policy-and-legislation-watch.md` with `last_reviewed`.
7. **Hand off.** Deadlines to the compliance officer calendar; dollar effects above the
   threshold to the finance controller and orchestrator as plan assumptions; trade items
   to the geopolitical watchlist; licensing changes to vertical owners.
8. **Write.** `plans/<season>/policy-scan-YYYY-MM-DD.md`: changed items table, top three
   plan effects, deadlines in the next 60 days, sources.

## Output
The scan file, updated CSV and knowledge snapshot, and a short summary.
