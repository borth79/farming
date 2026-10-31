# Input price data schema

## `data/processed/input_prices.csv`
One row per observation.

| Column | Type | Notes |
|---|---|---|
| date | YYYY-MM-DD | observation date |
| product | text | controlled list below |
| location | text | e.g. `henry_hub`, `nola`, `illinois_retail`, `padd2_retail`, `conway`, `sedgwick_local` |
| unit | text | `usd_per_short_ton`, `usd_per_gal`, `usd_per_mmbtu`, `usd_per_bbl`, `usd_per_lb_n` |
| price | number | |
| source | text | `eia`, `usda_ams`, `dtn`, `world_bank`, `supplier_quote`, `coop_quote`, `cme`, `trade_press` |
| series_id | text | provider series id where applicable |
| note | text | optional |

Controlled product list: `anhydrous`, `urea`, `uan28`, `uan32`, `ams`, `dap`, `map`,
`potash`, `diesel_offroad`, `diesel_retail`, `ulsd_futures`, `wti`, `brent`,
`natural_gas`, `propane`.

## `data/processed/input_purchases.csv`
| Column | Notes |
|---|---|
| date | purchase or contract date |
| product | from controlled list |
| quantity | numeric |
| unit | `short_ton`, `gal`, `lb_n` |
| price | per unit |
| total | quantity × price |
| supplier | |
| contract_type | `spot`, `prepay`, `forward_fixed`, `forward_capped`, `price_later` |
| delivery_window | text |
| rule_triggered | the decision rule that justified the purchase |
| season | e.g. `2027-wheat`, `2027-row-crop` |
