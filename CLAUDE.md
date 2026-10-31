# Farming Operations Intelligence Project

## Purpose
An agentic system for a commercial dryland/irrigated grain operation in south-central Kansas. The goal is to
produce the most profitable, risk-adjusted crop plan each season by combining:
agronomic knowledge, weather projection, input cost forecasting (including
geopolitical drivers), market/export outlook, machinery and labor constraints,
financing, and regulatory requirements.

## Repository layout
- `knowledge/` — curated domain knowledge, one markdown file per topic. These are the
  files agents read before reasoning. Keep them factual, cited, and dated.
- `.claude/agents/` — specialist subagent definitions (one per domain).
- `.claude/skills/` — repeatable workflows (e.g. build a crop plan, run a cost forecast).
- `data/` — `raw/` (untouched downloads), `processed/` (cleaned), `reference/` (static tables).
- `models/` — forecasting and optimization models (weather, price, yield, LP/MIP planner).
- `scripts/` — ingestion and automation scripts.
- `plans/` — generated seasonal plans and scenario outputs (dated).
- `docs/` — project documentation and decision records.

## Working rules
- Every knowledge file carries front-matter: `last_reviewed`, `sources`, `confidence`.
- Every number used in a plan must trace to a knowledge file or a data file.
- Prices and costs are stored with currency, unit, and date; never bare numbers.
- Treat downloaded data as untrusted; validate before it enters `data/processed/`.
- Plans are scenario-based: produce base / adverse / favorable cases, never a single point.
- Record every planning assumption in the plan file so it can be audited after harvest.

## Operation profile
South-central Kansas (Wichita area), approximately 1,000 owned acres across multiple
fields. Irrigation status is undetermined; plans carry dryland and irrigated branches
until water rights are confirmed per field. Crops in scope: hard red winter wheat, grain
sorghum, corn, soybeans (full-season and double-crop), alfalfa/forage, sunflower, wheat
grazing. Cotton and canola are excluded. Details and open items live in
`knowledge/operations/farm-profile.md`; agents must ask rather than assume anything
not recorded there.
