---
title: Aaron's business with the trust farm as direct supplier
domain: verticals
last_reviewed: 2026-11-23
review_cadence: each time a supply price, contract term or product plan changes
confidence: low-medium (structure is standard; dollar figures come from data/processed/finished_products.csv, which rests on search-summary prices marked verify)
sources:
  - data/processed/finished_products.csv (146 products, uplift after buying crop at market value)
  - models/supply_agreement.py → data/processed/aaron_business_options.csv
  - knowledge/operations/family-trust-constraints.md (supply-agreement structure)
  - knowledge/crops/specialty/RANKING.md; knowledge/verticals/SUMMARY.md
used_by_agents:
  - finance-controller
  - compliance-officer
  - market-analyst
  - orchestrator-planner
---

# Aaron's business with the trust farm as direct supplier

## The model
- **The trust grows; it never runs the business.** The trust farm, managed by Tony, grows
  a crop to specification and sells it under a written supply agreement.
- **Aaron owns the business.** Aaron's company buys the crop directly from the trust,
  makes and sells the finished goods, owns the equipment, licenses, brand, buyers, debt and
  risk, and keeps the profit. No elevator, co-op, broker or other middleman sits between
  the field and the product.
- **The trust must come out ahead.** On every acre committed, the trust earns at least
  what its best common crop would have earned there, plus a margin. In this analysis the
  floor is soybeans' net over direct costs ($159/acre) plus 15%, or **$183/acre**. That is
  above wheat ($105), corn ($94) and sorghum ($79).
- **Direct sale saves money for both sides.** Skipping the elevator avoids basis
  discounts, hauling and handling, assumed at $25/acre here and split equally.

## How the trust is paid (pick one per crop in the agreement)
| Option | How it works | Trust risk | Aaron risk | Best for |
|---|---|---|---|---|
| A. Acreage contract | Aaron pays a fixed $/acre (at or above the floor) for the crop on named acres, whatever the yield | none on price or yield | carries both | specialty crops with no public price (Turkey Red, popcorn, berries) |
| B. Market plus premium | price = local cash bid on delivery day + agreed premium for variety, cleanliness and identity preservation, with a $/acre floor | yield risk only | price risk | crops with a public price (wheat, rye, corn, soybeans, alfalfa) |
| C. Cost plus | Aaron pays the trust's documented growing cost + a fixed margin per acre | almost none | carries price and yield | perennials, where establishment cost is large |
Recommended default: option A for specialty crops, option B with a floor for commodity
crops sold direct. The floor is reviewed every year against the common-crop benchmark.

## What the agreement must cover
Acres and fields; variety or hybrid and who supplies seed; growing practices and herbicide
restrictions (plant-backs, allergen and gluten segregation); quality specs and testing;
harvest, cleaning, storage and delivery (who does each, at whose cost); price option and
payment dates; what happens to off-spec or surplus grain (trust may sell it to the
elevator); term and renewal; who owns any improvement on trust land (default: none, or
Aaron's under a separate lease with removal rights); insurance and liability (Aaron's
business carries product liability); a market-rate review so the trustee can show
beneficiaries the price is fair; Tony's approval and the trustee's signature.

## Results: products where both sides win
All 146 products run through `models/supply_agreement.py`. 73 products not rated skip
leave Aaron a profit with the trust at or above $183/acre. Grouped into business
concepts that share equipment:

| Concept | Products | Acres from the trust | Trust earns per year (vs common crops) | Aaron's business net per year | With Aaron's own wages | Starting capital (Aaron) | Notes |
|---|---|---|---|---|---|---|---|
| 1. Kansas stone mill | Turkey Red flour, Turkey Red wheat berries, rye flour, cornmeal and grits, heirloom bagged beans | ~39 | ~$7,100 (vs ~$6,200) | ~$71,000 | ~$81,000 | ~$110–125k (flour mill line from the wheat-flour plan plus extras) | biggest upside; the earlier flour-only model was marginal, so this needs a full model with fixed costs before money moves |
| 2. Seed and feed bagging | custom cover-crop mixes, rye food-plot seed, deer corn, wildlife grain blend, pollinator native seed mixes | ~105 | ~$19,200 (vs ~$16,700) | ~$53,000 | ~$60,000 | ~$25–35k (used cleaner, bagger, scale) | best return on capital; mostly tractor and machine work, fits Tony's equipment calendar; seed registration with KDA |
| 3. Berry products | blackberry u-pick and pints, elderberry syrup | ~3.3 | ~$12,500 (vs ~$500) | ~$61,000 | ~$67,000 | ~$18k plus planting | perennial on trust land; u-pick puts the public on trust land, so pre-picked sales or an off-trust site may be required; establishment cost under option C |
| 4. Popcorn | holiday gift tins, kettle corn, heirloom kernels | ~4 | ~$700 (vs ~$650) | ~$32,000 | ~$40,000 | ~$29k | small acres, seasonal, weekend market labor |
| 5. Alfalfa pellets | 40-lb pellets via a custom pelleter | ~20 | ~$5,000 (vs ~$3,200) | ~$23,000 | ~$25,000 | ~$5k | requires alfalfa in the rotation; trust earns more on those acres than with soybeans |

Reading:
- Concepts 1 and 2 can run together: they share storage, cleaning, bagging and delivery,
  and together use about 140 trust acres. Combined, about $124,000 a year of business net
  for Aaron at market ceiling, and about $26,000 a year to the trust on those acres versus
  about $23,000 from common crops.
- The trust's gain per acre is modest on annual crops (about $25 above soybeans) but it
  gets a committed buyer and, under option A, no price risk. On perennials the trust's net
  is much higher, but so is its establishment commitment.
- These are market-ceiling figures. Year 1 will be a fraction of them; the vertical
  business plans assume 25–50% sell-through in year 1.

## Rules
1. Every supply agreement is in writing, approved by Tony, signed by the trustee, and
   priced at or above the floor with the benchmark documented.
2. Aaron's business owns all processing equipment and buildings, off trust land by default.
3. The trust never extends credit, guarantees a loan, or takes equity in Aaron's business.
4. Surplus or off-spec crop goes back to the commodity market at the trust's choice.
5. The floor and premiums are reviewed every year; if the business cannot pay the floor,
   the acres return to common crops.

## Open items
- Aaron's role, background and interest in which concept; how much capital and time Aaron
  can commit.
- Full financial model for concept 1 (mill) including fixed costs, sell-through ramp and
  the Turkey Red premium; reconcile with `knowledge/verticals/wheat-flour/`.
- Trustee's view on supply agreements, perennials and any on-farm storage Aaron might lease.
- Attorney review of a template supply agreement.

## Change log
- 2026-11-23: created.
