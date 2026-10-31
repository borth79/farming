# Input price forecast model (overview)

Purpose: produce price distributions, not point forecasts, for each major input over
the horizons the crop plan and procurement rules need. Two sub-models share this
framework: `fertilizer-price-model.md` and `fuel-price-model.md`.

## Horizons
| Horizon | Used for |
|---|---|
| 1–3 months | procurement timing, storage fill decisions |
| 3–9 months | next-season input budget, prepay decisions |
| 9–18 months | crop-mix optimization, marketing-year planning |

## Method (staged; start simple)
1. **Baseline**: current spot price, forward curve where one exists (NYMEX ULSD, Henry
   Hub strip, CME urea swaps), and the seasonal pattern from 5+ years of history.
2. **Driver adjustment**: regress or rule-adjust for the primary driver (gas → N,
   crude and crack → diesel, index → P/K).
3. **Scenario overlay**: weight the geopolitical scenarios from
   `knowledge/geopolitics/` by their current probabilities to shift and widen the
   distribution.
4. **Output**: P10 / P50 / P90 price by month for each product, delivered to
   Sedgwick County (apply local basis from `data/processed/input_prices.csv`).

## Inputs
- `data/processed/input_prices.csv` (history and current)
- Forward curves (manual entry or fetched)
- Scenario probabilities from the weekly geopolitical scan
- Seasonal factors computed from history

## Outputs
- `plans/<season>/input-price-forecast.md` and a CSV of monthly P10/P50/P90.
- Flags when current price sits below P25 (buy signal) or above P75 (defer signal).

## Validation
Each post-harvest review compares forecast P10/P50/P90 to realized prices and records
calibration; adjust scenario weights and seasonal factors accordingly.
