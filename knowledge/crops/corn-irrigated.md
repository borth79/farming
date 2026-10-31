---
title: Corn (maize) — irrigated (center pivot)
domain: crops
last_reviewed: 2026-10-31
review_cadence: seasonal
confidence: low-medium (water-use agronomy medium; pumping costs, allocations, yields and budget low — many items flagged "verify"; irrigation status of this farm is itself undetermined)
sources:
  - All sources listed in corn-dryland.md (shared agronomy, markets, insurance)
  - K-State MF3066 "Efficient Crop Water Use in Kansas" — net irrigation requirement 5 in (east) to ~16 in (west); ET example 0.20 in/day
  - K-State C560 "Corn Production Handbook" — seasonal water use 22–30 in; peak use before/at early reproductive stages
  - K-State Sunflower District / Northwest Research-Extension Center "Limited Irrigation" page — 0.35 in/day typical, 0.50 in/day peaks
  - K-State eUpdate "Final Irrigation of the Growing Season — Timing is Everything" (Issue 1116, 2026-08-13; earlier version 604-1) — remaining water use by stage, 45% depletion limit
  - K-State L908 "Considerations for Nozzle Package Selection for Center Pivots" (90% of Kansas irrigated acres under pivots)
  - K-State MF2360 "Comparing Irrigation Energy Costs"; L885 "Evaluating Pumping Plant Efficiency Using On-Farm Fuel Bills" — energy conversion factors (12.5 whp-h/gal diesel, 61.7 whp-h/MCF gas, 0.885 whp-h/kWh)
  - Colorado State / Mountain Scholar irrigation energy report — ~37 kWh per acre-inch at 150 ft lift + 60 psi
  - K-State 2018 KFMG NW Kansas irrigated corn budget (O'Brien & Vandeveer, 2018-01-29) — irrigation energy $35.30/$46.54/$54.56 per acre at 11.0/14.5/17.0 in
  - K-State 2016 SW Kansas irrigated corn (center-pivot) budget — 18 ac-in applied, $2.85/ac-in fuel (dated)
  - K-State eUpdate seeding-rate table (Issue 792, 2020-03-27); K-State eUpdate 2008-02-15 irrigated populations by maturity; MF3208 Kansas Corn Management 2025 (≥30,000 plants/ac for >200 bu)
  - K-State MF2586 (2024 revision) — 300 lb N/ac cap irrigated
  - GMD2 (Equus Beds GMD) Annual Reports 2023 and 2025 (Kansas Legislature testimony); KGS Open-File Report 2017-3 (Qstable 180,308 ac-ft/yr); KDA-DWR GMD No. 2 page; Hendricks (K-State) "Irrigation Groundwater Rights" 2023-11-16; Cameron/Harp (K-State) irrigation update
  - Virginia Cooperative Extension "Irrigation Management for Corn" — 0.35 in/day at 85% efficiency = 7.8 gpm/ac (arithmetic cross-check)
  - Southern Ag Today 2026-07-20 "Fuel Pricing Impacts Irrigation Pumping Costs" (diesel sensitivity, not Kansas-specific)
  - Kansas Corn Commission 2025 yield contest release (irrigated 349.34 bu/ac state record, Haskell County; 277.30 bu/ac Barton County irrigated)
used_by_agents:
  - agronomist
  - input-cost-analyst
  - market-analyst
  - orchestrator-planner
  - water-rights (if defined)
---

# Corn (maize) — irrigated (center pivot)

> Read `corn-dryland.md` first. This file records only what changes when the field is
> under a center pivot: fit, population and hybrid choices, nitrogen, water use and
> scheduling, well/allocation constraints, pumping cost, yields, the irrigated cost
> table and breakeven, and irrigated-specific decision rules. Weeds, insects, diseases,
> rotation, marketing and insurance mechanics are shared and are not repeated except
> where irrigation changes the risk.
>
> **Status:** this farm's irrigation status is undetermined (farm-profile.md). Nothing
> here may be used in a plan until the water right (file number, authorized quantity in
> acre-feet, authorized acres, well capacity in gpm, source aquifer, GMD2 status) is
> recorded per field in `knowledge/water/` and farm-profile.md.

## Fit for this operation (irrigated differences)

- Irrigated corn is the highest-gross-revenue grain crop available to this farm and
  the one for which irrigation is most often justified in south central Kansas,
  because corn's water-use curve peaks exactly when Wichita rainfall is least reliable
  (July). It converts the dryland "defining risk" (heat/drought at silking) into a
  pumping-cost and well-capacity question.
- Fit depends on **well capacity relative to pivot acres** (see "Center-pivot capacity
  needs"): a full-capacity system (≥7–8 gpm/ac) supports full-yield corn; a
  low-capacity well (4–5 gpm/ac) supports deficit-irrigated corn with lower
  population, or favors sorghum/soybeans under the pivot.
- Equus Beds aquifer (GMD2) fields usually have shallower lifts and better water
  quality than western Kansas, so pumping costs per acre-inch are lower; the binding
  constraint is the **authorized annual quantity** and GMD2's management rules, not
  energy.
- Corn-on-corn is more defensible irrigated than dryland (water is not the limiter),
  but rootworm, gray leaf spot, tar spot and N cost rise; a corn–soybean rotation under
  the pivot is the planning default.
- Disqualifiers: wells under 400 gpm on a 120+ acre pivot without a deficit plan;
  water rights with remaining annual quantity <10 in/ac; fields with saline/sodic
  water (verify water test); fields where GMD2 reductions or a LEMA are pending.

## Agronomic requirements (irrigated differences)

| Parameter | Irrigated recommendation | Source / status |
|---|---|---|
| Final plant population | 28,000–34,000 plants/ac. K-State: environments yielding >200 bu/ac generally need ≥30,000 plants/ac (MF3208 2025); older K-State table (2008) gave 30,000–36,000 for shorter-season hybrids under full irrigation. Use 28–30k for limited-capacity pivots, 32–34k for full capacity on deep soils. | MF3208; eUpdate 2008-02-15 (dated) |
| Seeding rate | 30,000–36,000 seeds/ac (plan ~5–8% over target stand) | derived |
| Row spacing | 30 in standard; 20-in rows and twin rows show small, inconsistent gains under full irrigation in the central Plains — only if the planter/head already fit | general; **verify** |
| Hybrid maturity | 110–115 day RM for full-season yield when planted April 15–May 5; 105–110 day if planted after May 15 or if wheat follows. Prioritize high-yield, high-input-responsive hybrids with strong stalk and GLS/southern rust scores; drought scoring is secondary unless well capacity is limiting. | C560 |
| Traits | Above-ground Bt (Vip3A-containing) recommended — irrigated green canopies attract more earworm/WBC; below-ground RW Bt only in corn-on-corn; glyphosate + glufosinate (or Enlist) for Palmer POST options. | MF810 |
| Planting window | Same as dryland (April 20–May 20 per L818; practical April 10–May 5). Irrigated corn tolerates slightly earlier planting because stand can be rescued, but cold-soil rule (≥50 °F) still applies. | L818 |
| Seasonal crop water use (ET) | 22–30 in total (C560); full-season 112-day hybrid in Wichita heat typically 26–28 in (**verify** Mesonet ET records) | C560 |
| Net irrigation requirement | South central Kansas sits between K-State's 5 in (east) and ~16 in (west) regional averages: plan **8–12 in net** in an average year, 14–18 in in a drought year, 4–6 in in a wet year | MF3066; interpolation **verify** with KanSched runs |
| Gross application | Net ÷ application efficiency (0.85–0.90 for low-pressure drops/LEPA-type packages; 0.75–0.80 for impact sprinklers): **10–14 in gross** average year | L908; general |
| Peak daily use | 0.30–0.35 in/day typical late June–July; 0.50 in/day or more on 100 °F wind days | K-State NWREC |
| Depletion limit | Keep root-zone available water ≥55% (allow ≤45% depletion) through R3; can let it draw down after R4 | K-State final-irrigation eUpdate |

### Crop water use by growth stage (planning table)
Values are typical for a late-April planted, 110–112 day hybrid in south central Kansas;
daily rates are ranges from K-State publications and standard corn crop coefficients,
not Sedgwick measurements — **verify** against Kansas Mesonet reference ET × Kc each
season.

| Stage (approx. dates) | Approx. daily ET (in/day) | Approx. cumulative ET (in) | Irrigation note |
|---|---|---|---|
| Emergence–V6 (late Apr–late May) | 0.05–0.12 | 2–3 | Rarely irrigate; rainfall usually sufficient; pre-season fill of profile if dry |
| V6–V12 (late May–mid June) | 0.15–0.25 | 6–8 | Begin when top 2 ft reaches ~50% depletion |
| V12–VT (mid–late June) | 0.25–0.35 | 10–12 | Rapid growth; do not fall behind entering tassel |
| VT–R2 silking/blister (late June–mid July) | 0.30–0.35, peaks 0.5 | 14–17 | **Most critical**; maintain ≥55% available water; capacity-limited systems run continuously |
| R2–R4 blister–dough (mid July–early Aug) | 0.25–0.30 | 20–22 | Still high demand |
| R4–R5 dough–dent (early–late Aug) | 0.15–0.25 | 24–26 | Taper |
| R5–R6 dent–black layer (late Aug–mid Sept) | 0.05–0.15 | 26–28 | Last irrigation decision (below) |

**Remaining water use to maturity (K-State eUpdate, Issue 1116, 2026-08-13):**
blister ≈ 45 days / 10.5 in; dough ≈ 34 days / 7.5 in; beginning dent ≈ 24 days /
5.0 in; full dent ≈ 13 days / 2.5 in; black layer 0. Rule: at a given stage, compare
remaining use with (available soil water above the 45% depletion line + expected
rain); irrigate only the shortfall. On deep silt loams holding ~2 in available water
per foot, a full 4-ft profile at full dent usually means **no further irrigation**.

### Scheduling tools
- **KanSched** (K-State Mobile Irrigation Lab; KanSched3 / KanSched online) — ET-based
  checkbook using reference ET from the nearest Kansas Mesonet station (Sedgwick-area
  stations **verify**: e.g., Viola/Clearwater/Hutchinson 10SW), crop coefficient by
  stage, soil water-holding capacity and rainfall. Run one account per pivot.
- **Kansas Mesonet** daily ET/evapotranspiration product and soil moisture; NWS
  Wichita 7-day QPF for rain forecasts.
- Soil moisture sensors (Watermark or capacitance probes) at 1, 2, 3 ft in two
  locations per pivot to calibrate the checkbook.
- Pivot telemetry: speed/application depth tables; verify applied depth with catch
  cans once per season (uniformity).

## Center-pivot capacity needs and well constraints

**Capacity arithmetic** (1 acre-inch = 27,154 gal):
- gpm per acre required = (peak ET in/day × 27,154) ÷ (1,440 min/day × efficiency).
  At 0.35 in/day and 85% efficiency: **7.8 gpm/ac** (matches Virginia Extension's
  7.8 figure). At 0.30 in/day: 6.7 gpm/ac. K-State design fragments cite ≥5 gpm/ac as
  a minimum for corn (deficit).
- A 130-acre pivot therefore wants ~1,000 gpm for full-yield corn; **600 gpm (4.6
  gpm/ac) delivers only ~0.21 in/day gross** — a deficit-irrigation system in which
  corn yield depends heavily on stored soil water and rain. At 600 gpm the planning
  population drops to ~26–28k and expected yield to ~170–190 bu/ac (**verify** with
  K-State limited-irrigation results, which generally show corn still out-yielding
  sorghum per inch at capacities ≥ ~4 gpm/ac in average years but not in droughts).
- Equus Beds wells in Sedgwick/Harvey County commonly yield several hundred to
  >1,000 gpm depending on saturated thickness (**verify** per well; WIMAS/DWR records).

**Water rights and GMD2 (Equus Beds Groundwater Management District No. 2):**
- GMD2 covers ~879,000 acres in parts of Sedgwick, Harvey, Reno and McPherson
  counties; >2,000 permitted wells withdraw ~177,000 ac-ft/yr on average (2023 report);
  irrigation ≈60% of use, municipal (Wichita, Equus Beds ASR) ≈25%, industrial ≈12%;
  >100,000 irrigated acres (district average 143,178 ac, 2011–2015).
- KGS (OFR 2017-3) estimated sustainable pumping ("Qstable") at ~180,308 ac-ft/yr,
  about 1.2% below average reported use — i.e., the district is roughly at its
  sustainable limit in aggregate, with some townships well above and showing
  water-level declines. Expect tightening, not new water.
- **Moratorium:** GMD2 has restricted new appropriations (moratorium extended in 2019;
  current scope **verify**). Assume no new water rights are obtainable; only existing
  rights, changes in place of use, or purchases/leases.
- **Authorized quantity:** each right specifies acre-feet per year and authorized
  acres. Older Kansas irrigation rights commonly authorize 1.5–2.0 ac-ft/ac (18–24
  in); actual use in neighboring GMD5 averages ~12.5 in/ac (Hendricks/K-State). The
  **field's authorized quantity, not the agronomic need, caps corn acres under the
  pivot** — **verify** per right via KDA-DWR WIMAS.
- Multi-Year Flex Accounts (MYFA) allow a 5-year allocation to be moved between years
  (statewide KDA program; terms **verify**) — valuable for pumping more in a drought
  year and less in a wet one.
- Assessments are small: district water-use charge capped at $2.00/ac-ft and land
  assessment at $0.05/ac (GMD2 report). Water-use reports due annually to DWR
  (March 1); meter required.
- Water quality: parts of the Equus Beds have chloride plumes (Burrton oilfield brine,
  Arkansas River) — test irrigation water before committing to corn.

## Pumping cost per acre-inch (method + 2026 estimates)

K-State method (MF2360 / L885): energy per acre-inch = whp-hr ÷ fuel factor, where
whp-hr per acre-inch ≈ 0.1144 × total dynamic head (ft), and fuel factors (Nebraska
Pumping Plant Performance Criteria) are **12.5 whp-hr/gal diesel, 61.7 whp-hr/MCF
natural gas, 0.885 whp-hr/kWh electricity**. Cross-check: 150 ft lift + 60 psi (≈290 ft
TDH) → ~33 whp-hr → ~37 kWh per acre-inch, matching the Colorado State figure.

Assumed Equus Beds pivot: 80 ft lift + 35 psi (≈81 ft) + friction ≈ **180 ft TDH →
~20.6 whp-hr per acre-inch** (lift **verify** per well). Real pumping plants often run
15–30% below the Nebraska criteria, so add ~25% to the energy figures.

| Energy source | Energy per ac-in (at criteria) | Unit price assumption (2026-10, **verify** local) | Cost per ac-in (criteria → with 25% inefficiency) | Notes |
|---|---|---|---|---|
| Electric | 23 kWh | $0.11–0.14/kWh energy charge | $2.60–3.30 → $3.20–4.10, **plus demand/horsepower charges** typically adding $1–3/ac-in on low-use seasons | Cleanest to schedule; demand charges penalize short seasons; Evergy/co-op irrigation tariff **verify** |
| Natural gas | 0.33 MCF | $6–10/MCF delivered farm tap | $2.00–3.35 → $2.50–4.20 | Historically the dominant Kansas pumping fuel (~59% of pumping, older KGS data); engine maintenance higher than electric |
| Diesel | 1.65 gal | $3.00–3.60/gal off-road | $4.95–5.95 → $6.20–7.45 | Most expensive and most volatile (see `knowledge/inputs/diesel-and-fuel.md`); Southern Ag Today 2026-07 shows a $5/gal diesel case raising a 24-in season from $88 to $147/ac |
| Reference points | — | — | K-State 2018 NW KS budget: $35.30/$46.54/$54.56 per ac at 11/14.5/17 in ≈ **$3.21/ac-in** (deeper lifts than Equus Beds, 2018 prices); K-State 2016 SW KS budget $2.85/ac-in fuel | dated |

Planning value for this farm until a well is characterized: **$3.50/ac-in electric or
gas, $6.50/ac-in diesel (energy only)**, plus pivot repairs/maintenance ~$1.00–1.50
per ac-in and irrigation labor ~$0.50–0.75 per ac-in (**verify** against K-State
2026 SC irrigated corn budget).

## Yield expectations (irrigated)

| System class | Trend yield (bu/ac) | Adverse (bu/ac) | Favorable (bu/ac) | Source / status |
|---|---|---|---|---|
| Full-capacity pivot (≥7 gpm/ac), deep silt loam, corn after soybeans | 210–230 | 160–180 (heat at silking, hail, disease, pumping limits) | 250–270 | Kansas irrigated averages ~200+ bu/ac statewide; 2025 contest: Barton County irrigated 277 bu/ac, state record 349 bu/ac (Haskell). KFMA SC irrigated corn average **not retrieved — verify** |
| Limited-capacity pivot (4–5 gpm/ac) | 170–190 | 110–140 | 210–230 | K-State limited-irrigation literature; estimate **verify** |
| Sandy soils (Arkansas River valley), full capacity | 190–210 | 140–160 | 230–250 | lower water holding → tighter scheduling; estimate **verify** |

NASS Sedgwick County irrigated corn yield series: not retrieved — pull with the dryland
series (see corn-dryland.md gaps).

## Fertility (irrigated differences)

- **N:** MF2586 formula with yield goal ~105% of 3–5 yr average; irrigated **cap 300 lb
  N/ac**. Example: 220 bu goal × 1.6 = 352 − SOM credit (2% × 20 × 0.5 no-till = 20) −
  profile N (20) − soybean credit (40, **verify**) = **~270 lb N/ac**; after wheat or
  corn, ~300 (at cap). Practical irrigated program: 40–60 lb pre-plant/starter, 120–150
  lb sidedress V5–V8 (anhydrous or UAN), and 40–60 lb fertigated through the pivot at
  V12–R1 (UAN 32 injected; requires backflow prevention/chemigation permit — Kansas
  chemigation law **verify**). Fertigation lets N be matched to the season (cut the last
  increment in a poor year).
- At $0.60/lb N (DTN anhydrous 2026-10-21), 250 lb N ≈ **$150/ac**; UAN for
  fertigation at $0.76–0.80/lb N costs 25–30% more per unit N.
- **P/K:** removal at 220 bu ≈ 75–80 lb P2O5 and 55–60 lb K2O per year (general
  factors, **verify**); on build-maintain soils plan 60–80 lb P2O5, K per test.
- **S:** more often responsive in irrigated corn on sandy soils; 15–25 lb S/ac
  (**verify** K-State).
- **Zn:** same DTPA <1.0 ppm threshold; high-yield corn more responsive.
- Nitrate leaching on sandy soils under irrigation is the main N-loss pathway (versus
  volatilization dryland): split heavily, use nitrapyrin with any fall/early anhydrous
  on sands, avoid large pre-plant applications.

## Pest differences under irrigation

- **Diseases:** irrigated canopies hold leaf wetness — gray leaf spot, southern rust
  and (in cool years) tar spot pressure is higher; a VT–R1 fungicide is routine on
  irrigated corn with ≥200 bu potential (budget it). Goss's wilt risk rises in
  irrigated corn-on-corn with wheel-track leaf injury. Aflatoxin risk is lower
  (less stress) but not zero — maintain water through R4 in heat waves.
- **Insects:** spider mites can still flare in July heat (pivot wetting helps
  suppress); corn rootworm matters only in corn-on-corn; earworm/WBC pressure higher
  in attractive green fields — Vip3A Bt.
- **Weeds:** more flushes (irrigation triggers germination) — the second layered
  residual is non-negotiable; avoid applying residuals just before a heavy irrigation
  on sands (leaching/injury).

## Input program and cost per acre (irrigated, 2027 crop, priced 2026-10-31)

Base scenario: 220 bu/ac, full-capacity pivot, 32,000 seeds/ac, corn after soybeans,
12 in gross applied, electric or natural-gas pump. The **K-State 2026 "Irrigated Corn
Cost-Return Budget in South Central Kansas" (dated 2025-11-01) exists at agmanager.info
but could not be opened; replace every "verify" line with its figures.**

| Item | Rate | Unit cost | Cost/acre (USD) | Date priced | Source / status |
|---|---|---|---|---|---|
| Seed (Vip3A Bt + glyphosate/glufosinate; RW trait only if corn-on-corn) | 32,000 seeds | $3.78/1,000 | $121 | 2026 | UMD/ISU 2026 budgets; **verify** local; add $10–15 if RW trait |
| Nitrogen | 250 lb N (anhydrous + UAN fertigation blend) | $0.60–0.78/lb N | $155 | 2026-10-21 | DTN retail survey; blend assumption |
| N application (knife + fertigation injection) | 2 operations | — | $18 | 2026 | custom rates **verify** |
| Phosphorus | 70 lb P2O5 (MAP) | $0.75–0.95/lb | $53–67 | 2026-10 | **verify** |
| Potassium | 0–40 lb K2O | $0.45–0.55/lb | $0–22 | 2026-10 | **verify** soil test |
| Sulfur + zinc | 20 lb S, 1 lb Zn | — | $15–20 | 2026-10 | **verify** |
| Lime | pH <6.0 | — | $0–15 | — | **verify** |
| Herbicide (PRE + layered POST residual) | 2 passes | — | $55–70 | 2026 | ISU 2026 $56; Palmer program upper end |
| Herbicide application | 2 ground passes | $7–9 | $16 | 2026 | **verify** |
| Insecticide / miticide | contingent; budget 1 in 3 years | — | $8–12 | 2026 | MF810 |
| Fungicide VT–R1 (aerial) | 1 application | $28–35 incl. application | $32 | 2026 | K-State fungicide eUpdates; cost **verify** |
| Crop insurance (RP 75–80%, irrigated enterprise unit) | — | — | $25–40 | 2026 | **verify** with agent |
| Irrigation energy | 12 ac-in | $3.50/ac-in (electric/gas) | $42 (range $30–75; diesel 12 in ≈ $78) | 2026-10 | derived above; **verify** |
| Irrigation repairs and maintenance | 12 ac-in | $1.00–1.50/ac-in | $15 | 2026 | **verify** vs K-State budget |
| Irrigation labor | 12 ac-in | $0.50–0.75/ac-in | $8 | 2026 | **verify** |
| Fuel and lube (field operations) | ~4.5–5.5 gal/ac | see diesel file | $18–24 | 2026-10 | **verify** |
| Machinery repairs | — | — | $28–38 | 2026 | **verify** |
| Labor (field) | ~0.9–1.1 hr/ac | $25–30/hr | $27 | 2026 | **verify** |
| Drying | 4 pts on 220 bu | 4.4 ¢/pt/bu at $2.00 propane | $39 (range $25–55) | 2026-10 | ISU/Farm Progress rule; irrigated corn is harvested wetter (18–22%) to beat lodging and basis |
| Hauling | 220 bu | $0.12–0.20/bu | $26–44 | 2026 | **verify** |
| Interest on operating capital | ~$650 × 8% × 7/12 | — | $30 | 2026 | **verify** |
| **Total direct (variable) costs** | | | **≈ $720–830** (point ~$770) | 2026-10-31 | |
| Machinery depreciation and interest | — | — | $60–80 | 2026 | **verify** |
| Pivot + well + pump ownership (depreciation, interest, insurance) | ~$1,000–1,300/ac installed (new pivot ~$130–170k per 130 ac incl. well/pump) over 20–25 yr | — | $65–95 | 2026 | estimate **verify** (existing paid-off systems carry only interest on salvage + insurance) |
| Land (owned; opportunity cost = irrigated cash-rent equivalent, Sedgwick) | — | — | $150–200 | 2025 | K-State 2025 irrigated rental rates — Sedgwick value **verify** |
| Management / overhead | — | — | $30–40 | — | **verify** |
| **Total specified costs** | | | **≈ $1,030–1,250** (point ~$1,130) | 2026-10-31 | |

Per bushel at 220 bu/ac: direct ≈ $3.50/bu; total ≈ $5.14/bu. Excluding the land charge
(owned land): total ≈ $4.30/bu.

## Breakeven (irrigated, priced 2026-10-31)

| Yield (bu/ac) | Price to cover direct ~$770 | Price to cover total excl. land ~$950 | Price to cover total ~$1,130 |
|---|---|---|---|
| 160 (adverse) | $4.81 | $5.94 | $7.06 |
| 190 | $4.05 | $5.00 | $5.95 |
| 220 (base) | $3.50 | $4.32 | $5.14 |
| 250 (favorable) | $3.08 | $3.80 | $4.52 |

- At ~$4.35 cash (2026 harvest price $4.75 less −40 ¢ Wichita-area basis), irrigated
  corn covers direct costs at ~177 bu/ac and all non-land costs at ~218 bu/ac; it does
  not return the full irrigated land opportunity cost at trend yields and 2026
  prices. This is consistent with 2025–2026 margins across the Plains and is why the
  irrigated branch must be compared against irrigated soybeans (lower cost, 2026 SC
  dryland soybean budget income $495/ac at 47 bu; irrigated 60–70 bu) and against
  drying/basis strategies, not assumed to win.
- Water-cost sensitivity: each additional acre-inch pumped costs ~$5 (electric/gas,
  all-in) to ~$8.50 (diesel); at $4.35 corn that is 1.1–2.0 bu/ac-in. Marginal corn
  response to water in the deficit range is typically 8–12 bu per acre-inch
  (K-State limited-irrigation results, **verify**), so pumping pays until the profile
  is full — the constraint is allocation and capacity, not cost.

## Marketing and insurance differences

- Yield scale: 220 bu × 130 ac per pivot = ~28,600 bu per pivot — trucking and
  storage/drying capacity, not price, is usually the first bottleneck. Check bin and
  dryer capacity in farm-profile.md before adding irrigated corn acres.
- Irrigated APH is separate from dryland APH; T-yields for irrigated corn in Sedgwick
  County **verify**. Irrigated practice requires adequate water (RMA "good farming
  practice") — a known-short allocation can void coverage; document the right.
- Higher, steadier yields justify earlier and larger forward sales (up to 50% of
  trend by June) than dryland.

## Decision rules for the irrigated branch (draft)

1. **Water first:** no irrigated corn is planned on a pivot until authorized quantity
   (in/ac), well capacity (gpm/ac), pump energy type and lift are recorded. Required:
   ≥12 in/ac of remaining annual (or MYFA) allocation and ≥5 gpm/ac; full-yield
   budget only at ≥7 gpm/ac and ≥14 in/ac.
2. **Capacity-to-crop match:** ≥7 gpm/ac → corn (or corn–soybean rotation);
   5–7 gpm/ac → corn at 26–28k population with deficit scheduling, or soybeans;
   <5 gpm/ac → sorghum or soybeans under the pivot, corn not planned.
3. **Energy:** if the pump is diesel, budget $6.50+/ac-in and prioritize electrification
   or natural gas conversion in the capital plan; irrigated corn margin at 2026 prices
   cannot absorb 15–18 in of diesel pumping in a drought year (~$100–120/ac).
4. **N trigger:** same corn:N ratio test as dryland (Dec corn ÷ $/lb N; 7.6 on
   2026-10-31). Below 6, shift the pivot to soybeans rather than cut corn N below the
   K-State rate — under-fertilized irrigated corn wastes the water.
5. **Fungicide:** budgeted by default; cancel only if scouting at V14–VT finds no
   GLS/southern rust/tar spot and the 10-day outlook is hot and dry.
6. **Last irrigation:** apply the K-State remaining-use table; stop at full dent if the
   profile is ≥55% available water. Overwatering past R5 is the most common wasted
   $10–15/ac.
7. **Rotation:** corn–soybean under pivots by default; corn-on-corn only when the price
   spread and water allow and with a RW-trait or soil insecticide plan.

## Open items / gaps

1. K-State 2026 "Irrigated Corn Cost-Return Budget in South Central Kansas" (2025-11-01)
   figures for every verify line; the 2027 edition when posted.
2. Per-field water rights (WIMAS), well tests (gpm, static/pumping level), pump energy
   type, pivot package efficiency.
3. GMD2 current rules: moratorium scope, any LEMA/IGUCA proposals, MYFA terms, ASR
   interactions near Wichita's wellfield.
4. Local utility irrigation tariff (energy + demand), farm-tap gas price, off-road
   diesel price — feed `data/processed/input_prices.csv`.
5. KFMA SC irrigated corn yields/costs and NASS Sedgwick County irrigated yield series.
6. Kansas Mesonet station choice and historical ET for Sedgwick County; KanSched
   calibration run.
7. Kansas chemigation permit requirements for fertigation through the pivot.

## Change log
- 2026-10-31 — Initial version; differences-only companion to corn-dryland.md.
  Pumping costs derived from K-State conversion factors and assumed 180 ft TDH; all
  prices, allocations and yields flagged verify pending water-right confirmation.
