# Soil test and field trial schemas

## `data/processed/soil_tests.csv`
One row per sample (composite or grid point).

| Column | Notes |
|---|---|
| field_id | matches farm-profile field table |
| sample_id | lab or farm sample code; grid point id if gridded |
| sample_date | YYYY-MM-DD |
| depth_in | `0-6` or `0-24` |
| lab | lab name |
| ph_water | 1:1 water pH |
| buffer_ph | for lime requirement |
| om_pct | organic matter %, LOI |
| p_ppm | Bray P1 or Mehlich-3, state in `p_method` |
| p_method | `bray1` or `mehlich3` |
| k_ppm | ammonium acetate |
| no3_n_lb_acre | profile nitrate-N, 0–24 in, lb/acre |
| so4_s_ppm | sulfate-S |
| cl_lb_acre | chloride, 0–24 in |
| zn_ppm | DTPA zinc |
| cec | meq/100 g |
| notes | free text (zone, landscape position, previous crop) |

## `data/processed/field_trials.csv`
| Column | Notes |
|---|---|
| season | e.g. 2027 |
| field_id | |
| trial_id | |
| practice_or_product | what is being tested |
| treatment | description |
| control | description |
| reps | number of paired strips |
| yield_treatment | bu/acre or lb/acre |
| yield_control | |
| cost_treatment_per_acre | |
| cost_control_per_acre | |
| net_effect_per_acre | computed |
| notes | weather, problems, confidence |
