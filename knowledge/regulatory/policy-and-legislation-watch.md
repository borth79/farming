---
title: Policy and legislation watch — federal and Kansas laws affecting output and profitability
domain: regulatory
last_reviewed: 2026-11-16
review_cadence: monthly; weekly during the Kansas session (January–May) and when Congress is in session on a farm bill
confidence: medium (status facts from search summaries dated 2026-11-16; sources conflict on the farm bill lapse; verify each item against the official record before acting)
sources:
  - farmdoc daily / Farm Policy News, "Farm Bill Expires Again as Lawmakers Continue Negotiations", 2026-10
  - Holland & Knight, "Beyond the Midterms: Congress Faces Converging Year-End Deadlines", 2026-10
  - IEDC, "Farm Bill Programs Extended Through 2026 in Legislation Ending Federal Government Shutdown", 2025-11-20
  - American Farm Bureau, "Time to Finish the Job: 2026 Farm Bill"
  - USDA farmers.gov Farm Bill updates
  - Kansas Livestock Association, "Kansas Legislature Wraps Up 2026 Session"; Renew Kansas and Kansas Grain and Feed Association 2026 session updates
  - Kansas Legislature: HB 2114 (dams and water structures, signed 2026-04-09), HB 2477 (DWR mapping and posting), HB 2558 (state water plan fund), HB 2745 (vetoed 2026-04-08), HB 2043, SCR 1616/1603 (assessed value cap), SB 235 (neonicotinoids), pesticide labeling preemption bill
  - Kansas Legislature REST API documentation (kslegislature.gov/klois/Pages/RESTianAPI.html; free key)
  - Federal Register API (federalregister.gov/developers; no key); Congress.gov API (free key); regulations.gov API (free key)
used_by_agents:
  - policy-analyst
  - compliance-officer
  - finance-controller
  - orchestrator-planner
---

# Policy and legislation watch

## Summary
Laws and rules set the farm's safety net, input costs, allowed practices, water, taxes
and market access. Most move slowly and predictably on a calendar; a few move fast and
matter a lot (tariffs, pesticide registrations, farm bill extensions). This file lists what
to watch, where it stands as of mid-November 2026, how each item reaches the farm's
profit, and the calendar and tools for keeping it current. The policy-analyst agent runs
the monthly scan; items live in `data/processed/policy_watch.csv`.

## Status snapshot (verify against official record)
| Item | Status 2026-11-16 | Effect on this farm |
|---|---|---|
| Farm bill | 2018 act's last extension ran to 30 Sep 2026; sources conflict on whether a further extension is in force; Congress back 9 Nov; year-end comprehensive bill or another extension expected | ARC/PLC, conservation, disaster, credit, research titles; uncertainty on program sign-up dates |
| Commodity safety net | 2025 reconciliation law (OBBBA) extended ARC, PLC and related commodity support through 2031 with revised reference prices (details to verify) | base-acre payments for wheat, sorghum, corn, soybeans; affects breakeven and marketing floors |
| Crop insurance | changes in the 2025 reconciliation law (premium support, SCO/ECO) to verify | coverage cost and level decisions each year |
| 45Z clean fuel production credit | status and guidance to verify | low-carbon-intensity grain premiums at ethanol and biodiesel plants; soybean oil demand |
| Renewable Fuel Standard volumes | EPA set rule for 2026–2027 to verify | corn, sorghum and soybean demand |
| Tariffs and trade | China tariff relief on US ag effective 2025-11-10 and large sorghum purchases; Mexico and USMCA review pending; Section 232/301 actions on steel and inputs | sorghum and soybean prices; machinery and parts cost; fertilizer import duties |
| EPA pesticide actions | dicamba over-the-top re-registration 2026-02-06 with temperature-based limits; atrazine label changes 2026; Endangered Species Act herbicide and insecticide strategies rolling out | herbicide programs, spray windows, costs |
| Waters of the United States | definition narrowed after Sackett; rulemaking continues | wetland determinations, basins and drainage work |
| Right to repair | FTC–Deere settlement 8 Jul 2026, 10-year order, pending court entry | diagnostics access and repair cost |
| Kansas water | HB 2114 signed 2026-04-09 amending dam and water-structure rules; HB 2477 (DWR map and posting) and HB 2558 (water plan fund to $60M) outcomes to verify; GMD2 local enhanced management area discussions | pond and basin permits; groundwater allocation if irrigated |
| Kansas property tax | HB 2745 vetoed 2026-04-08; HB 2043 enacted (scope to verify); SCR 1616/1603 proposed a 3% assessed-value cap amendment, ballot status to verify | land carrying cost; agricultural-use valuation stability |
| Kansas pesticides | House passed federal-label preemption bill; SB 235 on neonicotinoids introduced; outcomes to verify | seed treatment and label liability |
| Kansas sales and income tax | sales-tax exemptions on farm machinery and inputs; any change to agricultural exemptions | input costs |
| Kansas alcohol law | microdistillery and farm winery statutes | spirits vertical route C |
| Kansas food law | KDA licensing; cottage food provisions | flour, sorghum, produce verticals |
| Kansas corporate farming law | K.S.A. 17-5904; periodic amendment attempts | any LLC land purchase |
| Labor and immigration | H-2A rules and wage rates; enforcement | seasonal produce labor |

## How each policy area reaches profit
| Area | Transmission | Model or file it feeds |
|---|---|---|
| Commodity programs, reference prices | expected government payment per base acre; effective price floor | enterprise budgets; crop-mix optimizer |
| Crop insurance rules | premium subsidy and products available; projected price dates | insurance-selection skill; risk model |
| Biofuel policy | demand for corn, sorghum, soybean oil; low-CI premiums | commodity price scenarios; sustainability files |
| Trade and tariffs | export demand and basis; input and machinery tariffs | geopolitical scenario playbook; input price model |
| Pesticide registration and labels | which products and timings are legal; resistance management cost | weed, disease and insect files; crop budgets |
| Water law | permits for structures; allocation; produce irrigation | water-management agent; capital plan |
| Property and sales tax | fixed land cost; input cost | finance files |
| Conservation programs | cost share for terraces, basins, tunnels, cover crops | water plan; capital plan |
| Food, alcohol and labor law | licensing cost and feasibility of verticals | vertical business plans |
| Trust-related tax law | §2032A, basis, grantor rules | trust constraints file |

## Calendar
| When | What |
|---|---|
| January | Kansas session opens (through ~April/May); From the Land of Kansas enrollment; FSA ARC/PLC election window typically opens |
| Feb–Mar | crop insurance sales closing for spring crops (15 Mar); Kansas committee hearings peak; EPA spring label decisions |
| April–May | Kansas veto session and sine die; USDA planting intentions |
| June–Sep | Federal Register rulemaking (RFS, pesticide decisions, 45Z guidance); farm bill markup windows |
| 30 Sep | federal fiscal year end; farm bill and extension deadlines; wheat insurance sales closing |
| Oct–Dec | Congress year-end packages; Kansas interim committees; trade actions often announced |

## Tools and feeds
| Tool | Access | Use |
|---|---|---|
| Federal Register API | free, no key | daily rules and notices from USDA, EPA, FSA, RMA, NRCS, Treasury; `scripts/fetch_federal_register.py` |
| Congress.gov API | free key | bill status and text for farm bill, tax and trade bills |
| regulations.gov API | free key | dockets and comment periods (pesticide registrations, WOTUS, RFS) |
| Kansas Legislature REST API | free key, `Authorization: Api-Key` header, endpoints under `/api/v1/` (measures, bill status, subjects, statute sections, measure text) | track Kansas bills by subject (agriculture, water, taxation, alcoholic beverages) |
| USDA FSA and RMA program pages | free | sign-up dates, rates |
| Kansas Department of Agriculture notices | free | pesticide, water, food licensing changes |
| Trade groups' session updates (Kansas Farm Bureau, Kansas Grain and Feed, Kansas Livestock, Renew Kansas, Kansas Wheat) | free | curated weekly summaries during session |

## Decision rules
1. Every item in the watch list carries a probability of enactment, an estimated dollar
   effect per acre or per vertical, and a date; items above a set effect threshold enter
   the seasonal plan's assumptions with base, adverse and favorable cases.
2. Program deadlines (insurance sales closing, ARC/PLC election, EQIP sign-up) are
   calendar entries with a two-week warning, owned by the compliance officer.
3. A proposed rule with a comment period that affects a planned practice or vertical gets
   a short written comment through a trade association or directly.
4. No vertical business plan is finalized on a licensing assumption older than six months.
5. Policy changes that move expected revenue or cost by more than 5% on any crop trigger a
   re-run of the crop-mix optimizer.

## Open items
- Confirm farm bill status after Congress returns 9 Nov 2026 and record enacted reference
  prices and insurance changes.
- Record final 2026 Kansas session outcomes for HB 2477, HB 2558, HB 2043, SCR 1616/1603,
  SB 235 and the pesticide preemption bill.
- Obtain Kansas Legislature, Congress.gov and regulations.gov API keys.
- Verify 45Z guidance and RFS volumes.

## Change log
- 2026-11-16: created.
