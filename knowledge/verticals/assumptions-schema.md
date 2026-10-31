# assumptions.csv schema

Columns (header row required, exactly these names):

| Column | Meaning |
|---|---|
| section | one of: `capital`, `operating_fixed`, `operating_variable`, `production`, `price`, `volume`, `financing`, `scenario` |
| item | short name, unique within section |
| value_base | number for the base case |
| value_adverse | number for the adverse case (blank = same as base) |
| value_favorable | number for the favorable case (blank = same as base) |
| unit | e.g. `usd`, `usd_per_lb`, `lb`, `acres`, `pct`, `years`, `hours`, `usd_per_year` |
| stage | 1, 2 or 3 (which growth stage this applies from); blank = all |
| year_start | first model year the item applies (1–5); blank = 1 |
| source | citation with date |
| note | free text |

Required items the model expects (others are optional and are carried through):

- production: `acres`, `yield_per_acre` (lb or bu), `yield_unit_lb` (lb per yield unit, e.g. 60 for wheat bu), `conversion_pct` (finished product lb per 100 lb raw), `byproduct_pct` (byproduct lb per 100 lb raw, may be 0)
- price: `product_price_per_lb`, `byproduct_price_per_lb`, `grain_price_per_lb` (opportunity cost of the raw crop)
- volume: `sales_pct_of_output` by year (use `year_start` rows: year 1, 2, 3, 4, 5) — share of output actually sold
- capital: one row per equipment or facility item with `stage`
- operating_fixed: annual fixed costs (license, insurance, facility, maintenance, marketing)
- operating_variable: per-lb finished product costs (packaging, power, labor, testing, delivery)
- financing: `discount_rate_pct`, `loan_share_pct`, `loan_rate_pct`, `loan_term_years`, `depreciation_years`
- scenario: optional qualitative rows (ignored by the model but kept for the sheet)

Model outputs (generated sheets): Assumptions, Capital, Production, Unit economics,
Cash flow (5 years × 3 scenarios), Breakeven, Grain comparison.
