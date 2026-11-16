---
title: Labor rates used in project models
domain: finance
last_reviewed: 2026-11-16
review_cadence: annual (January, after wage rule updates)
confidence: medium (minimum wage and H-2A rates from official releases via search 2026-11-16; loaded-cost multipliers are estimates to verify with the CPA)
sources:
  - Kansas minimum wage follows the federal $7.25/hr (K.S.A. 44-1203); no state increase enacted as of 2026 — verify
  - US Department of Labor H-2A Adverse Effect Wage Rates 2026–2027: Kansas skill level 1 $13.86/hr, level 2 $18.39–19.71/hr (effective Aug 2026)
  - USDA NASS Farm Labor: Northern Plains hired worker average $19.78/hr (Jul 2024), $20.48/hr (Oct 2024)
  - BLS OEWS Wichita MSA: farmworkers and laborers, crop, median ~$15–17/hr (verify current table)
  - IRS Publication 51 (Agricultural Employer's Tax Guide): FICA exemption for children under 18 employed by a parent's sole proprietorship or parents-only partnership; FUTA exemption under 21 — verify applicability to an LLC
used_by_agents:
  - finance-controller
  - orchestrator-planner
  - agronomist
  - market-analyst
---

# Labor rates used in project models

## Standard rates
| Rate code | Who | Wage $/hr | Loaded $/hr | Basis |
|---|---|---|---|---|
| FAMILY | family members working in the produce or vertical enterprises | 10.00 | 11.00 | project owner's direction: slightly above the $7.25 minimum; loading ~10% for payroll tax where applicable (family exemptions may reduce this) |
| HIRED_SEASONAL | local seasonal hire | 15.00 | 18.00 | Wichita-area farm labor wages; ~20% loading for payroll tax, workers' comp, insurance |
| HIRED_SKILLED | equipment operator, manager | 22.00 | 27.00 | regional skilled farm wage |
| H2A | H-2A guest worker, Kansas level 1 | 13.86 | 20.00+ | AEWR plus housing, transport, fees; loading is large |
| OWNER_OPP | owner or Tony's time | 25.00 | 25.00 | opportunity cost for management time; not a cash cost |

## Rules
1. Every produce and vertical model states which rate code each labor line uses.
2. Family labor at FAMILY rate is a real cash cost in the model, not free labor; the
   family member is paid.
3. Models report profitability twice where labor matters: at FAMILY rate and at
   HIRED_SEASONAL rate, so the plan shows what happens if family labor is unavailable.
4. Hours per acre or per pound come from the crop file; rate × hours gives the labor
   line. Do not bury labor in a blended cost.
5. Compliance: Kansas and federal child labor rules for minors in agriculture (hours,
   hazardous tasks, school hours); family exemptions are narrower under an LLC than a
   sole proprietorship; check with the CPA before relying on FICA exemptions.

## Change log
- 2026-11-16: created.
