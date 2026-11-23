# Finished products schema

## `data/processed/finished_products.csv`
One row per crop × finished product (include a `raw` row per crop for the baseline).

| Column | Notes |
|---|---|
| crop | |
| product | `raw` for the baseline sale |
| crop_group | specialty_grain / oilseed_industrial / pulse / perennial_fruit_nut / seed_specialty / core_crop |
| raw_net_per_acre | net from selling the raw crop, USD/acre |
| product_units_per_acre | units of finished product from one acre of crop |
| unit | lb, bottle, bag, jar, etc. |
| price_per_unit | base, USD |
| channel | wholesale / retail / online / chef / institutional / contract |
| variable_cost_per_unit | excluding raw crop and labor |
| labor_hours_per_acre_equiv | hours to process one acre's output |
| labor_cost_per_acre_equiv | at FAMILY rate |
| stage1_capital | USD |
| fixed_cost_per_year | USD |
| net_per_acre_equiv | whole-chain net per acre: raw_net_per_acre + uplift_per_acre_over_raw (farm net from growing plus processing LLC margin) |
| uplift_per_acre_over_raw | processing LLC margin per acre of crop processed: product revenue − variable − labor − raw crop bought at market value − fixed share |
| max_acres_by_market | acres the reachable market can absorb |
| regulatory | license/permit needed |
| verdict | pursue / test / skip |
| confidence | high / medium / low |
| source_file | knowledge/crops/specialty/<crop>.md |


Clarified 2026-11-23: uplift is the processing margin after buying the crop at market value; net_per_acre_equiv = raw_net + uplift. Earlier wording double-counted the raw crop.
