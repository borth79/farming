# Produce crop economics schema

## `data/processed/produce_crop_economics.csv`
One row per crop × channel × labor rate.

| Column | Notes |
|---|---|
| crop | |
| channel | chef_direct / grocery_wholesale / market_csa |
| labor_rate_code | FAMILY / HIRED_SEASONAL |
| acres_stage1 | recommended |
| yield_lb_per_acre | marketable, base |
| price_per_lb | channel base price |
| sellthrough_pct | base |
| revenue_per_acre | |
| variable_cost_per_acre_excl_labor | seed, inputs, irrigation, packaging, freight |
| labor_hours_per_acre | |
| labor_cost_per_acre | hours × loaded rate |
| fixed_share_per_acre | land charge, insurance, storage, equipment depreciation share |
| net_per_acre | |
| net_per_labor_hour | net ÷ hours, before paying labor (shows what the enterprise earns per hour of work) |
| family_income_per_acre | at FAMILY rate: wages paid + net (what the family takes home) |
| breakeven_price_per_lb | |
| capital_crop_specific | |
| mechanizable | yes / partial / no |
| storable_months | |
| source_file | knowledge/crops/produce/<crop>.md |
| confidence | |
