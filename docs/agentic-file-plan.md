# Agentic File Plan — South-Central Kansas Operation

Master list of the files that guide the agents in this project. Each entry names the
file, what it holds, and why it matters for this operation. Grouped by layer:
knowledge, agents, skills, data, models, plans, governance.

Status key: `[ ]` not started · `[~]` drafted (populated but contains items marked verify) · `[x]` populated and reviewed.

## Operation context

- Region: Sedgwick County, Kansas (Wichita) and surrounding farmland.
- Land: approximately 1,000 owned acres across multiple fields.
- Irrigation: undetermined. First task is to establish water-right status per field
  (see `knowledge/water/`). Plans carry dryland and irrigated branches until resolved.
- Crops in scope: hard red winter wheat, grain sorghum, corn, soybeans (full season and
  double-crop after wheat), alfalfa/forage, sunflower, wheat grazing. Cotton and canola
  are excluded.

Regional drivers that shape every file: hard red winter wheat as the anchor crop, hail
and severe-storm exposure, recurring drought tied to ENSO state, the Equus Beds aquifer
and Groundwater Management District 2, Koch Fertilizer nitrogen production in Wichita,
Kansas City wheat futures, Gulf export by rail, China as the dominant sorghum buyer, and
Mexico as the top buyer of Kansas wheat and corn.

---

## 1. Knowledge layer (`knowledge/`)

### 1.1 Operations (`knowledge/operations/`)
- `[~] farm-profile.md` — location, fields, acreage, soils, drainage, water rights,
  storage, buyers in reach, labor.
- `[ ] field-history.md` — per-field rotation, yields, weed and disease pressure,
  fertility trends, tile, water right if any.
- `[~] equipment-inventory.md` — see section 1.6; the full machinery register lives there.
- `[ ] labor-and-custom-work.md` — labor availability, custom rates (harvest, spraying,
  trucking) as capacity fallback.
- `[ ] storage-and-logistics.md` — bins, drying, commercial storage, hauling distances
  to Wichita, Hutchinson, Newton, Wellington elevators; rail access.
- `[ ] seasonal-calendar.md` — wheat planting (fly-free date), sorghum and corn windows,
  double-crop soybean cutoff, harvest windows, workable days.

### 1.2 Agronomy (`knowledge/agronomy/`)
- `[ ] soils-of-south-central-kansas.md` — sandy Arkansas River corridor soils versus
  heavier soils east and north; productivity by series.
- `[ ] soils-and-fertility.md` — soil testing, pH, nutrient removal per crop, build and
  maintain strategies.
- `[ ] rotation-principles.md` — wheat/sorghum/soybean/corn sequences, fallow, nitrogen
  credits, herbicide carryover (atrazine, sulfonylureas).
- `[ ] wheat-stubble-and-no-till-systems.md` — moisture conservation in dryland systems.
- `[ ] planting-agronomy.md` — populations, depth, soil temperature, replant rules.
- `[ ] integrated-pest-management.md` — scouting thresholds, mode-of-action rotation.
- `[ ] herbicide-resistant-weeds-kansas.md` — Palmer amaranth, kochia, waterhemp,
  marestail; resistance status and programs.
- `[ ] weed-management.md` — pre/post programs by crop.
- `[ ] disease-management.md` — wheat rusts, Fusarium head blight, sorghum diseases,
  fungicide timing.
- `[ ] wheat-streak-mosaic-and-volunteer-control.md` — regional disease driven by
  volunteer wheat and wheat curl mite.
- `[ ] insect-management.md` — sugarcane aphid, Hessian fly, army cutworm, greenbug,
  corn earworm; thresholds.
- `[ ] cover-crops-and-soil-health.md` — species that fit a moisture-limited system.

### 1.3 Crops (`knowledge/crops/`)
- `[~] crop-template.md` — template every crop file follows.
- `[~] wheat-hard-red-winter.md` — anchor crop: varieties, protein, fly-free planting,
  freeze and heat risk, graze-out option.
- `[~] wheat-grazing-and-dual-purpose.md` — graze-out economics and cattle linkage.
- `[~] grain-sorghum.md` — drought tolerance, China export dependence, sugarcane aphid.
- `[~] corn-dryland.md`
- `[~] corn-irrigated.md` — only if water rights confirmed.
- `[~] soybeans-full-season.md`
- `[~] soybeans-double-crop.md` — after wheat; separate economics and risk.
- `[~] sunflower.md`
- `[~] alfalfa-and-forage.md` — including forage sorghum and hay markets.
- `[ ] specialty-and-contract-crops.md` — seed wheat, food-grade, identity-preserved.

### 1.4 Water (`knowledge/water/`)
- `[ ] groundwater-and-water-rights.md` — Equus Beds, GMD2, Ogallala to the west,
  water-right lookup, allocation, Kansas Chief Engineer and Kansas Water Office.
- `[ ] irrigation-economics.md` — pumping cost, allocation, yield response, when
  irrigation pays versus dryland.
- `[ ] irrigation-scheduling.md` — crop water use curves, evapotranspiration data from
  Kansas Mesonet.

### 1.5 Inputs (`knowledge/inputs/`)
- `[ ] seed.md` — wheat variety selection, sorghum and corn hybrids, trait packages,
  seed treatments, discounts.
- `[~] fertilizer-nitrogen.md` — Wichita Koch plant, anhydrous and UAN availability,
  Kansas and Oklahoma natural gas, Gulf imports, seasonal pricing.
- `[~] fertilizer-phosphorus-potassium.md` — mine concentration, tariffs, sanctions.
- `[ ] micronutrients-and-lime.md`
- `[ ] herbicides.md` — actives by crop, generic versus branded, China/India intermediates,
  dicamba restrictions.
- `[ ] fungicides.md`, `[ ] insecticides.md`, `[ ] adjuvants-and-application.md`
- `[~] diesel-and-fuel.md` — fuel per operation per acre, Mid-Continent refinery pricing,
  hedging, on-farm storage.
- `[~] propane-and-drying.md` — corn drying only; wheat and sorghum rarely dried.
- `[ ] electricity-and-irrigation-energy.md` — if irrigated.
- `[ ] crop-insurance-kansas.md` — RP/YP products, county yields, wheat and sorghum
  price discovery periods, hail coverage, key dates.
- `[~] input-procurement-strategy.md` — prepay, forward contracts, supplier diversity.

### 1.6 Machinery and equipment (`knowledge/machinery/`)
- `[~] equipment-inventory.md` — register of every machine: combines, headers, tractors,
  planter/drill, sprayer, tillage, grain cart, trucks and trailers, augers, bins, dryer,
  pickups, shop tools. Per item: make/model/year, size or capacity, hours or miles,
  condition, ownership status (owned outright, financed, leased, shared, custom-hired),
  purchase price and date, current market value, insured value.
- `[~] equipment-financing.md` — per financed or leased item: lender, principal
  outstanding, interest rate, monthly or annual payment, payment dates, term remaining,
  balloon, collateral, early-payoff terms. Produces the fixed-payment schedule that feeds
  the cash-flow model regardless of what is planted.
- `[ ] machinery-costs.md` — ownership costs (depreciation, interest or lease, insurance,
  housing, property tax) and operating costs (fuel, lubrication, repairs and maintenance,
  labor) per hour and per acre for each operation, using K-State machinery cost methods
  and the farm's own records. Separates fixed costs that exist regardless of crop from
  variable costs that change with the plan.
- `[ ] maintenance-and-repair-log.md` — service intervals, repair history, known
  failure risks, pre-season readiness checklist; feeds repair-cost assumptions.
- `[ ] field-capacity.md` — acres/hour per implement, workable days, timeliness
  penalties, especially wheat harvest versus double-crop planting.
- `[ ] own-vs-lease-vs-custom.md` — breakeven acres for owning each machine at 1,000
  acres, custom-hire rates for harvest, spraying, planting and trucking, and rules for
  when to custom-hire instead of own.
- `[ ] replacement-and-capital-plan.md` — age and hours triggers, trade cycle, expected
  replacement cost, tax (Section 179 / bonus depreciation) timing.
- `[ ] precision-ag-and-automation.md` — payback assumptions at 1,000 acres.
- `[ ] parts-and-service-supply.md` — dealer access, lead times, tariff exposure.

### 1.7 Weather and climate (`knowledge/weather/`)
- `[ ] climate-normals-south-central-kansas.md` — Wichita and Hutchinson records, GDD,
  frost dates, rainfall distribution.
- `[ ] hail-and-severe-storm-risk.md` — frequency, seasonality, mitigation, insurance.
- `[ ] drought-and-enso-patterns.md` — La Niña drought linkage, seasonal forecast skill.
- `[ ] wheat-freeze-and-heat-stress.md` — spring freeze at jointing, grain-fill heat.
- `[ ] seasonal-forecast-sources.md` — NOAA/CPC, ECMWF, Kansas Mesonet, private services.
- `[ ] weather-to-yield-relationships.md` — critical periods per crop.
- `[ ] long-term-climate-trends.md`

### 1.8 Markets (`knowledge/markets/`)
- `[ ] hard-red-winter-wheat-markets.md` — KC futures, protein premiums, Gulf export
  competition with Russia, Ukraine, Australia; Mexico and Nigeria as top buyers.
- `[ ] sorghum-export-markets.md` — China demand and tariff swings as the key driver.
- `[ ] corn-and-soybean-markets.md` — Kansas basis, ethanol, crush, Mexico export.
- `[ ] kansas-ethanol-and-feed-demand.md` — local ethanol plants, feedlot belt demand.
- `[~] marketing-channels-and-coops.md` — buyer types, how co-ops work, contract types,
  pricing and discount differences, storage charges, counterparty law, bid worksheet.
- `[~] local-elevators-and-basis.md` — catalog of buyers within ~75 miles, basis history.
- `[ ] futures-and-hedging.md` — contracts, options, HTA, basis contracts.
- `[ ] hay-and-forage-markets.md`
- `[ ] marketing-plan-framework.md` — incremental sales targets, triggers.

### 1.9 Geopolitics and policy (`knowledge/geopolitics/`)
- `[~] monitoring-framework.md` — exposure channels, event categories, watch regions,
  scoring, and the signal-to-action process.
- `[~] watchlist.md` — live table of situations with probability, channels, impact,
  indicators and responses.
- `[ ] geopolitical-risk-register.md` — living register mapping events to this farm's
  input, export, currency and freight exposure.
- `[~] case-studies/2026-iran-war-lessons-learned.md` — timeline, transmission
  channels, who was protected, lessons, future indicators. Template for future shocks.
- `[ ] case-studies/<event>.md` — one per major shock (2022 Russia–Ukraine, 2018 China
  tariffs, 2008 fertilizer spike are candidates for back-fill).
- `[ ] wheat-geopolitics.md` — Black Sea exports, Russian quotas and taxes, global crops.
- `[ ] china-trade-exposure.md` — sorghum and soybean demand, retaliatory tariffs.
- `[ ] mexico-trade-relations.md` — USMCA, top buyer of Kansas wheat and corn.
- `[~] fertilizer-geopolitics.md` — potash and phosphate concentration, urea, gas shocks.
- `[~] energy-geopolitics.md` — OPEC+, sanctions, chokepoints, diesel and gas linkage.
- `[ ] agrochemical-supply-chain.md` — China/India concentration in actives.
- `[ ] currency-and-macro.md` — USD, interest rates, competitor currencies.
- `[ ] conflict-and-chokepoints.md` — Black Sea, Red Sea, Hormuz, Panama, Taiwan Strait.
- `[ ] domestic-farm-policy.md` — Farm Bill, ARC/PLC, disaster aid, conservation.
- `[~] scenario-playbook.md` — China sorghum ban, Black Sea wheat surge, Hormuz closure,
  Mexico tariff dispute, fertilizer sanctions; triggers and responses.

### 1.10 Finance (`knowledge/finance/`)
- `[ ] enterprise-budget-template.md` — per-crop budget using K-State Farm Management
  Guide structure.
- `[ ] cash-flow-and-credit.md`, `[ ] tax-planning.md`, `[ ] capital-investment.md`
- `[ ] land-values-and-opportunity-cost.md` — owned land carrying cost, Kansas land
  values, cash-rent benchmarks for expansion decisions.
- `[ ] risk-management-framework.md` — how insurance, hedging, diversification and cash
  reserves combine; risk tolerance statement.

### 1.11 Land (`knowledge/land/`)
- `[ ] soil-map-and-productivity.md`, `[ ] drainage-and-terraces.md`
- `[ ] expansion-and-acquisition.md` — land market, rental opportunities, criteria.

### 1.12 Regulatory and compliance (`knowledge/regulatory/`)
- `[ ] kansas-pesticide-licensing.md` — KDA applicator rules, restricted use, dicamba,
  recordkeeping, drift.
- `[ ] kansas-water-law-compliance.md` — water right reporting, meters, penalties.
- `[ ] nrcs-and-conservation-programs.md` — CRP, EQIP, HEL and wetland compliance.
- `[ ] noxious-weed-law.md` — Kansas statutory noxious weed list.
- `[ ] labor-and-safety.md`, `[ ] grain-grading-and-contracts.md`
- `[ ] traceability-and-certification.md`

### 1.13 Sustainability and carbon (`knowledge/sustainability/`)
- `[ ] carbon-markets.md`, `[ ] regenerative-practices-economics.md`
- `[ ] low-carbon-intensity-premiums.md` — 45Z and low-CI grain premiums at ethanol plants.

### 1.14 Risk (`knowledge/risk/`)
- `[ ] risk-register.md` — all risks with likelihood, impact, mitigation, owner.
- `[ ] decision-rules.md` — pre-committed rules: switch crops, prepay, hedge, replant,
  graze out, abandon, double-crop go/no-go.

---

## 2. Agent definitions (`.claude/agents/`)
- `[ ] orchestrator-planner.md` — runs the seasonal loop, assembles the plan.
- `[ ] agronomist.md`, `[ ] weather-forecaster.md`, `[ ] input-cost-analyst.md`
- `[~] geopolitical-analyst.md`, `[ ] market-analyst.md`
- `[ ] water-rights-and-irrigation.md` — allocation as a hard planning constraint.
- `[ ] machinery-and-logistics.md`, `[ ] finance-controller.md`
- `[ ] insurance-and-risk.md`, `[ ] compliance-officer.md`, `[ ] sustainability-analyst.md`
- `[ ] data-ingestion.md` — fetches, validates, files external data.
- `[ ] red-team-reviewer.md` — challenges hidden assumptions and correlated risks.

## 3. Skills / workflows (`.claude/skills/`)
- `[ ] build-seasonal-plan/`, `[ ] forecast-input-costs/`, `[ ] weather-scenario-build/`
- `[ ] market-outlook-refresh/`, `[~] geopolitical-scan/` (weekly)
- `[ ] enterprise-budget/`, `[ ] field-level-recommendation/`
- `[ ] in-season-replan/`, `[ ] hail-and-storm-response/` — damage assessment, claims,
  replant or double-crop decision.
- `[ ] double-crop-decision/` — go/no-go after wheat harvest based on moisture and date.
- `[~] procurement-timing/`, `[ ] hedging-decision/`, `[ ] insurance-selection/`
- `[ ] post-harvest-review/`, `[ ] knowledge-file-update/`

## 4. Data layer (`data/`)
- `[~] reference/data-sources.md` — USDA NASS/AMS/WASDE/ERS, RMA, NOAA/CPC, Kansas
  Mesonet, K-State Extension, Kansas Farm Management Association, KDA, Kansas Water
  Office / WIMAS water rights, CME/KC futures, EIA, FAO/AMIS, IGC, fertilizer indices.
- `[~] reference/input-price-schema.md` — schema for `input_prices.csv` and `input_purchases.csv`.
- `[ ] reference/units-and-conversions.md`
- `scripts/fetch_eia_prices.py` — pulls EIA diesel, WTI and Henry Hub weekly series.
- `scripts/fetch_gdelt_events.py` — news volume and headlines per watch topic (GDELT, no key).
- `[~] reference/geopolitical-event-schema.md` and `processed/geopolitical_events.csv`.
- `[~] reference/free-apis.md` — survey of free data feeds and where free data is weak.
- `raw/` immutable dated downloads · `processed/` cleaned tables with schema.

## 5. Models (`models/`)
- `[ ] yield-response-model.md` — by crop, dryland and irrigated branches.
- `[~] input-price-forecast-model.md` — overview; sub-models `[~] fertilizer-price-model.md`
  and `[~] fuel-price-model.md`.
- `[ ] commodity-price-scenario-model.md`
- `[ ] weather-scenario-model.md` — keyed to ENSO state and Mesonet history.
- `[ ] crop-mix-optimizer.md` — LP/MIP over fields: rotation, water allocation,
  wheat/double-crop sequencing, graze-out, machinery and labor capacity, cash.
- `[ ] monte-carlo-risk-model.md`, `[ ] cash-flow-model.md`

## 6. Plans (`plans/`)
- `[ ] plan-template.md`, `[ ] YYYY-season-plan.md`, `[ ] YYYY-post-harvest-review.md`

## 7. Governance (`docs/`)
- `[x] agentic-file-plan.md`, `[~] knowledge-file-template.md`
- `[ ] glossary.md`, `[ ] decision-records/`

---

## Build order
1. Farm profile, field list, water-right lookup per field, and the equipment inventory
   with financing schedule (fixed costs exist before any crop is chosen).
2. Crop template, then wheat, sorghum, soybeans (both), corn (dryland first).
3. Enterprise budget template and input files (nitrogen, herbicides, diesel, seed,
   insurance).
4. Geopolitical risk register, wheat and China trade files, fertilizer and energy files.
5. Weather files (hail, drought/ENSO, freeze) and the data-source catalog.
6. Agents and the seasonal-plan skill.
7. Models: budgets first, then optimizer and Monte Carlo.
8. First seasonal plan, red-team review, iterate.
