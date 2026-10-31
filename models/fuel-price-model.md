# Fuel price model

## Products modeled
Dyed off-road diesel delivered to the farm; propane (Conway hub) when corn is planned.

## Structure
Farm diesel = NYMEX ULSD (or WTI + crack spread) + Group 3 basis + distributor margin
and delivery − excise tax exemption.

- **Forward curve**: NYMEX ULSD monthly futures give a market-implied P50 for 18+ months.
- **Crack spread**: model ULSD − WTI by season and inventories; widen in winter and at
  refinery maintenance.
- **Basis**: Group 3 (Wichita area) minus NYMEX, from history or OPIS; typically small
  but spikes on pipeline or refinery events.
- **Volatility**: use options-implied volatility on ULSD or historical volatility to
  build P10/P90 bands.
- **Shock overlay**: scenarios from `knowledge/geopolitics/energy-geopolitics.md`.

## Procedure
1. Pull EIA Midwest retail diesel, WTI, and (manually or by feed) ULSD futures curve.
2. Estimate farm delivered basis from the last several supplier invoices versus the
   EIA Midwest series on the same dates.
3. Project P50 from the futures curve + basis; P10/P90 from volatility; shift for
   scenario weights.
4. Multiply by the season's planned gallons (from `knowledge/inputs/diesel-and-fuel.md`
   consumption table × planned operations) to get fuel cost per acre and total, with
   bands.
5. Emit fill/contract flags per the diesel decision rules.

## Status
Specification only. `scripts/fetch_eia_prices.py` begins accumulating the EIA series.
