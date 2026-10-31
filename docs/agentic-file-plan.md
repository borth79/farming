# Agentic File Plan

This is the master list of files that will guide the agents in this project. Each entry
names the file, what it holds, and which agents depend on it. Files are grouped by the
layer they belong to: knowledge, agents, skills, data, models, and plans.

Status key: `[ ]` not started · `[~]` stub exists · `[x]` populated and reviewed.

---

## 1. Knowledge layer (`knowledge/`)

Curated, cited, dated domain knowledge. These are what the agents read first.

### 1.1 Operations (`knowledge/operations/`)
- `[~] farm-profile.md` — location, fields, acreage, soil series, drainage, irrigation,
  storage capacity, elevators/buyers within reach, labor pool. Everything else keys off this.
- `[ ] field-history.md` — per-field crop rotation history, yields, problem weeds,
  disease history, tile, pH/fertility trends.
- `[ ] equipment-inventory.md` — tractors, planters, sprayers, combines, trucks, grain
  handling; widths, capacities, hours, ownership vs lease, replacement schedule.
- `[ ] labor-and-custom-work.md` — seasonal labor availability, wage rates, custom
  operator rates (planting, spraying, harvest, trucking) as a fallback for capacity.
- `[ ] storage-and-logistics.md` — on-farm bins, drying capacity, commercial storage,
  trucking distances, rail/barge/port access, basis implications.
- `[ ] seasonal-calendar.md` — planting windows, spray windows, harvest windows by
  crop for this latitude, with workable-day assumptions.

### 1.2 Agronomy (`knowledge/agronomy/`)
- `[ ] soils-and-fertility.md` — soil testing, CEC, pH management, nutrient removal
  rates per crop, build/maintain/drawdown strategies.
- `[ ] rotation-principles.md` — rotation effects on yield, pests, nitrogen credits,
  herbicide carryover constraints.
- `[ ] planting-agronomy.md` — populations, depth, row spacing, soil temperature
  thresholds, replant decision rules.
- `[ ] integrated-pest-management.md` — scouting thresholds, resistance management,
  mode-of-action rotation.
- `[ ] weed-management.md` — key weeds by region, resistance status, pre/post programs.
- `[ ] disease-management.md` — key diseases, fungicide timing, weather-driven risk models.
- `[ ] insect-management.md` — key insects, economic thresholds, trait considerations.
- `[ ] irrigation-and-water.md` — crop water use curves, scheduling, water rights.
- `[ ] cover-crops-and-soil-health.md` — species, costs, benefits, termination.

### 1.3 Crops (`knowledge/crops/`) — one file per candidate crop
Each crop file follows the same template: agronomic requirements, yield potential by
soil class, input program, cost per acre, marketing channels, storage/drying needs,
rotation fit, risk profile, and relevant trait/seed options.
- `[ ] corn.md`
- `[ ] soybeans.md`
- `[ ] wheat-winter.md`
- `[ ] wheat-spring.md`
- `[ ] canola.md`
- `[ ] sorghum.md`
- `[ ] barley.md`
- `[ ] oats.md`
- `[ ] sunflower.md`
- `[ ] cotton.md`
- `[ ] alfalfa-and-hay.md`
- `[ ] pulses.md` (peas, lentils, chickpeas, dry beans)
- `[ ] specialty-and-contract-crops.md` — seed production, food-grade, organic premiums,
  identity-preserved contracts.
- `[ ] crop-template.md` — the template every crop file follows.

### 1.4 Inputs (`knowledge/inputs/`)
- `[ ] seed.md` — seed costs by trait package, discounts, early-pay programs, treatments.
- `[ ] fertilizer-nitrogen.md` — anhydrous, urea, UAN; natural-gas linkage; import
  dependence; seasonal price patterns; application timing/loss.
- `[ ] fertilizer-phosphorus-potassium.md` — DAP/MAP, potash; mine concentration
  (Morocco, Russia, Belarus, Canada); tariffs and sanctions exposure.
- `[ ] micronutrients-and-lime.md`
- `[ ] herbicides.md` — active ingredients, generic vs branded pricing, supply chain
  (China/India intermediates), label constraints, resistance.
- `[ ] fungicides.md`
- `[ ] insecticides.md`
- `[ ] adjuvants-and-application.md`
- `[ ] diesel-and-fuel.md` — fuel use per operation per acre, price linkage to crude
  and refinery margins, hedging options, storage.
- `[ ] propane-and-drying.md` — drying cost per point of moisture, propane/natural gas
  price drivers.
- `[ ] electricity-and-irrigation-energy.md`
- `[ ] crop-insurance.md` — RP/YP/ARP products, coverage levels, premium costs,
  SCO/ECO, key dates, projected/harvest price mechanics.
- `[ ] input-procurement-strategy.md` — prepay, forward contracting, volume discounts,
  supplier diversification, timing rules.

### 1.5 Machinery (`knowledge/machinery/`)
- `[ ] machinery-costs.md` — ownership (depreciation, interest, insurance, housing) and
  operating (fuel, labor, repairs) cost per hour and per acre by operation.
- `[ ] field-capacity.md` — acres/hour by implement, workable days, timeliness penalties.
- `[ ] precision-ag-and-automation.md` — autosteer, VRT, section control, autonomy,
  data platforms; payback assumptions.
- `[ ] parts-and-service-supply.md` — lead times, tariff exposure on steel/components.

### 1.6 Weather and climate (`knowledge/weather/`)
- `[ ] climate-normals.md` — GDD, frost dates, precipitation distribution, drought
  frequency for the farm's location.
- `[ ] seasonal-forecast-sources.md` — ENSO state, NOAA/CPC outlooks, ECMWF seasonal,
  private services; skill and limitations of each.
- `[ ] weather-to-yield-relationships.md` — critical periods (pollination, grain fill),
  heat/drought stress response curves per crop.
- `[ ] extreme-event-risk.md` — hail, flooding, derecho, early frost; frequencies and
  mitigation.
- `[ ] long-term-climate-trends.md` — shifting zones, changing growing season, water.

### 1.7 Markets (`knowledge/markets/`)
- `[ ] commodity-price-fundamentals.md` — supply/demand balance sheets, stocks-to-use,
  WASDE reading guide.
- `[ ] basis-and-local-markets.md` — local basis history, buyer list, delivery terms.
- `[ ] futures-and-hedging.md` — contracts, margin, options strategies, HTA, basis
  contracts, when to use each.
- `[ ] export-markets.md` — top importers per crop, trade flows, port logistics,
  freight (Panama Canal, Mississippi, Black Sea, Brazil ports).
- `[ ] competitor-producers.md` — Brazil, Argentina, Ukraine, Russia, Australia, EU;
  planting progress, currency effects, their cost structures.
- `[ ] biofuels-and-demand-policy.md` — RFS, SAF, 45Z, ethanol/crush margins, renewable
  diesel soybean-oil demand.
- `[ ] livestock-and-feed-demand.md` — herd sizes, feed ratios, domestic demand drivers.
- `[ ] marketing-plan-framework.md` — incremental sales targets, decision triggers.

### 1.8 Geopolitics and policy (`knowledge/geopolitics/`)
- `[ ] geopolitical-risk-register.md` — living register of events and their exposure
  pathways to this farm (inputs, exports, currency, freight).
- `[ ] fertilizer-geopolitics.md` — Russia/Belarus potash, Chinese phosphate export
  controls, Middle East urea, natural gas shocks, sanctions.
- `[ ] energy-geopolitics.md` — OPEC+, sanctions, shipping chokepoints, refinery
  outages; mapping to diesel and propane.
- `[ ] trade-policy-and-tariffs.md` — US-China, retaliatory tariffs, USMCA, EU
  deforestation rules, phytosanitary barriers.
- `[ ] agrochemical-supply-chain.md` — China/India concentration in actives and
  intermediates, export licensing, shipping disruption.
- `[ ] currency-and-macro.md` — USD strength, BRL/ARS/UAH, interest rates, inflation;
  effects on competitiveness and input costs.
- `[ ] conflict-and-chokepoints.md` — Black Sea, Red Sea/Suez, Strait of Hormuz, Taiwan
  Strait, Panama; scenario probabilities and impact matrices.
- `[ ] domestic-farm-policy.md` — Farm Bill, ARC/PLC, disaster programs, conservation
  payments, ad-hoc aid patterns.
- `[ ] scenario-playbook.md` — pre-written scenarios (e.g. potash sanction escalation,
  Chinese soybean tariff, Gulf closure) with trigger indicators and response actions.

### 1.9 Finance (`knowledge/finance/`)
- `[ ] enterprise-budget-template.md` — per-crop revenue, direct costs, overhead,
  breakeven; the planner's cost model.
- `[ ] cash-flow-and-credit.md` — operating line, interest rates, payment timing,
  covenant constraints.
- `[ ] land-costs.md` — cash rent, flex leases, crop share, ownership costs, rent
  negotiation benchmarks.
- `[ ] tax-planning.md` — depreciation, prepaid inputs, deferred sales, entity structure.
- `[ ] capital-investment.md` — equipment, bins, tile, irrigation; NPV/payback rules.
- `[ ] risk-management-framework.md` — how insurance, hedging, diversification, and
  cash reserves combine; risk tolerance statement.

### 1.10 Land (`knowledge/land/`)
- `[ ] soil-map-and-productivity.md` — soil survey, productivity indices per field.
- `[ ] drainage-and-tile.md`
- `[ ] lease-portfolio.md` — leases, expiry, terms, landlord relationships.
- `[ ] expansion-and-acquisition.md` — land market, valuation, criteria.

### 1.11 Regulatory and compliance (`knowledge/regulatory/`)
- `[ ] pesticide-regulations.md` — licensing, restricted-use products, recordkeeping,
  drift rules, buffer zones, label-is-law.
- `[ ] nutrient-and-water-regulations.md` — nutrient management plans, watershed rules.
- `[ ] environmental-and-conservation.md` — wetlands, highly erodible land, CRP, EQIP.
- `[ ] labor-and-safety.md` — H-2A, OSHA, worker protection standard.
- `[ ] traceability-and-certification.md` — organic, non-GMO, sustainability
  certifications, Scope 3 reporting from buyers.
- `[ ] grain-grading-and-contracts.md` — grades, discounts, contract law basics.

### 1.12 Sustainability and carbon (`knowledge/sustainability/`)
- `[ ] carbon-markets.md` — programs, payments per practice, verification costs.
- `[ ] regenerative-practices-economics.md` — no-till, cover crops, reduced inputs;
  realistic payback.
- `[ ] low-carbon-intensity-premiums.md` — 45Z/CI scoring, low-CI corn premiums.

### 1.13 Risk (`knowledge/risk/`)
- `[ ] risk-register.md` — all identified risks with likelihood, impact, mitigation,
  owner. Cross-references geopolitics, weather, markets, operations.
- `[ ] decision-rules.md` — pre-committed rules: when to switch crops, when to
  prepay, when to hedge, when to replant, when to abandon.

---

## 2. Agent definitions (`.claude/agents/`)

Specialist subagents. Each reads its knowledge files, has a narrow mandate, and
returns structured output the orchestrator can combine.

- `[ ] orchestrator-planner.md` — runs the seasonal planning loop; calls specialists;
  builds the final crop plan with scenarios.
- `[ ] agronomist.md` — crop suitability, rotation, input programs, yield expectations.
- `[ ] weather-forecaster.md` — pulls forecasts, builds seasonal weather scenarios,
  maps them to yield risk.
- `[ ] input-cost-analyst.md` — forecasts seed, fertilizer, chemical, fuel costs;
  flags procurement timing.
- `[ ] geopolitical-analyst.md` — monitors the risk register, assigns probabilities,
  translates events into input/export price shocks.
- `[ ] market-analyst.md` — price outlook, basis, export demand, hedging recommendations.
- `[ ] machinery-and-logistics.md` — capacity checks, timeliness, custom-hire needs,
  fuel use.
- `[ ] finance-controller.md` — enterprise budgets, cash flow, breakeven, lender view.
- `[ ] insurance-and-risk.md` — insurance product selection, coverage, program dates.
- `[ ] compliance-officer.md` — checks plans against regulations and label constraints.
- `[ ] sustainability-analyst.md` — carbon/CI revenue opportunities and costs.
- `[ ] data-ingestion.md` — fetches, validates, and files external data into `data/`.
- `[ ] red-team-reviewer.md` — adversarially challenges each plan: hidden assumptions,
  correlated risks, over-optimism.

---

## 3. Skills / workflows (`.claude/skills/`)

Repeatable, step-by-step procedures the agents follow.

- `[ ] build-seasonal-plan/` — end-to-end: profile → scenarios → budgets → optimization
  → plan file in `plans/`.
- `[ ] forecast-input-costs/` — refresh input price forecasts with geopolitical overlays.
- `[ ] weather-scenario-build/` — produce base/adverse/favorable weather scenarios.
- `[ ] market-outlook-refresh/` — update price, basis, export outlook after WASDE etc.
- `[ ] geopolitical-scan/` — weekly scan; update risk register and scenario probabilities.
- `[ ] enterprise-budget/` — produce or refresh a per-crop budget.
- `[ ] field-level-recommendation/` — assign crops and programs field by field.
- `[ ] in-season-replan/` — re-optimize after planting delays, weather shocks, price moves.
- `[ ] procurement-timing/` — decide when and how much input to lock in.
- `[ ] hedging-decision/` — propose marketing actions against targets and risk limits.
- `[ ] insurance-selection/` — compare products and coverage levels for the plan.
- `[ ] post-harvest-review/` — compare plan vs actual; update knowledge files.
- `[ ] knowledge-file-update/` — standard procedure for revising a knowledge file with
  sources and review date.

---

## 4. Data layer (`data/`)

- `[ ] data/reference/units-and-conversions.md` — bushels, tonnes, lbs N, etc.
- `[ ] data/reference/data-sources.md` — catalog of feeds: USDA NASS/AMS/WASDE/ERS,
  NOAA/CPC, DTN, CME, EIA, FAO/AMIS, IGC, World Bank commodity, Baltic freight, fertilizer
  price indices, state extension budgets; cadence and access method for each.
- `[ ] data/raw/` — immutable downloads, dated subfolders.
- `[ ] data/processed/` — cleaned tables with a schema file beside each.

---

## 5. Models (`models/`)

- `[ ] yield-response-model.md` — yield as function of weather, soil, inputs, planting
  date; by crop.
- `[ ] input-price-forecast-model.md` — fertilizer/fuel/chem price models with
  macro and geopolitical shock variables.
- `[ ] commodity-price-scenario-model.md` — price distributions per crop for the
  marketing year.
- `[ ] weather-scenario-model.md` — seasonal scenario generation and probabilities.
- `[ ] crop-mix-optimizer.md` — LP/MIP: maximize expected risk-adjusted profit subject
  to rotation, machinery capacity, labor, cash, storage, agronomic constraints.
- `[ ] monte-carlo-risk-model.md` — simulate combined weather/price/cost uncertainty;
  report downside metrics.
- `[ ] cash-flow-model.md` — monthly cash flow under each scenario.

---

## 6. Plans and outputs (`plans/`)

- `[ ] plan-template.md` — fixed structure: assumptions, scenarios, crop mix by field,
  input program, procurement plan, marketing plan, insurance, cash flow, risks, triggers.
- `[ ] YYYY-season-plan.md` — one per season, generated by the orchestrator.
- `[ ] YYYY-post-harvest-review.md` — actuals vs plan, lessons, knowledge updates.

---

## 7. Governance (`docs/`)

- `[x] agentic-file-plan.md` — this file.
- `[ ] decision-records/` — ADR-style records for major planning and system decisions.
- `[ ] glossary.md` — terms and acronyms used across files.
- `[ ] knowledge-file-template.md` — front-matter and section standard.

---

## Suggested build order

1. `operations/farm-profile.md` and `field-history.md` — nothing else is meaningful
   without them.
2. Crop template and the 3–5 crops actually under consideration.
3. Enterprise budget template and the input files (fertilizer, chemicals, diesel, seed).
4. Geopolitical risk register and fertilizer/energy geopolitics files.
5. Weather and market knowledge files, then data-sources catalog.
6. Agents and the `build-seasonal-plan` skill.
7. Models, starting with enterprise budgets, then the crop-mix optimizer and Monte Carlo.
8. First full seasonal plan, red-team review, iterate.
