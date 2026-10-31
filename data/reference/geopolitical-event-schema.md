# Geopolitical event log schema

## `data/processed/geopolitical_events.csv`
| Column | Notes |
|---|---|
| date | event or detection date, YYYY-MM-DD |
| watch_id | watchlist row (W-###) or `new` |
| category | 1–12 per monitoring-framework.md |
| region | text |
| event | one-line description |
| channels | semicolon list, e.g. `C1;C3;C7` |
| probability | low / medium / high (6-month) |
| max_impact | 0–3 |
| lead_time | days / weeks / months |
| source | URL or publication |
| action_taken | text or `none` |
| outcome | filled later: realized price or market effect |
