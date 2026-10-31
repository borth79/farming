# Data sources catalog

| Domain | Source | What | Cadence | Access |
|---|---|---|---|---|
| Fuel | EIA Weekly Retail Diesel, Midwest PADD 2 | retail diesel $/gal | weekly | EIA API v2 (`EIA_API_KEY`), series `PET.EMD_EPD2D_PTE_R20_DPG.W` |
| Fuel | EIA WTI spot Cushing | $/bbl | daily/weekly | EIA API series `PET.RWTC.W` |
| Energy | EIA Henry Hub spot | $/MMBtu | daily/weekly | EIA API series `NG.RNGWHHD.W` |
| Propane | EIA Conway / Mont Belvieu propane spot | $/gal | weekly | EIA API |
| Fertilizer | USDA AMS Illinois Production Cost Report | retail anhydrous, urea, UAN, DAP, MAP, potash | weekly | report text/PDF; parse or hand-enter |
| Fertilizer | DTN retail fertilizer survey | national retail averages | weekly | web article; hand-enter |
| Fertilizer | World Bank Commodity Price Data | DAP, urea, potash, TSP monthly | monthly | spreadsheet download |
| Fertilizer | Argus / Green Markets / CRU | NOLA barge, Tampa ammonia | weekly | subscription |
| Grain | USDA WASDE, NASS Crop Progress, Grain Stocks | balance sheets, progress | monthly/weekly | public |
| Grain | CME / KC HRW wheat, corn, soybean futures | prices | daily | public delayed |
| Insurance | USDA RMA price discovery, county yields | | seasonal | public |
| Weather | Kansas Mesonet | station weather, ET, soil temp | hourly/daily | public API |
| Weather | NOAA CPC outlooks, ENSO status | seasonal | monthly/weekly | public |
| Water | Kansas DWR WIMAS water rights | rights by location | static | public web |
| Economics | K-State Farm Management Guides, KFMA | budgets, machinery costs, land values | annual | public |
| Freight | Mississippi River stages (USACE), Baltic indices | logistics | daily | public |
