# Policy watch schema

## `data/processed/policy_watch.csv`
| Column | Notes |
|---|---|
| item_id | P-### |
| level | federal / kansas / local |
| type | statute / bill / rule / proposed_rule / program_notice / court_order / trade_action |
| title | |
| identifier | bill number, docket, FR citation |
| status | introduced / in_committee / passed_chamber / enacted / proposed / final / effective / expired / vetoed |
| key_date | next deadline or effective date |
| area | commodity_programs / insurance / biofuels / trade / pesticides / water / tax / conservation / food_alcohol_labor / trust_tax / repair / other |
| probability_enactment | 0–1 for pending items |
| effect_direction | positive / negative / mixed |
| effect_estimate | text with units, e.g. "+$12/acre wheat PLC" or "−1 spray window" |
| affected | crops, verticals or files |
| action | comment / plan_assumption / calendar / none |
| source | URL or citation with date |
| last_checked | YYYY-MM-DD |
| notes | |
