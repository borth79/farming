# Free data APIs and feeds for prediction inputs

Survey as of 2026-10-31. "Free" means no payment for the access level described; most
need a free registration key. Real-time exchange prices are generally not free; delayed
or daily data is. Verify terms before building on any feed.

## Energy and fuel
| Source | Data | Cadence | Access | Notes |
|---|---|---|---|---|
| EIA Open Data API v2 | WTI, Brent, Henry Hub, PADD 2 retail diesel, propane (Conway, Mont Belvieu), distillate inventories, STEO forecasts | daily/weekly/monthly | free key | best free energy source; used by `scripts/fetch_eia_prices.py` |
| FRED (St. Louis Fed) | WTI (DCOILWTICO), Henry Hub (DHHNGSP), PPI fertilizer indices, diesel retail, global wheat/corn/soybean monthly prices (IMF series), exchange rates, interest rates | daily/monthly | free key | one API for macro, FX, rates and many commodity series |
| Alpha Vantage | WTI, Brent, natural gas, wheat, corn (monthly/weekly/daily where available) | daily | free key, rate-limited | simple JSON; useful as a cross-check |

## Fertilizer
| Source | Data | Cadence | Access | Notes |
|---|---|---|---|---|
| USDA AMS Market News (MARS API) | Illinois Production Cost Report: anhydrous, urea, UAN, DAP, MAP, potash retail; many grain and feed reports | weekly | free | nearest thing to a free fertilizer price API; confirm report slugs |
| World Bank Commodity Price Data (Pink Sheet) | urea, DAP, TSP, potash, phosphate rock monthly | monthly | free download (xlsx) | global benchmark; no live API, scheduled download |
| IMF Primary Commodity Prices | urea, DAP, potash, wheat, corn, soybeans, energy | monthly | free download / API | alternative benchmark |
| FAO / AMIS Market Monitor | fertilizer and grain market commentary | monthly | free | qualitative outlook |
| No free real-time NOLA or Tampa benchmark | — | — | — | Argus, Green Markets, CRU are paid; use Henry Hub and TTF as leading proxies, AMS retail as lagging |

## Grain and oilseed markets
| Source | Data | Cadence | Access | Notes |
|---|---|---|---|---|
| USDA NASS Quick Stats API | acreage, yield, production, prices received, crop progress, county data for Sedgwick | weekly/monthly/annual | free key | 50,000-record query limit |
| USDA AMS MARS API | cash grain bids, Kansas grain market reports, basis-relevant terminal prices | daily | free | local basis proxies |
| USDA FAS PSD API | world production, supply, distribution, trade by country | monthly | free key | competitor and buyer balance sheets |
| USDA FAS GATS / Export Sales | weekly export sales (China sorghum purchases) | weekly | free | watch China sorghum pace |
| USDA WASDE | monthly balance sheets | monthly | free (files, API via OCE) | plan anchor |
| USDA RMA price discovery | projected and harvest prices for insurance | seasonal | free (web/xls) | insurance decisions |
| CME Group | KC HRW wheat, corn, soybeans, ULSD, natural gas futures | real-time | paid; delayed quotes free on web | no free official API |
| Yahoo Finance via `yfinance` (unofficial) | delayed futures KE=F, ZW=F, ZC=F, ZS=F, HO=F, CL=F, NG=F | 15-min delayed, daily history | free, unofficial, may break | acceptable for daily models, not for execution |
| Barchart / Nasdaq Data Link | limited free tiers | varies | free tier | check limits |

## Weather and climate
| Source | Data | Cadence | Access | Notes |
|---|---|---|---|---|
| Kansas Mesonet | station observations, soil temperature, ET, GDD for Sedgwick-area stations | hourly/daily | free (web data access) | primary local weather source |
| NOAA NWS API (api.weather.gov) | forecasts, alerts, observations | hourly | free, no key | severe weather and hail alerts |
| NOAA CPC | seasonal outlooks, ENSO status and probabilities | weekly/monthly | free files | drives weather scenarios |
| Open-Meteo | forecast, historical reanalysis, seasonal ensemble (ECMWF-based), soil moisture | hourly/daily | free, no key for non-commercial; paid for commercial | easiest programmatic weather; check license for commercial farm use |
| NOAA NCEI Climate Data Online | historical station records (Wichita, Hutchinson) | daily | free token | climate normals |
| USDA Drought Monitor | weekly drought classes | weekly | free (GIS services) | drought scenarios |
| NOAA NHC | hurricane advisories | as needed | free | Gulf logistics risk |

## Water and logistics
| Source | Data | Cadence | Access | Notes |
|---|---|---|---|---|
| Kansas DWR WIMAS | water rights by location | static | free web | irrigation question |
| USGS Water Services API | river stages, groundwater levels | real-time | free | Mississippi stage via NWS/USGS |
| USACE / NWS AHPS | river gauge forecasts | daily | free | barge logistics |
| WTO Strait of Hormuz Trade Tracker | transit and trade flow estimates | weekly | free web | chokepoint monitoring |
| MarineTraffic / Kpler | vessel tracking | real-time | paid; limited free web views | transit counts |

## Geopolitics, conflict, policy
| Source | Data | Cadence | Access | Notes |
|---|---|---|---|---|
| GDELT DOC 2.0 API | global news article search, volume timelines, tone | 15-min | free, no key | used by `scripts/fetch_gdelt_events.py`; velocity signal |
| GDELT Events / GKG | coded events (CAMEO) | 15-min | free (BigQuery or raw files) | heavier; structured events |
| ACLED | conflict and protest events | weekly | free with registration (limits) | structured conflict data |
| UCDP API | armed conflict events | monthly/annual | free token | slower, authoritative |
| ReliefWeb API | humanitarian reports | daily | free | context on crises |
| Federal Register API | US rules: tariffs, EPA labels, RFS, sanctions notices | daily | free, no key | domestic policy triggers |
| OFAC SDN list | sanctions designations | as issued | free download | sanctions triggers |
| USTR / MOFCOM announcements | tariff actions | as issued | free web / RSS | China and Mexico triggers |
| Google News RSS | keyword feeds | continuous | free | lightweight alerts |
| Polymarket / Kalshi public APIs | crowd probabilities on ceasefires, strait reopening, tariffs | real-time | free read | probability sanity check, not a forecast |
| CISA advisories | cyber threats to critical infrastructure | as issued | free | C11 channel |
| USDA APHIS | animal and plant disease detections | as issued | free | C12 channel |

## Gaps where free data is weak
- Real-time fertilizer benchmarks (NOLA, Tampa): paid only. Use gas prices as a leading
  proxy and AMS retail as a weekly lagging check; collect local co-op quotes by hand.
- Real-time futures: delayed data only. Fine for daily models.
- Vessel-level chokepoint tracking: paid. Use WTO tracker and news velocity.
- Local Kansas diesel rack (Group 3): paid (OPIS). Use EIA Midwest retail plus supplier
  invoices to calibrate basis.

## Keys to obtain (all free)
EIA, FRED, NASS Quick Stats, FAS PSD, NCEI token, ACLED registration, UCDP token,
Alpha Vantage. Store them as environment variables; never commit them.
