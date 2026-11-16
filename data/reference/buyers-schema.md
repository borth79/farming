# Buyer network schema

## `data/processed/buyers.csv`
One row per buyer organization. Contacts and interactions in `buyer_contacts.csv`.

| Column | Notes |
|---|---|
| buyer_id | B-### |
| name | organization |
| segment | restaurant / bakery / grocer / distributor / food_hub / farmers_market / csa / online / wholesale_marketplace / institution / brewer_distiller / processor_contract / pet_food / feed_garden_store / hay_buyer / other |
| city | |
| distance_miles | from farm |
| products_interest | semicolon list: flour; sorghum_flour; popped_sorghum; oil; birdseed; produce; popcorn; heritage_wheat; food_grade_sorghum; hay; grain_for_distilling; other |
| status | target / contacted / sampled / trial / repeat / contracted / lost |
| first_contact | YYYY-MM-DD |
| last_contact | YYYY-MM-DD |
| decision_maker | role |
| requirements | GAP, insurance, UPC, delivery day, pack size, certifications |
| price_terms | agreed or quoted price and unit; payment terms |
| est_annual_volume | with unit |
| est_annual_revenue_usd | |
| source | how found (From the Land of Kansas, Meet the Buyers, competitor analysis, referral) |
| notes | |

## `data/processed/buyer_contacts.csv`
| Column | Notes |
|---|---|
| date | |
| buyer_id | |
| contact_type | visit / call / email / sample_drop / delivery / event |
| product | |
| outcome | |
| next_step | |
| next_date | |
| hours_spent | for margin-per-hour review |
