---
title: Corn (maize) — dryland
domain: crops
last_reviewed: 2026-10-31
review_cadence: seasonal
confidence: medium (agronomy) / low (costs, county yields, local basis — several numbers flagged "verify")
sources:
  - K-State Agronomy eUpdate, "Optimal corn seeding rate recommendations" (Issue 792, 2020-03-27; re-issued as article 585-5) — regional population/seeding-rate table
  - K-State MF3208 "Kansas Corn Management 2025" — populations in >200 bu environments, starter placement
  - K-State C560 "Corn Production Handbook" — water use 22–30 in, final planting dates, maturity selection
  - K-State L818 "Kansas Crop Planting Guide" — planting windows by zone
  - K-State MF2586 "Soil Test Interpretations and Fertilizer Recommendations" (2024 revision, announced eUpdate Issue 996, 2024-03-21) — N formula, caps, SOM credit
  - K-State MF3572 "Predicting Corn Yield Based on Soil Nitrogen Supply"
  - K-State eUpdate (2025-04-10) — starter fertilizer placement and salt limits
  - K-State eUpdates "Critical timing in Kansas: high temperatures and corn development" (2016, 2022), "Corn development in Kansas during recent high temperatures" (2023-07-27), "Drought and heat stress in Kansas corn fields"
  - K-State eUpdates on fungicide timing for gray leaf spot (Issue 640, 2017; Issue 808, 2020; "Fungicide considerations for corn diseases in 2023"); MF2341 Gray Leaf Spot of Corn
  - K-State news release 2025-06 "Tar Spot confirmed in Kansas cornfields for 2025"; eUpdate "Update on Tar Spot in Kansas" (Issue 1112, 2026-07-16); eUpdate "Southern Rust is Now Active in Kansas" (Issue 1113, 2026-07-23); eUpdate "Southern rust continues to spread in Kansas this season" (2025-07-31)
  - K-State MF810 "Corn Insect Pest Management 2026"; eUpdate "Western Corn Rootworm Bt Traits and Resistance" (article 496)
  - K-State / Kansas Agricultural Experiment Station reports on multiple-resistant Palmer amaranth (Stafford County glyphosate + mesotrione; BT12 four-way; KCTR six-way; Riley County dicamba/2,4-D)
  - K-State Farm Management Guide, 2026 South Central Kansas budgets dated 2025-11-01 (grain sorghum and soybean PDFs read via search summaries; corn PDF exists at agmanager.info but could not be opened — see Gaps)
  - K-State 2025 budget comparison, north central Kansas, sorghum vs corn direct costs
  - Kansas Farm Management Association (KFMA) 2025 South Central Summary Book
  - K-State Tribune long-term dryland rotation and stubble-height studies (2007–2020); K-State eUpdate 2006-01-20 strip-till vs no-till corn into wheat stubble (2003–2005)
  - USDA NASS Kansas Crop Production reports (Aug 2023, Aug/Oct 2024), USDA NASS 2025 Kansas State Agriculture Overview
  - USDA RMA 2026 corn projected price; DTN 2026-10-30 harvest-price article; Rain and Hail harvest price table (Kansas)
  - DTN Retail Fertilizer Trends, weeks of 2026-10-07, -14, -21, -28
  - AGSIST Kansas cash bid index (2026-10-01 to -15); USDA AMS Kansas Daily Grain Bids via secondary summaries (2026-10-26)
  - University of Maryland and Iowa State 2026 crop budgets (seed and herbicide unit prices; used as proxies — verify against K-State)
  - Iowa State Ag Decision Maker A2-31 "Estimating the Cost for Drying Corn"; Farm Progress drying rule of thumb
  - NWS Wichita annual climate normals; currentresults.com / climate-zone.com (1991–2020 Wichita normals, secondary)
  - Kansas Corn Commission yield-contest releases (2023, 2024, 2025)
  - EIA Kansas state energy profile (ethanol plants and capacity, 2025); Kansas Grain Sorghum Producers "About Ethanol"
  - Illinois Corn / USDA on US corn exports to Mexico (2024/25)
  - PMC 2016 "Potential economic losses to the USA corn industry from aflatoxin contamination" (Kansas elevator schedule description)
used_by_agents:
  - agronomist
  - input-cost-analyst
  - market-analyst
  - orchestrator-planner
---

# Corn (maize) — dryland

> Scope: non-irrigated corn on this ~1,000-acre owned operation in Sedgwick County,
> Kansas. Irrigated differences live in `corn-irrigated.md`, which cross-references
> this file for everything shared. Research note: web fetch of K-State, NASS and NWS
> hosts was blocked in the session that wrote this file; numbers come from search
> summaries of those sources. Anything not directly sourced is given as a range and
> marked **verify**.

## Fit for this operation

**Climate fit — marginal to fair.** Sedgwick County receives roughly 30–33 in of
precipitation per year (farm-profile.md), but corn's seasonal water use is 22–30 in
(K-State C560), and the crop's most water-sensitive window (two weeks either side of
silking, roughly July 1–25 for late-April plantings) coincides with Wichita's hottest,
driest stretch (July average high about 93 °F, about 6 days at or above 100 °F in July,
first 100 °F day on average July 1 — NWS/1991–2020 normals, secondary sources). Dryland
corn here is a high-variance crop: excellent in years with full subsoil moisture and
timely July rain, poor to catastrophic in 2011/2012/2022-type years. Grain sorghum is the
lower-risk C4 alternative on the same ground and is the default comparator (see
"Decision rules").

**Soil fit.** Best on deep, medium-textured loams and silt loams with 8+ in of plant-
available water storage per 4 ft profile (Arkansas River valley alluvial soils and the
better upland silt loams). Avoid shallow, claypan, or sandy upland fields for dryland
corn; those go to sorghum, wheat or soybeans. Field-level soil series are TBD in
farm-profile.md — **the agronomist must fill the land table before assigning corn
acres.**

**Rotation fit — good.** Corn after soybeans (N credit, no rootworm carryover) or after
wheat (longer fallow, most stored water; K-State Tribune work found corn/sorghum yields
roughly 50% higher after wheat than after corn or sorghum, western Kansas data) are the
fits. Corn after corn is not recommended dryland here (water, rootworm, gray leaf spot,
Goss's wilt inoculum, N cost).

**Equipment fit.** Needs a row planter (30-in or 20/15-in), a sprayer with residual-
herbicide capability, a combine corn head, more trucking per acre than wheat or sorghum,
and either drying/aeration or a buyer that takes 17–18% corn. Equipment inventory is a
stub — verify a corn head and planter exist before planning corn acres.

**Storage fit.** Corn is the crop most likely to need drying on this farm (see
`knowledge/inputs/propane-and-drying.md`). Aeration bins sized to hold at least one
field's worth of corn at harvest are the practical minimum if harvest-time basis is weak.

**Disqualifiers.** Fields with a history of severe Palmer amaranth with confirmed HPPD +
glyphosate resistance and no clean-up plan; fields with less than ~6 in plant-available
water at planting in a drought year (shift to sorghum); fields where a planned wheat crop
follows (corn harvest is usually too late for timely wheat planting unless an early
hybrid is used).

## Agronomic requirements

| Parameter | Dryland recommendation for Sedgwick County | Source / status |
|---|---|---|
| Growing degree days to black layer | ~2,400–2,700 GDD (base 50 °F) for 105–112 day hybrids | industry/C560 general; **verify** against hybrid tag |
| Frost tolerance | Seedlings tolerate light frost if growing point below ground (to ~V5); kill at 28 °F after V6 | general agronomy |
| Planting window | April 20 – May 20 suggested (K-State L818 planting guide, zone covering south central KS). Practical target: April 10–30 when 2-in soil temperature is ≥50 °F at mid-morning and warming trend forecast. Final planting date reference for south central KS: June 4 (C560). Crop insurance final planting date — **verify** with agent (RMA Sedgwick County). | L818; C560 |
| Soil temperature | ≥50 °F at 2 in, with a warming 5–7-day forecast | K-State general guidance; **verify** exact wording |
| Final plant population | 18,000–22,000 plants/ac (south central dryland) | K-State eUpdate seeding-rate table (Issue 792, 2020-03-27) |
| Seeding rate | 21,000–26,000 seeds/ac to achieve the above (assumes ~85–90% stand) | same |
| Population adjustments | Lower end (18–20k) on upland/shallow soils, late planting, after sorghum; upper end (22k, up to 24k) on deep bottomland with full profile or after soybeans/wheat. Flex-ear hybrids tolerate the low end better. | K-State eUpdate: "final rate depends on environment, hybrid, planting date, rotation, tillage" |
| Row spacing | 30 in standard. Narrow rows (20 or 15 in) show little dryland yield advantage in Kansas and complicate low-population canopy; skip-row (plant 2, skip 1) is a western Kansas drought tactic, not recommended for 30-in precipitation. | general K-State guidance; **verify** |
| Planting depth | 1.75–2.0 in; go 2.0–2.5 in into dry seedbed for moisture; never shallower than 1.5 in | C560 general |
| Hybrid maturity | 105–115 day RM; sweet spot 108–112 day. Earlier (105–108) if planting after May 10, on shallow soils, or if wheat follows. Note: there is no standardized industry maturity rating; compare within a company and use K-State Performance Tests (south central dryland sites). | C560; K-State performance tests (SRP series) |
| Hybrid traits | Drought-tolerance screened hybrids (e.g., Pioneer AQUAmax, Bayer DroughtGard/VT4PRO-class, Syngenta Artesian). Bt: above-ground lepidopteran package (Vip3A-containing packages give the best earworm/WBC suppression) is worth paying for; below-ground rootworm Bt is **not** needed in first-year corn after soybeans/wheat/sorghum — use a non-RW trait or conventional to save $10–20/ac (**verify** seed price list). Herbicide traits: glyphosate + glufosinate tolerant at minimum; consider Enlist (2,4-D choline + glufosinate + FOP) for Palmer programs. Atrazine, mesotrione etc. need no trait. | MF810; K-State Palmer research |
| Seasonal water use | 22–30 in total ET (C560); dryland yield roughly tracks stored soil water at planting plus May–August rain. Peak use 0.30–0.35 in/day, up to 0.5 in/day in heat, around VT–R2 (K-State irrigation publications). | C560; MF3066; K-State Sunflower district irrigation page |
| Critical stress window | V12–R2 (about 2 weeks before to 3 weeks after silking). Temperatures above 95 °F and small day–night temperature range during pollination reduce pollen viability and kernel number (K-State eUpdate 2016). In 2022, K-State recorded stress-degree-day accumulation of ~170–200 around R1 with pollination failure at mid and basal ear positions. | K-State eUpdates 2016, 2022, 2023 |
| Harvest | Black layer ~late Aug–mid Sept for late-April planting; field dry-down to 15–18% by mid/late Sept in a normal year. | general |

### Planting system: no-till into residue
- **Into soybean stubble (preferred):** easy planting, warmer/drier seedbed, N credit,
  no rootworm. Residue is light, so plant on time (April 15–30).
- **Into wheat stubble (previous year's wheat, i.e., 10 months fallow):** most stored
  water; heavy residue keeps seed zone cool and wet — wait for 50 °F and use row
  cleaners; strip-till in fall is an option (K-State 2003–2005 data: strip-till corn
  61 bu/ac vs no-till 48 bu/ac into wheat stubble in a 6-in-rain season; eUpdate
  2006-01-20). Taller-cut stubble helps: +8 bu/ac for corn into high or strip-cut vs
  low-cut wheat stubble, Tribune 2007–2020 average. Watch for chinch bugs moving
  from wheat residue, and for volunteer wheat/cheat as a green bridge.
- **Into sorghum stubble:** least preferred dryland. Sorghum leaves the profile
  driest, residue hosts the same stalk rot complex, and atrazine applied to sorghum
  is not a problem (corn tolerates it) but sorghum herbicides like Zidua/Outlook are
  also fine. Lower population by ~2,000 plants/ac vs after soybeans.
- Starter band (2x2) of N+P enhances early growth in no-till corn into corn,
  sorghum or wheat stubble (K-State MF3208 2025).

## Yield expectations

| Soil / field class | Trend yield (bu/ac) | Adverse (bu/ac) | Favorable (bu/ac) | Source |
|---|---|---|---|---|
| Deep bottomland / alluvial silt loam, after soybean or wheat, full profile | 120–135 | 40–70 | 160–190 | KFMA SC 2025 non-irrigated corn average ≈112 bu/ac (all farms); K-State 2026 SC budgets use ~110–120 for sorghum; Sedgwick County yield-contest dryland winners 219 bu/ac (2023) and 170 bu/ac (2024) show the ceiling. Class split is an estimate — **verify** with field records |
| Good upland silt loam | 100–115 | 30–60 | 140–160 | as above, estimate — **verify** |
| Shallow / claypan / sandy upland | 70–90 | 10–40 (abandonment possible) | 110–130 | estimate — **verify**; sorghum usually wins here |
| Kansas statewide (all practices, incl. irrigated) | 2023: ~119 bu/ac (8% below trend); 2024: ~138 (Oct forecast); 2025: 145 | — | — | USDA NASS Kansas Crop Production, farmdoc daily |

- **NASS Sedgwick County series (non-irrigated / irrigated, 2015–2025): NOT retrieved
  in this session.** NASS county PDFs (e.g., 23KScorn.pdf) exist but were unreadable.
  Action item: pull from NASS Quick Stats (Kansas, Sedgwick, CORN GRAIN, YIELD,
  PRODUCTION PRACTICE = NON-IRRIGATED / IRRIGATED) into
  `data/reference/nass_sedgwick_corn_yields.csv` before any plan uses the table above.
- Planning convention (CLAUDE.md): carry base / adverse / favorable; for corn the
  adverse case must include a ~1-in-8 year of ≤50 bu/ac and partial abandonment.
- Yield goal for N: K-State says ~105% of the field's 3–5 year average (MF2586).

## Input program and cost per acre (dryland, 2027 crop, priced 2026-10-31)

Base scenario: 110 bu/ac yield goal, no-till after soybeans, 24,000 seeds/ac, 30-in
rows. The official **K-State 2026 "Corn Cost-Return Budget in South Central Kansas"
(dated 2025-11-01) exists at agmanager.info but could not be opened in this session;
every line below is either sourced as noted or an estimate to be replaced by that
PDF's figure.** The sibling 2026 SC budgets that were readable: grain sorghum $4.56/bu,
110–120 bu/ac, returns above direct expenses $277–295/ac, above total specified
expenses $202/ac, total expense $2.72/bu; soybeans 47 bu/ac × $10.53 = $494.91 income.

| Item | Rate | Unit cost | Cost/acre (USD) | Date priced | Source / status |
|---|---|---|---|---|---|
| Seed (Bt above-ground + glyphosate/glufosinate, no RW trait) | 24,000 seeds | $3.78 per 1,000 seeds | $91 | 2026 budgets | UMD 2026 and ISU 2026 budgets ($3.78–3.79/1,000); K-State SE KS older budget $3.33. **verify** local quote; drought-trait premiums can add $0.30–0.60/1,000 |
| Nitrogen (anhydrous, pre-plant or sidedress) | 110 lb N (after 40 lb soybean credit and ~20 lb profile N; see fertility section) | $0.60/lb N ($987/ton NH3) | $66 | 2026-10-21 | DTN retail fertilizer survey, national avg, 3rd week Oct 2026 (anhydrous up 17% y/y). Local Koch/Wichita quote may differ — see `knowledge/inputs/fertilizer-nitrogen.md` |
| N application (custom knife-in) | 1 pass | $12–16/ac | $14 | 2026 | Kansas Custom Rates 2026 (KDA/K-State) exists; value **verify** |
| Phosphorus (MAP 11-52-0, starter 2x2 or broadcast) | 40 lb P2O5 (~77 lb MAP; supplies 8.5 lb N) | $0.75–0.95/lb P2O5 | $30–38 | 2026-10 | DTN MAP price not captured; range **verify**; see `fertilizer-phosphorus-potassium.md` |
| Potassium | 0–30 lb K2O (most Sedgwick soils test >130 ppm K; apply only if soil test <130 ppm) | $0.45–0.55/lb K2O | $0–15 | 2026-10 | **verify** soil test and price |
| Sulfur | 10–15 lb S (AMS or ATS in starter) on sandy/low-OM fields | — | $6–10 | 2026-10 | K-State guidance is soil-test/texture based; **verify** rate |
| Zinc | 1 lb Zn chelate in starter if DTPA Zn <1.0 ppm | — | $0–8 | 2026-10 | threshold from K-State MF2586 general practice; **verify** |
| Lime | as needed, pH <6.0 | $35–45/ton ECCE applied | $0–15 (amortized) | — | **verify** |
| Herbicide program (PRE residual + POST w/ residual; see weeds) | 2 passes | — | $50–65 | 2026 | ISU 2026 budget $56/ac; Kansas Palmer programs with layered residuals run the upper end. **verify** with retailer |
| Herbicide application | 2 passes | $7–9/ac/pass | $16 | 2026 | custom rates **verify** |
| Insecticide | seed treatment included in seed; foliar only on threshold (mites/earworm rarely justified) | — | $0–8 | — | MF810 |
| Fungicide | none planned dryland; VT–R1 application only if GLS/southern rust/tar spot threshold met and yield potential >130 bu | — | $0 (contingent $28–35 incl. application) | 2026 | K-State fungicide eUpdates; cost **verify** |
| Crop insurance (RP 75–80%, enterprise unit) | — | — | $15–28 | 2026 | **verify** with agent; projected price $4.62 (RMA 2026) |
| Fuel and lube (no-till: plant, 2 spray, harvest, haul) | ~3.5–4.5 gal diesel/ac | see `diesel-and-fuel.md` | $14–20 | 2026-10 | K-State budget machinery tables; **verify** |
| Machinery repairs | — | — | $18–28 | 2026 | **verify** vs K-State 2026 SC corn budget |
| Labor | ~0.6–0.8 hr/ac | $25–30/hr | $18–24 | 2026 | **verify** |
| Drying | 2–4 points removed on 110 bu | 4.4 ¢/pt/bu at $2.00 propane (0.022 × price) | $10–19 | 2026-10 | Farm Progress / ISU A2-31 rule of thumb; commercial drying 5 ¢/pt/bu (2025–26 posted rate, Illinois elevator). Conway propane price **verify** |
| Hauling | 110 bu, 20–40 mi | $0.12–0.20/bu | $13–22 | 2026 | **verify** |
| Interest on operating capital | ~$300 × 8% × 7/12 | — | $14 | 2026 | assumption **verify** rate |
| **Total direct (variable) costs** | | | **≈ $345–420** (point estimate ~$385) | 2026-10-31 | Cross-check: K-State 2025 NC Kansas comparison put corn direct costs ~$106/ac above sorghum's $246 ⇒ ≈$352 at 120 bu; 2026 inputs higher |
| Machinery depreciation and interest (ownership) | — | — | $45–65 | 2026 | **verify** vs K-State budget |
| Land charge (owned; opportunity cost = cash rent equivalent, Sedgwick non-irrigated) | — | — | $55–75 | 2025 | K-State 2025 county cash rental rates (Ibendahl) — Sedgwick value **verify** |
| Management / overhead | — | — | $20–30 | — | **verify** |
| **Total specified costs** | | | **≈ $470–590** (point estimate ~$525) | 2026-10-31 | |

Per-bushel: direct ≈ $3.50/bu and total ≈ $4.75/bu at 110 bu/ac (point estimates).

## Fertility detail (K-State MF2586, 2024 revision)

**Nitrogen recommendation (lb N/ac):**

N rec = (1.6 × yield goal) − SOM credit − profile nitrate-N − manure/other credits + previous-crop adjustment, capped at **230 lb N/ac for dryland corn** (300 irrigated).

- Crop N factor was raised to **1.6 lb N/bu** in the 2024 revision (previously 1.3).
- SOM credit ≈ **20 lb N per 1% soil organic matter** for warm-season crops; for no-till
  the credit adjustment is reduced 50%.
- Profile nitrate: sample to 24 in (0–24 in profile N test) in late winter/early spring;
  south central Kansas profiles after a failed or low-yield crop commonly carry 20–60 lb
  NO3-N/ac, after a good soybean crop 10–25 lb — **verify** by sampling every field
  intended for corn; this is the cheapest N decision on the farm.
- Previous-crop adjustment: soybean credit is conventionally **40 lb N/ac** in K-State
  materials (**verify** against MF2586 2024 table, which this session could not read);
  alfalfa larger; wheat and sorghum zero.
- Yield goal = ~105% of field's 3–5 year average (MF2586). Do not use favorable-case
  yields for N.
- Worked example, 115 bu goal after soybeans, 2% SOM, 20 lb profile N, no-till:
  184 − (40 × 0.5 = 20) − 20 − 40 = **~104 lb N/ac**. Same field after wheat with 1.5%
  SOM and 35 lb profile N: 184 − 15 − 35 − 0 = **~134 lb N/ac**.
- K-State MF3572 ("Predicting Corn Yield Based on Soil Nitrogen Supply") supports
  using measured soil N supply rather than a flat rate.

**Timing and form (dryland):** Split is risk management, not yield: 30–50% pre-plant
or at planting (anhydrous or UAN with starter), balance sidedressed V4–V8 only if the
crop and moisture outlook justify it. In a drought spring, withholding the sidedress is
the single largest input saving available (~$35–45/ac at 60–70 lb N). Stabilizers:
nitrapyrin or DCD with fall/early-spring anhydrous on sandy or wet-prone fields; NBPT
urease inhibitor on any surface-applied urea/UAN not incorporated within 2–3 days.
Surface-applied urea on no-till residue without rain is the main loss pathway here.

**Starter:** 2x2 band of 10-34-0 or MAP + ATS is the most reliable starter method in
no-till. In-furrow (pop-up) rates must stay low: K-State eUpdate 2025-04-10 cautions
against high N and/or K in starter; safest placement is a band 2–3 in from the seed.
Industry/university guidance: keep N + K2O in a 2x2 under ~75–100 lb/ac, and in-furrow
under ~10 lb N + K2O on 30-in rows (**verify** against K-State table).

**P and K:** Build-and-maintain or sufficiency per K-State soil-test categories; corn
removal ≈ 0.35 lb P2O5 and 0.27 lb K2O per bushel (general; **verify**). Never skip
starter P on low-testing or cold soils regardless of price
(`fertilizer-phosphorus-potassium.md` rule).

**Zinc and sulfur:** Zn response likely where DTPA Zn <1.0 ppm (common on eroded,
high-pH, or leveled soils; 1 lb chelated Zn in starter or 5–10 lb Zn sulfate
broadcast). S response increasingly common on low-OM sandy soils and after wet
springs; 10–20 lb S/ac as ATS/AMS (**verify** K-State S recommendation).

## Weed management

**Key species in Sedgwick County:** Palmer amaranth (dominant), waterhemp (increasing,
bottomland), kochia (lighter soils, early emergence), large crabgrass, foxtails,
shattercane/johnsongrass (field-specific), volunteer wheat/cheat after wheat, morningglory,
velvetleaf.

**Resistance status (K-State research):**
- Palmer amaranth populations in Kansas confirmed resistant to glyphosate + mesotrione
  (HPPD) (Stafford County, adjacent region); to glyphosate + chlorsulfuron (ALS) +
  mesotrione + atrazine (population BT12); a six-way-resistant population (KCTR,
  Riley County area) with 84–90% survival to mesotrione/tembotrione; and dicamba +
  2,4-D resistance confirmed in a Riley County (Ashland Bottoms) population.
- Assume every Palmer population on this farm is glyphosate- and ALS-resistant, treat
  HPPD and atrazine as "working but at risk", and treat Group 4 (dicamba/2,4-D) as a
  tool to protect, not lean on.
- Kochia: glyphosate and ALS resistance widespread in Kansas; dicamba resistance present.

**Program (K-State two-pass PRE fb EPOST, shown effective on the Stafford County
population):**
1. **Burndown + PRE at planting:** glyphosate (grasses/volunteer) + a Group 15
   (S-metolachlor/acetochlor/pyroxasulfone) + atrazine (1–1.5 lb ai) ± a Group 27
   (mesotrione/bicyclopyrone) premix (e.g., Acuron, Resicore XL, Lexar-type). Add 2,4-D
   or dicamba burndown for emerged kochia/marestail (observe planting intervals).
2. **Early POST (V3–V5, Palmer <3 in):** glufosinate (Liberty) or 2,4-D choline (Enlist
   corn) or dicamba (pre-V8 only, drift risk to neighboring soybeans/cotton — note
   dicamba OTT labels for soybeans are in flux; corn dicamba use is a separate label) **plus a
   second Group 15 residual** ("layered residual") ± HPPD (tembotrione/topramezone) if
   the population still responds. Glyphosate alone POST is not a Palmer program.
3. Never let Palmer exceed 4 in before POST; late-season escapes seed the next 5 years.
   Harvest weedy fields last; clean combine.
- Trait choice: Enlist corn or glufosinate-tolerant corn gives a POST option
  independent of glyphosate. Conventional corn is viable with atrazine + Group 15 +
  Group 27 programs if seed savings matter.
- Carryover into next crop: atrazine >1.5 lb/ac restricts soybeans/wheat/sunflower the
  following year on high-pH or dry soils; mesotrione/isoxaflutole have rotation
  intervals for wheat and soybeans — check labels before planning wheat after corn.
- Cost reference: $50–65/ac for a layered-residual program (**verify**; ISU 2026
  budget $56).
- Consult the current K-State "Chemical Weed Control for Field Crops" (SRP series,
  2026) for rates; not readable in this session.

## Insect management (K-State MF810 "Corn Insect Pest Management 2026")

| Pest | Risk here | Management |
|---|---|---|
| Corn rootworm (western, some northern) | Low in first-year corn after soybeans/wheat/sorghum; higher only in continuous corn. Resistance to every commercial rootworm Bt trait has been detected in major corn areas (K-State eUpdate); rotation is the best tool. | Rotate; skip RW Bt in rotated corn; if continuous corn is ever grown, use pyramided RW traits, rotate trait families yearly, consider soil insecticide. Extended-diapause northern CRW and soybean-variant western CRW are not a documented problem in south central KS (**verify**). |
| Corn earworm | Common; ear tip feeding, aflatoxin entry wounds | Insecticide control "usually impractical in field corn" (MF810); Bt hybrids (esp. Vip3A) give suppression. Early planting reduces exposure. |
| Western bean cutworm | Historically western KS; MF810 2026 notes infestations becoming more perennial | Scout tassel-stage egg masses late June–July; some Bt packages (Vip3A) have activity; Cry1F no longer effective. |
| Spider mites (Banks grass mite, two-spotted) | Significant in hot, dry July–August, especially after broad-spectrum insecticide | Avoid unnecessary pyrethroids; threshold-based miticide (abamectin, etoxazole, bifenazate) when colonies move above ear leaf before dent; rain and humidity suppress. |
| Aphids (corn leaf aphid) | Usually minor; heavy tassel colonies in drought can interfere with pollination | Rarely treat; beneficials. |
| Wireworm / white grub / seedcorn maggot | Field-specific, higher after sod/CRP/long fallow or heavy residue | Standard neonicotinoid seed treatment (250 rate) adequate; bait stations pre-plant if history. |
| Chinch bug | Corn adjacent to or following wheat; dry springs | Scout wheat edges at wheat harvest; seed treatment helps early; border spray. |
| Cutworms (black) | No-till, weedy burndown, bottomland | Clean burndown 2+ weeks pre-plant; scout to V5; rescue pyrethroid at 3–5% cutting. |
| Grasshoppers | Field edges in dry years | Border treatment. |

## Disease management

| Disease | Status in south central Kansas | Management |
|---|---|---|
| Gray leaf spot | Most consistent foliar disease, worse in no-till corn-on-corn and humid Julys | Hybrid resistance first (short-season resistant hybrids exist; for the company's most resistant rating fungicide generally not recommended). If needed, single fungicide at **VT–R1** is the best-documented timing (K-State). Scout from 2 weeks before tassel. Rotation removes residue inoculum. |
| Southern rust | Blows in from the south most years, sometimes early. Confirmed in ≥21 Kansas counties by 2025-07-31 (central, eastern, SW); 2026 trace levels in Stafford, Jefferson, Meade counties by 2026-07-23 — Stafford is two counties west of Sedgwick. | Dryland corn planted in April is usually at R3+ when rust arrives and is rarely sprayed; late-planted corn is at risk. VT–R1 fungicide also suppresses southern rust and tar spot. Track the Corn ipmPIPE / Kansas Corn Disease Network map. |
| Tar spot | **Present in Kansas since 2024/2025 but, as of 2026-07-16, confirmed only in northeast and north-central counties** (2025: Doniphan first on 2025-06-11 — first US report of the season — then Brown, Jefferson, Atchison, Jackson, Republic, Marshall, Washington, Lincoln 2025-10-10, Smith 2025-10-16; 2026 by July 16: Republic, Brown, Washington, Nemaha, Marshall, Jewell, Atchison, Jefferson, Doniphan). Severity overall low; some NE Kansas growers reported severe yield impact. Not confirmed in Sedgwick County. | Scout; favored by cool (60–70 °F), humid, long leaf-wetness periods — Wichita Julys are generally too hot, so risk is mainly in cool wet years and irrigated canopies. Fungicide at VT–R2 if lesions present pre-tassel. Re-check status each July. |
| Goss's wilt (bacterial) | Occurs primarily in NW Kansas, NE Colorado, SW Nebraska; sporadic in central KS after hail/sandblasting in no-till corn-on-corn | No fungicide works (bacterial). Hybrid tolerance ratings, rotation, residue management. |
| Stalk rots (Fusarium, charcoal rot, anthracnose) | Charcoal rot is the signature dryland Kansas stalk rot in hot dry years; stress at grain fill cannibalizes stalks | Balanced K, avoid excess population, pinch test at R6 and harvest lodging-prone fields first. |
| Ear rots / **aflatoxin** (Aspergillus flavus) | Primary quality risk in hot, dry years (2011, 2012, 2022 in Kansas). Stress during grain fill plus insect wounding drives it. K-State-linked 2023 study projects Kansas aflatoxin losses rising under warming. | Agronomic: early planting, adequate population (not excessive), Bt for earworm, timely harvest, dry to <15% quickly, cool aeration. Market: FDA action level 20 ppb for interstate food/feed corn; elevators test by black light then quantitative. A Kansas elevator schedule referenced in the literature (Team Marketing Alliance, Moundridge; older) was described as more lenient than Texas but **did not accept lots over 200 ppb**; typical Kansas discounts step at 20/50/100/200 ppb — current local schedule **verify** each August. Insurance: aflatoxin is an insurable quality loss only if sampled/tested **before** harvest or before the grain goes into storage (RMA Loss Adjustment Procedures for Aflatoxin) — call the agent before combining a suspect field. |
| Seedling blights (Pythium, Fusarium) | Cold wet no-till seedbeds | Fungicide seed treatment (standard), wait for 50 °F. |

## Heat and drought at pollination — the defining risk

- Wichita normals (1991–2020, secondary sources): July average high ~93 °F (sources
  range 91–93), ~6 days ≥100 °F in July, average first 100 °F day July 1, last
  August 17; July rainfall ~3.5 in (**verify** NCEI normals, station USW00003928).
- K-State: temperatures above 95 °F and, importantly, warm nights (small diurnal
  range) around flowering reduce pollen viability and kernel number; under dryland
  conditions heat and water stress "use to happen together" (eUpdate). Stress during
  R2–R3 causes additional kernel abortion and lower kernel weight.
- 2022 example: stress degree days ~170–200 around R1 → pollination failures at ear
  middle/base (K-State North Farm). 2023 SDD accumulation far lower.
- Tactics: (1) plant April 10–25 so silking lands late June/first days of July, ahead
  of the mean first 100 °F day; (2) low population (18–20k) so each plant has more
  water; (3) deep-rooted, drought-scored hybrids with good silk–pollen synchrony
  (short ASI); (4) hybrid maturity spread (108 and 112 day) across fields to spread
  pollination dates; (5) no-till + tall stubble for stored water; (6) sorghum on the
  shallow fields.
- Track with Kansas Mesonet (stress degree days, soil moisture) and the NWS Wichita
  CPC 6–10/8–14 day outlooks in late June; a hot-dry outlook at V12 is the trigger to
  skip sidedress N and fungicide.

## Machinery and labor requirements

| Operation | Timing | Approx. hours/ac | Notes / timeliness penalty |
|---|---|---|---|
| Burndown + PRE spray | 0–7 days pre-plant | 0.06–0.08 | Late PRE = Palmer escapes |
| Anhydrous (if pre-plant) | Mar–Apr | 0.10–0.12 (or custom) | Wait 5–7 days before planting over the band, or offset |
| Plant (no-till, 30-in, 16-row) | Apr 10–May 10 | 0.10–0.13 | Yield loss accelerates after ~May 10 in south central KS (~0.5–1 bu/ac/day, general **verify**) |
| POST spray | V3–V5 (May 10–June 5) | 0.06–0.08 | Palmer >4 in = control failure |
| Sidedress UAN (optional) | V4–V8 | 0.08–0.10 | |
| Fungicide (contingent) | VT–R1 (late June–July) | aerial custom | |
| Harvest (8-row head) | Sept 10–Oct 15 | 0.20–0.30 | Harvest ahead of soybeans; field losses and stalk lodging rise after Oct 15 in charcoal-rot years |
| Hauling / drying | Sept–Oct | 0.10–0.15 | ~2.5–3× the bushels per acre of wheat ⇒ truck capacity is the bottleneck |
| **Total labor** | | **~0.6–0.9 hr/ac** | **verify** vs K-State machinery tables |

Dryland corn harvest (mid-Sept) competes with wheat planting prep and soybean harvest;
it also precedes sorghum harvest, which spreads combine use — one of corn's logistical
advantages over all-sorghum.

## Marketing

**Local demand structure (Wichita area):**
- **Ethanol:** Kansas has 11 operating plants with ~561 million gal/yr capacity (EIA
  Kansas profile; nameplate 643 MGY listed for 2025 — the two EIA figures differ),
  consuming roughly 183 million bu of corn and sorghum per year (Kansas Grain Sorghum
  Producers). The Colwich plant in Sedgwick County (former Abengoa site, 25 MGY
  nameplate; Element LLC groundbreaking 2018 for a $175 M expansion) is listed on
  cash-bid aggregators as "Cardinal Colwich" (Cardinal Ethanol) in Oct 2026 — **verify
  operating status, ownership and whether it posts corn bids**. Other plants within
  ~100 mi: Kansas Ethanol LLC (Lyons, Rice County), Pratt Energy (Pratt), plus plants
  at Garnett, Phillipsburg, Russell, and western Kansas (Liberal/Arkalon, Garden City,
  Hugoton) — capacities **verify** against EIA plant list.
- **Feed:** south-central/western Kansas feedlots and the Hutchinson/Wichita feed
  mills; corn competes with sorghum and wheat in rations.
- **Export:** Mexico took ~40% of US corn exports in 2024/25 (record 72.5 MMT total US
  corn exports); Kansas corn moves by rail (BNSF/UP) toward Mexico and the Texas Gulf.
  Kansas Corn is lobbying for a Mexican E10 standard, which would add ethanol pull.
  Trade-policy exposure is therefore direct (see `knowledge/geopolitics/`).
- **Local elevators/handlers:** Sedgwick County and adjacent cooperatives (e.g., in
  the Wichita–Haysville–Cheney–Garden Plain–Colwich–Mount Hope corridor), Team
  Marketing Alliance (Moundridge), ADM/Bartlett/Scoular terminals in the region —
  names and distances must be filled in farm-profile.md "Storage and handling".

**Basis:** Kansas corn is a basis-weak state relative to Illinois because of distance
to river markets, but the Wichita area is better than western Kansas thanks to the
Colwich plant and feed demand. Observed Oct 2026: Kansas average cash corn bid $4.59,
average basis about −31 ¢ vs December (AGSIST Kansas index, 2026-10-01 to -15; 221 of
221 tracked elevators cut bids in the period); USDA AMS Kansas country bids
2026-10-26 showed SW Kansas −110 to −75 ¢ Z and NW −80 ¢ Z. Harvest basis near Wichita
has typically run **−30 to −60 ¢** vs December, firming to **−15 to −35 ¢** by
spring (**verify** from local bid history; start logging weekly in
`data/processed/basis_corn_sedgwick.csv`). Ethanol-plant bids at harvest are often the
best local basis when the plant needs corn.

**Price reference (2026-10-31):** CBOT December 2026 corn settled 456.00 ¢/bu on
2026-10-23 (KDA report); RMA 2026 projected price $4.62, harvest price ≈$4.75
(DTN 2026-10-30; Rain and Hail lists Kansas $4.78). New-crop 2027 (Dec 2027) futures
**verify** before planning.

**Contracting:** forward contract or HTA 20–40% of expected production once Dec
futures exceed total-cost breakeven (see below); use basis contracts into the ethanol
plant when harvest basis is wide; never sell more than the adverse-case yield (~50
bu/ac) before pollination on dryland.

**Quality:** standard discounts for moisture >15.0–15.5% (shrink 1.3–1.4%/pt plus
drying 4–5 ¢/pt/bu), test weight <54 lb, damage, and aflatoxin (above). Food-grade
white/waxy premiums not relevant unless contracted.

## Risk profile

| Risk | Exposure | Mitigation |
|---|---|---|
| Drought/heat at silking | Highest of any crop in scope; ~1 year in 4 significant loss, ~1 in 8 near-total | Field selection, early planting, low population, hybrid spread, RP insurance, sorghum alternative |
| Hail | Sedgwick County is hail-prone; corn most vulnerable V10–R2 | Hail endorsement on high-value irrigated acres; dryland usually self-insured |
| Price | High: input commitments ($350+/ac) in March vs price in Oct; 2026 projected $4.62 vs breakeven ~$4.75 total cost | RP insurance harvest-price option, incremental forward sales |
| Input price (N) | Anhydrous $987/ton Oct 2026, +17% y/y (DTN); natural-gas and import driven (see fertilizer-nitrogen.md) | Buy N for corn in the summer/fall lull if ratio favorable; keep the soybean switch option open until March |
| Weed resistance | Multiple-resistant Palmer; losing HPPD + atrazine would remove the cheap PRE backbone | Two-pass layered residuals, zero seed rain, rotate to Enlist/glufosinate soybeans |
| Aflatoxin | Hot dry years; discounts to rejection | Bt, early harvest, pre-harvest testing, insurance procedure |
| Export/geopolitics | Mexico tariff/GMO disputes, Gulf freight, rail service; ethanol policy (RFS, E15, 45Z) | Diversify buyers (ethanol vs rail export vs feed), see geopolitics watchlist |
| Water (irrigated branch) | GMD2 allocation/moratorium; see corn-irrigated.md | |

## Rotation effects

- **Following crop N credit:** none from corn. Corn itself receives ~40 lb N/ac after
  soybeans (**verify** MF2586), none after wheat/sorghum.
- **Water:** corn leaves the profile depleted; wheat planted after corn (if harvest
  allows) usually yields less than wheat after soybeans/fallow in dry falls. Double-
  crop soybeans after corn are not possible (too late); the natural sequence is
  corn → soybeans (full season) or corn → wheat (if corn is off by Oct 1).
- **Residue:** heavy residue benefits following soybeans (erosion, moisture) but cools
  seedbeds; manage with row cleaners.
- **Disease:** corn-on-corn builds gray leaf spot, Goss's wilt, tar spot, rootworm.
  Sorghum and corn share Fusarium/charcoal stalk rot and some ear-rot fungi.
- **Herbicide carryover from corn:** atrazine (soybeans sensitive at high rates/high
  pH/dry year; wheat 8–12 months), mesotrione/isoxaflutole/clopyralid (check wheat,
  sunflower and soybean intervals), fomesafen is not used in corn. Carryover **into**
  corn: sulfentrazone/chlorimuron from soybeans (minor), imazamox from Clearfield
  wheat (10-month interval), sorghum herbicides generally safe.
- **Rootworm:** first-year corn after any other crop essentially avoids it in this
  region.

## Breakeven (dryland, priced 2026-10-31; totals from the cost table above)

| Yield (bu/ac) | Direct cost ~$385/ac → price needed ($/bu) | Total cost ~$525/ac → price needed ($/bu) |
|---|---|---|
| 70 (adverse) | $5.50 | $7.50 |
| 90 | $4.28 | $5.83 |
| 110 (base) | $3.50 | $4.77 |
| 130 | $2.96 | $4.04 |
| 150 (favorable) | $2.57 | $3.50 |

- At the 2026 RMA harvest price (~$4.75) and a Wichita harvest basis of −40 ¢, cash
  ≈ $4.35: dryland corn covers direct costs at ~89 bu/ac and total costs at ~121
  bu/ac. With KFMA's SC non-irrigated average of ~112 bu/ac, dryland corn roughly
  covers all costs in an average year only when basis and price cooperate — the margin
  is thin and the variance is high.
- Revenue needed per acre: ~$385 (direct) / ~$525 (total). Replace with K-State 2026
  SC corn budget figures when obtained.

## Comparison with grain sorghum (dryland) and decision rules for this farm

**Sourced comparison points:**
- K-State 2026 SC grain sorghum budget (2025-11-01): $4.56/bu, 110–120 bu/ac, total
  expense $2.72/bu, returns above direct expenses $277–295/ac, above total specified
  expenses $202/ac.
- K-State 2025 NC Kansas comparison: sorghum direct costs ≈$106/ac lower than corn at
  the same 120 bu/ac (mainly seed and fertilizer).
- KFMA SC 2025: non-irrigated corn ~112 bu/ac vs sorghum ~88 bu/ac (all farms, not
  paired fields).
- K-State O'Brien analysis: break-even "cutoff" corn yields where crop choice flips of
  roughly 64–100 bu/ac depending on price scenario; sorghum shows less yield variation.
- Norwood (western KS, 1990s): corn pays in good years, loses in dry years; no-till
  essential for dryland corn in dry years.

**Decision rules (draft; orchestrator-planner to apply per field each February):**
1. **Field eligibility:** dryland corn only on fields with ≥8 in plant-available water
   capacity in the top 4 ft and ≥6 in actually stored at planting (Mesonet/probe).
   Otherwise sorghum.
2. **Yield-ratio test:** plant corn where expected corn yield ≥ 1.25 × expected sorghum
   yield **and** expected corn yield ≥ 110 bu/ac. Rationale: corn direct costs run
   ~$100–140/ac above sorghum and corn price per bushel is usually within ±5% of
   sorghum locally; at 110 corn vs 88 sorghum (KFMA SC) the gross margins are close,
   so the ratio must be higher or the price spread wider to justify the variance.
3. **Price-spread test:** if new-crop corn minus new-crop sorghum cash bid ≥ +$0.30/bu,
   tilt to corn on eligible fields; if sorghum is at a premium (export-driven years),
   go sorghum everywhere dryland.
4. **Nitrogen trigger:** compute the corn-to-N price ratio = Dec corn ($/bu) ÷
   anhydrous ($/lb N). At 2026-10-31: 4.56 ÷ 0.60 = **7.6**. Rules: ratio ≥ 8 — corn
   N program at full K-State rate; 6–8 — trim yield goal to the field's 3–5 yr average
   (drop the 105%) and keep sidedress contingent; **< 6 — shift the marginal corn
   fields to soybeans** (soybeans need no N; 2026 SC budget 47 bu × $10.53 =
   $495/ac income) or sorghum (same N logic but ~30% lower N and seed cost). Also
   shift to soybeans whenever the soybean:corn new-crop price ratio exceeds ~2.5.
5. **Spring moisture trigger:** if April 1 Palmer Drought Severity Index for Kansas
   Division 8 (south central) is ≤ −2 and the 0–4 ft profile is below 60% of capacity,
   cap dryland corn at the best 20% of fields or zero.
6. **Rotation guard:** no corn after corn; no corn after sorghum unless the ratio test
   clears by a wide margin; prefer corn after soybeans or wheat.
7. **Logistics guard:** total corn acres (dryland + irrigated) must not exceed what the
   farm can harvest, dry/aerate and haul in ~15 working days without custom help, or
   budget custom harvest/hauling in the plan.

## Crop insurance notes

- Products: Revenue Protection (RP) with harvest price option, enterprise units
  across dryland corn (separate irrigated/non-irrigated enterprise units are
  allowed), 70–80% coverage typical in Kansas; SCO/ECO stacking available.
- 2026 prices: projected $4.62/bu (Feb average of Dec futures); harvest price ≈$4.75
  national (DTN 2026-10-30), Kansas table $4.78 (Rain and Hail) — official RMA release
  2026-11-05. 2027 projected price is set in February 2027.
- APH: a new corn grower uses county T-yields (Sedgwick non-irrigated T-yield **verify**)
  at reduced percentage until 4 years of records exist; yield exclusion/YA options
  matter after 2022–23 drought years.
- Final planting date and late-planting period for Sedgwick County corn **verify**
  (likely late May / early June with 25-day late period).
- Prevented-planting and replant provisions matter in wet Aprils; aflatoxin requires
  pre-harvest/pre-storage sampling by an adjuster-approved method.
- Premium estimate $15–28/ac dryland at 75–80% RP (**verify** with agent; depends on
  APH).

## Open items / gaps (for the next review)

1. Obtain and transcribe the K-State 2026 (and 2027 when posted) "Corn Cost-Return
   Budget in South Central Kansas" (dated 2025-11-01) — every cost line marked verify.
2. Pull NASS Quick Stats Sedgwick County corn yields 2010–2025 by practice.
3. Read MF2586 (2024) previous-crop credit table and S/Zn thresholds.
4. Confirm status/ownership of the Colwich ethanol plant and collect weekly bids.
5. Collect a current local aflatoxin discount schedule and drying/shrink schedule.
6. RMA Sedgwick County corn T-yields, final planting dates, premium quotes.
7. Kansas Custom Rates 2026 figures for anhydrous application, spraying, harvest.
8. K-State "Chemical Weed Control for Field Crops 2026" program tables and costs.

## Change log
- 2026-10-31 — Initial version. Written from K-State, NASS, RMA, DTN and industry
  search summaries; direct document fetch blocked. Costs and county yields flagged
  verify. Decision rules are drafts pending operator review.
