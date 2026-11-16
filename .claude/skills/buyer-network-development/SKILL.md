---
name: buyer-network-development
description: Build and work the buyer pipeline for non-commodity crops and products: target list by segment, spec and price sheets, outreach and sampling schedule, letters of intent before planting, contact logging and quarterly account review.
---

# Buyer network development

Run monthly year-round, weekly from January to May when planting decisions depend on
pre-sold volume. Owner: market-analyst agent.

## Steps
1. **Targets.** For each product with a vertical plan, pull buyer names from the
   competitor analyses, From the Land of Kansas directories, Wichita business
   directories and referrals. Add to `data/processed/buyers.csv` with segment, products of
   interest and source. Aim for 60–100 named targets before January.
2. **Materials.** Confirm each product has a spec sheet, price sheet, story sheet, sample
   packaging and the food-safety documents buyers ask for; list gaps to the compliance
   officer and the vertical owner.
3. **Outreach plan.** Schedule visits, sample drops and calls by segment; chefs and bakers
   mid-afternoon Tuesday to Thursday; grocers through program introductions; processors
   and contract buyers in winter before planting.
4. **Log.** Every interaction goes in `buyer_contacts.csv` the same day with outcome, next
   step and hours.
5. **Convert.** Move accounts from sampled to trial to letter of intent or contract; record
   price, volume and terms in `buyers.csv`.
6. **Pre-sold check.** Before each planting decision, compute pre-sold share per product
   (LOI plus contract plus tested-channel estimate over expected output) and report to
   the orchestrator against the 60% rule.
7. **Quarterly review.** Revenue, margin and hours per account; drop or reprice the bottom
   quartile; set growth targets for the top; update each vertical's `assumptions.csv`
   with realized prices and volumes.
8. **Write.** `plans/<season>/buyer-pipeline.md` with the pipeline table, pre-sold share
   and the month's plan.

## Output
Updated CSVs, the pipeline file, and a short summary: targets, conversions this period,
pre-sold share by product, blockers.
