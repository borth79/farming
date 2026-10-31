#!/usr/bin/env python3
"""Build a multi-sheet Excel financial model for a vertical from its assumptions.csv.

Usage:
  python3 scripts/build_vertical_model.py knowledge/verticals/<vertical>
  python3 scripts/build_vertical_model.py --all

Reads <folder>/assumptions.csv (schema: knowledge/verticals/assumptions-schema.md) and
writes <folder>/<vertical>-financial-model.xlsx with sheets: Assumptions, Capital,
Production, Unit economics, Cash flow, Breakeven, Grain comparison.
All formulas are computed in Python and written as values plus a formula-free layout so
the sheet opens anywhere; the Assumptions sheet is the audit trail back to the CSV.
"""
import csv
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
YEARS = 5
SCENARIOS = ["base", "adverse", "favorable"]
HDR = Font(bold=True)
FILL = PatternFill("solid", fgColor="DDEBF7")


def num(x, default=None):
    if x is None or str(x).strip() == "":
        return default
    return float(str(x).replace(",", "").replace("$", ""))


def load(folder: Path):
    rows = []
    with (folder / "assumptions.csv").open(newline="") as f:
        for r in csv.DictReader(f):
            r = {k.strip(): (v.strip() if isinstance(v, str) else v) for k, v in r.items()}
            base = num(r.get("value_base"))
            r["_v"] = {
                "base": base,
                "adverse": num(r.get("value_adverse"), base),
                "favorable": num(r.get("value_favorable"), base),
            }
            r["_stage"] = int(num(r.get("stage"), 1) or 1)
            r["_year"] = int(num(r.get("year_start"), 1) or 1)
            rows.append(r)
    return rows


def get(rows, section, item, scen, default=None):
    for r in rows:
        if r["section"] == section and r["item"] == item:
            v = r["_v"][scen]
            return default if v is None else v
    return default


def by_year(rows, section, item, scen, default):
    """Return a 1..YEARS list; rows with year_start fill forward."""
    vals = [None] * (YEARS + 1)
    for r in rows:
        if r["section"] == section and r["item"] == item:
            y = min(max(r["_year"], 1), YEARS)
            vals[y] = r["_v"][scen]
    out, cur = [None], default
    for y in range(1, YEARS + 1):
        if vals[y] is not None:
            cur = vals[y]
        out.append(cur)
    return out


def stage_for_year(rows, scen):
    """Stage active in each year from scenario/production rows named stage_year_N; default stage 1."""
    stages = [None]
    cur = 1
    for y in range(1, YEARS + 1):
        s = get(rows, "production", f"stage_year_{y}", scen)
        if s is not None:
            cur = int(s)
        stages.append(cur)
    return stages


def model(rows, scen):
    acres = by_year(rows, "production", "acres", scen, 0)
    ypa = get(rows, "production", "yield_per_acre", scen, 0)
    unit_lb = get(rows, "production", "yield_unit_lb", scen, 1)
    conv = get(rows, "production", "conversion_pct", scen, 100) / 100
    byp = get(rows, "production", "byproduct_pct", scen, 0) / 100
    p_prod = get(rows, "price", "product_price_per_lb", scen, 0)
    p_byp = get(rows, "price", "byproduct_price_per_lb", scen, 0)
    p_grain = get(rows, "price", "grain_price_per_lb", scen, 0)
    sales_pct = by_year(rows, "volume", "sales_pct_of_output", scen, 100)
    disc = get(rows, "financing", "discount_rate_pct", scen, 8) / 100
    loan_share = get(rows, "financing", "loan_share_pct", scen, 0) / 100
    loan_rate = get(rows, "financing", "loan_rate_pct", scen, 8) / 100
    loan_term = int(get(rows, "financing", "loan_term_years", scen, 7))
    dep_years = get(rows, "financing", "depreciation_years", scen, 10)
    stages = stage_for_year(rows, scen)

    cap_rows = [r for r in rows if r["section"] == "capital"]
    fixed_rows = [r for r in rows if r["section"] == "operating_fixed"]
    var_rows = [r for r in rows if r["section"] == "operating_variable"]

    out = {"years": [], "capex_items": cap_rows}
    cum_capex = 0.0
    stage_bought = set()
    cum_cash = 0.0
    npv = 0.0
    loan_bal = 0.0
    for y in range(1, YEARS + 1):
        st = stages[y]
        capex = 0.0
        for s in range(1, st + 1):
            if s not in stage_bought:
                capex += sum((r["_v"][scen] or 0) for r in cap_rows if r["_stage"] == s)
                stage_bought.add(s)
        cum_capex += capex
        raw_lb = acres[y] * ypa * unit_lb
        prod_lb = raw_lb * conv
        byp_lb = raw_lb * byp
        sold_lb = prod_lb * sales_pct[y] / 100
        revenue = sold_lb * p_prod + byp_lb * p_byp
        grain_value = raw_lb * p_grain
        fixed = sum((r["_v"][scen] or 0) for r in fixed_rows if r["_stage"] <= st and r["_year"] <= y)
        var_per_lb = sum((r["_v"][scen] or 0) for r in var_rows if r["_stage"] <= st and r["_year"] <= y)
        variable = var_per_lb * prod_lb
        ebitda = revenue - grain_value - fixed - variable
        dep = cum_capex / dep_years if dep_years else 0
        new_loan = capex * loan_share
        loan_bal += new_loan
        interest = loan_bal * loan_rate
        principal = (loan_bal / loan_term) if loan_bal > 0 else 0
        loan_bal = max(loan_bal - principal, 0)
        cash = ebitda - capex + new_loan - interest - principal
        cum_cash += cash
        npv += cash / ((1 + disc) ** y)
        out["years"].append(dict(year=y, stage=st, acres=acres[y], raw_lb=raw_lb, prod_lb=prod_lb,
                                 byp_lb=byp_lb, sales_pct=sales_pct[y], sold_lb=sold_lb, revenue=revenue,
                                 grain_value=grain_value, fixed=fixed, variable=variable, var_per_lb=var_per_lb,
                                 ebitda=ebitda, capex=capex, dep=dep, interest=interest, principal=principal,
                                 cash=cash, cum_cash=cum_cash, ebit=ebitda - dep))
    out["npv"] = npv
    out["payback_year"] = next((d["year"] for d in out["years"] if d["cum_cash"] >= 0), None)
    # breakeven at full stage-1 scale, year 1 cost structure
    y1 = out["years"][0]
    contrib_per_lb = p_prod - (y1["var_per_lb"]) - (p_grain / conv if conv else 0) + (byp * p_byp / conv if conv else 0)
    out["contrib_per_lb"] = contrib_per_lb
    out["breakeven_lb"] = (y1["fixed"] + (cum_capex / dep_years if dep_years else 0)) / contrib_per_lb if contrib_per_lb > 0 else None
    out["breakeven_acres"] = out["breakeven_lb"] / (ypa * unit_lb * conv) if out["breakeven_lb"] and ypa else None
    out["price_floor_per_lb"] = (y1["var_per_lb"] + p_grain / conv) if conv else None
    return out


def write_sheet(ws, header, rows, widths=None):
    ws.append(header)
    for c in ws[1]:
        c.font = HDR
        c.fill = FILL
    for r in rows:
        ws.append(r)
    for i, _ in enumerate(header, 1):
        ws.column_dimensions[get_column_letter(i)].width = (widths[i - 1] if widths else 16)


def build(folder: Path):
    rows = load(folder)
    name = folder.name
    wb = Workbook()
    ws = wb.active
    ws.title = "Assumptions"
    write_sheet(ws, ["section", "item", "base", "adverse", "favorable", "unit", "stage", "year_start", "source", "note"],
                [[r["section"], r["item"], r["_v"]["base"], r["_v"]["adverse"], r["_v"]["favorable"], r.get("unit", ""),
                  r.get("stage", ""), r.get("year_start", ""), r.get("source", ""), r.get("note", "")] for r in rows],
                [16, 30, 12, 12, 12, 14, 7, 10, 50, 40])

    results = {s: model(rows, s) for s in SCENARIOS}

    ws = wb.create_sheet("Capital")
    write_sheet(ws, ["item", "stage", "base", "adverse", "favorable", "unit", "source"],
                [[r["item"], r["_stage"], r["_v"]["base"], r["_v"]["adverse"], r["_v"]["favorable"], r.get("unit", ""), r.get("source", "")]
                 for r in results["base"]["capex_items"]], [36, 7, 12, 12, 12, 10, 50])
    for s in SCENARIOS:
        tot = sum((r["_v"][s] or 0) for r in results[s]["capex_items"])
        ws.append([f"total ({s})", "", tot])

    ws = wb.create_sheet("Production")
    hdr = ["scenario", "year", "stage", "acres", "raw lb", "product lb", "byproduct lb", "sales %", "sold lb"]
    body = [[s, d["year"], d["stage"], d["acres"], round(d["raw_lb"]), round(d["prod_lb"]), round(d["byp_lb"]), d["sales_pct"], round(d["sold_lb"])]
            for s in SCENARIOS for d in results[s]["years"]]
    write_sheet(ws, hdr, body)

    ws = wb.create_sheet("Unit economics")
    body = []
    for s in SCENARIOS:
        r = results[s]
        body.append([s, get(rows, "price", "product_price_per_lb", s), r["years"][0]["var_per_lb"],
                     get(rows, "price", "grain_price_per_lb", s), r["price_floor_per_lb"], r["contrib_per_lb"]])
    write_sheet(ws, ["scenario", "price $/lb", "variable cost $/lb product", "grain cost $/lb raw", "price floor $/lb (var + grain)", "contribution $/lb"], body, [12, 12, 24, 20, 28, 18])

    ws = wb.create_sheet("Cash flow")
    hdr = ["scenario", "year", "stage", "revenue", "grain opportunity cost", "fixed", "variable", "EBITDA", "depreciation", "EBIT", "capex", "interest", "principal", "net cash", "cumulative cash"]
    body = [[s, d["year"], d["stage"], round(d["revenue"]), round(d["grain_value"]), round(d["fixed"]), round(d["variable"]), round(d["ebitda"]),
             round(d["dep"]), round(d["ebit"]), round(d["capex"]), round(d["interest"]), round(d["principal"]), round(d["cash"]), round(d["cum_cash"])]
            for s in SCENARIOS for d in results[s]["years"]]
    write_sheet(ws, hdr, body, [12, 6, 6] + [16] * 12)
    ws.append([])
    for s in SCENARIOS:
        ws.append([f"NPV ({s})", round(results[s]["npv"]), "", f"payback year ({s})", results[s]["payback_year"] or "beyond 5"])

    ws = wb.create_sheet("Breakeven")
    body = [[s, results[s]["contrib_per_lb"], round(results[s]["breakeven_lb"]) if results[s]["breakeven_lb"] else "n/a",
             round(results[s]["breakeven_acres"], 1) if results[s]["breakeven_acres"] else "n/a"] for s in SCENARIOS]
    write_sheet(ws, ["scenario", "contribution $/lb product", "breakeven lb product / yr (fixed + depreciation)", "breakeven acres"], body, [12, 24, 40, 16])

    ws = wb.create_sheet("Grain comparison")
    body = []
    for s in SCENARIOS:
        for d in results[s]["years"]:
            body.append([s, d["year"], d["acres"], round(d["grain_value"]), round(d["ebitda"] + d["grain_value"]),
                         round(d["ebitda"]), round(d["ebitda"] / d["acres"]) if d["acres"] else 0])
    write_sheet(ws, ["scenario", "year", "acres", "value as grain", "vertical gross margin before grain cost", "added margin over grain", "added margin per acre"], body, [12, 6, 8, 16, 32, 22, 20])

    out = folder / f"{name}-financial-model.xlsx"
    wb.save(out)
    print(f"wrote {out}")
    for s in SCENARIOS:
        r = results[s]
        print(f"  {s:10} NPV {r['npv']:>12,.0f}  payback yr {r['payback_year']}  breakeven acres {r['breakeven_acres'] if r['breakeven_acres'] is None else round(r['breakeven_acres'],1)}")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--all":
        folders = [p for p in (ROOT / "knowledge" / "verticals").iterdir() if p.is_dir() and (p / "assumptions.csv").exists()]
    else:
        folders = [Path(a) for a in args]
    for f in folders:
        build(f.resolve())
    return 0


if __name__ == "__main__":
    sys.exit(main())
