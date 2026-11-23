---
title: Flax (fit check)
domain: crops
last_reviewed: 2026-11-23
review_cadence: every 3 years unless a Southern Plains buyer appears
confidence: low (no Kansas yield data or buyer found; price is the North Dakota 2025 NASS figure; freight, yields and product prices are estimates)
sources:
  - USDA NASS State Agriculture Overview, North Dakota (pulled 2026-09-24): 2025 flaxseed $12.60/bu; ~165,000 ac harvested; 3.96 M bu (≈24 bu/ac); $51.48 M; 2026 planted 185,000 ac, harvested 181,000 (2026-08-12 snapshot)
  - USDA NASS Agricultural Prices (Jan–Oct 2026 releases, esmis): U.S. flaxseed ~$12.00/bu Feb 2026, $12.20 Jan 2026 (ycharts summary)
  - Texas A&M, Keys to Profitable Flax Production: Texas commercial flax 1938–1949 peak, South Texas winter flax, cold-tolerant varieties later moved north (historical)
  - NDSU Extension A1038, Flax Production in North Dakota (agronomy reference)
  - Selina Wamucii (aggregator, low quality): U.S. flaxseed oil wholesale $2.76–3.37/lb 2026
  - knowledge/crops/grain-sorghum.md; knowledge/verticals/sunflower-oil-and-birdseed/business-plan.md
used_by_agents:
  - agronomist
  - market-analyst
  - finance-controller
---

# Flax

## 1. Fit for this farm
**Verdict: poor fit. Do not grow.**

- **Climate:** flax is a cool-season crop. Spring flax sown in March here flowers in June heat,
  which cuts yield and oil quality. Winter flax was historically a South Texas crop, and winter
  hardiness at 37.7 N is unproven for modern varieties (**verify**). Kansas grew flax a century
  ago (eastern Kansas linseed era, **verify**) but has had no meaningful acreage in modern NASS
  data (not retrieved).
- **Rotation:** spring flax occupies March to July. That blocks full-season sorghum and soybeans and
  only allows a late double crop. It competes poorly with wheat for the cool-season slot.
- **Equipment:** drill, combine (tough stems wrap; sharp sickle needed) and sprayer are owned.
  Flax straw is hard to manage in no-till.
- **Weeds:** a poor competitor. A limited label (e.g. MCPA, bromoxynil, some grass products;
  **verify**).
- **Market:** all buyers and crushers are in the northern Plains (ND, MN, SD) and Canada, about
  700+ miles away.
- **Trust and labor:** no issue beyond those of any crop.

## 2. Agronomy summary (reference only)
- **Seeding:** 40–50 lb/ac, early spring, ≤1 in deep.
- **Fertility:** 40–60 lb N.
- **Diseases:** pasmo, fusarium wilt, rust.
- **Harvest:** straight-combine or swath at maturity. Dry to ≤9%.
- **Benchmark:** ND averaged ~24 bu/ac in 2025 under its ideal climate. Southern Kansas would be
  well below (estimate 8–22 bu).

## 3. Yield and raw-crop economics
| Case | Yield (bu/ac; lb) | Net price ($/bu after freight) | Revenue ($/ac) | Direct cost ($/ac) | Net over direct ($/ac) |
|---|---|---|---|---|---|
| Adverse | 8 (450) | 10.00 | 80 | 130 | -50 |
| Base | 15 (840) | 10.50 | 158 | 140 | **18** |
| Favorable | 22 (1,230) | 11.00 | 242 | 145 | 97 |

- **Price:** ND $12.60/bu (2025) less an estimated $2.10/bu freight to a northern crusher
  (**verify**; no Kansas buyer found).
- **Direct cost (estimate):**
  - seed: $25
  - N: $25
  - herbicide: $25
  - fuel and repairs: $45
  - misc. and interest: $10
  - insurance: none assumed (RMA flax is available in northern states; Kansas **verify**)
- **Versus sorghum (~$79/ac over direct, `grain-sorghum.md`):** flax trails by ~$60/ac at base and
  also costs the full-season summer crop.

## 4. Raw-crop market
No buyer within reach. Northern crushers and food-flax handlers buy at ND/MN delivery points. Spot
pricing tracks Canadian flax (Saskatchewan) and EU and China demand. The volume ceiling is
effectively zero for this farm.

## 5. Finished products
Structure, labor rates and the schema note match the other files: `net_per_acre_equiv` already
charges seed at market value. The main finding is that **every flax food product can be made from
purchased ND flax at ~$0.25/lb delivered**. Growing it here adds risk and no product advantage.

### 5a. Milled flaxseed
- **Process:** clean, cold-mill (hammer or burr), nitrogen-flush pouch.
- **Capital:** ~$20,000.
- **Labor:** 31 hr/ac-equiv ($341).
- **Yield:** 840 lb → 780 lb milled.
- **Price:** $2.25/lb wholesale (estimate, **verify**; national brands such as Bob's Red Mill retail
  about $3–5/lb).
- **Margin:** net $232/ac-equiv (schema $214); about break-even at the hired rate.
- **Regulatory:** KDA food license; FDA.
- **Verdict: skip.** It's a commodity shelf item, and purchased seed works equally well.

### 5b. Cold-pressed flax oil
- **Process:** the sunflower-plan press; refrigerated distribution with a very short shelf life (high
  ALA).
- **Capital:** ~$10,000 incremental.
- **Labor:** 24 hr ($264).
- **Yield:** 840 lb → ~240 lb oil (≈30% recovery) → ~235 × 250 ml.
- **Price:** $5.00 wholesale (estimate). Bulk is ~$2.76–3.37/lb (aggregator, low quality).
- **Margin:** net $193/ac-equiv with a meal credit (schema $175); ~$25 at the hired rate.
- **Competitors:** Barlean's and Spectrum (national refrigerated brands).
- **Verdict: skip.**

### 5c. Linen fiber
- Oilseed flax straw is not linen-grade. Fiber flax needs dense seeding, pulling, retting and
  scutching, and the U.S. has only pilot-scale processing.
- **Not modelled and not in the CSV. Verdict: skip.**

| Product | Uplift per acre over raw | Stage-1 capital | Labor hr per acre-equivalent | Main channel | Regulatory | Verdict |
|---|---|---|---|---|---|---|
| Milled flaxseed, 1 lb | $214 (net $232; -$2 hired) | $20,000 | 31 | wholesale | KDA, FDA | skip |
| Cold-pressed flax oil, 250 ml | $175 (net $193; $7 hired) | $10,000 incremental | 24 | wholesale, chef | KDA, FDA, cold chain | skip |
| Linen fiber | not modelled | — | — | — | — | skip |

## 6. Risks and disqualifiers
- **Top disqualifier:** no buyer within ~700 miles.
- Climate mismatch (heat at flowering).
- It displaces the summer crop.
- Poor weed competitiveness.

## 7. Decision rules
1. Do not grow flax unless a buyer within 250 miles offers a delivered price ≥ $15/bu and a K-State
   or OSU trial shows ≥ 20 bu/ac in south-central Kansas.
2. If the LLC wants a flax SKU, buy ND or Canadian food-grade flax. Do not grow it.

## 8. Open items
- Pull NASS Quick Stats for any Kansas flax acreage since 2000.
- Check for winter flax variety trials in Oklahoma and Texas since 2015.

## Change log
- 2026-11-23: created as a fit check (oilseeds and industrial crops group).
