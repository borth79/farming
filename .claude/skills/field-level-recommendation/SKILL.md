---
name: field-level-recommendation
description: Turn soil tests and field history into per-field crop, variety, population and fertility recommendations with input-reduction opportunities; run the soil test recommendation script and produce the field plan table.
---

# Field-level recommendation

Run after soil test results are logged and before the seasonal plan fixes crops and
input purchases. Owner: agronomist agent.

## Steps
1. **Check data.** Confirm every field has a soil test under three years old in
   `data/processed/soil_tests.csv` and a row in `knowledge/operations/field-history.md`.
   List fields that need sampling.
2. **Run the recommender.** `python3 scripts/soil_test_recommend.py --season <year>`
   produces `plans/<season>/soil-recommendations.csv` with N, P2O5, K2O, lime, S, Cl and
   Zn per field for each candidate crop, using current prices for cost per acre.
3. **Rank crops per field.** For each field, score crops in scope on soil fit, rotation
   position, herbicide carryover, water holding, expected yield from the crop file's yield
   table, and expected margin at current prices. Exclude disqualified crops with reasons.
4. **Pick genetics and population.** From the crop files and the latest K-State
   performance tests, choose variety or hybrid and seeding rate per field.
5. **Apply input-reduction practices.** Walk the ranked list in
   `knowledge/agronomy/yield-enhancement-and-input-efficiency.md`; for each field record
   which practices apply, the expected effect and the input saved.
6. **Propose trials.** Any unproven product or practice gets a strip-trial design.
7. **Write the field plan.** `plans/<season>/field-plan.md` with the per-field table and
   `plans/<season>/field-plan.csv` for the spreadsheet, columns: field, acres, soil
   series, crop, variety_or_hybrid, population, N_lb, P2O5_lb, K2O_lb, lime_t, S_lb, Cl_lb,
   Zn_lb, input_cost_per_acre, expected_yield, expected_margin, practices, trials, notes.
8. **Hand off.** Notify the orchestrator and input-cost analyst; the field plan sets the
   input requirement for procurement.

## Output
The field plan files and a short summary: fields needing sampling, total input cost,
input reductions achieved versus a flat-rate program, trials proposed.
