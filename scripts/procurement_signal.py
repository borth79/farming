#!/usr/bin/env python3
"""Weekly procurement signal: BUY-SHOCK / BUY-TRANCHE / HOLD / DEFER per input.

Inputs:
  data/processed/input_prices.csv            price history (schema: data/reference/input-price-schema.md)
  data/processed/scenario_probabilities.csv  live scenario probabilities and impacts
  data/reference/procurement-config.csv      requirements, storage caps, tranches, drivers
  data/processed/input_purchases.csv         purchases to date (optional)

Logic (see knowledge/inputs/procurement-early-warning-system.md):
  price position   = percentile of latest price vs trailing 3 years; 30-day momentum
  driver pressure  = 30-day move in the input's driver series (natural_gas, wti)
  scenario pressure= sum(probability x impact) over scenarios touching the input
  retail lag       = benchmark move not yet in the local (sedgwick_local) quote
Appends a row per input to data/processed/procurement_signals.csv and prints the calls.

Usage: python3 scripts/procurement_signal.py [--as-of YYYY-MM-DD] [--month M] [--no-log]
"""
import argparse
import csv
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRICES = ROOT / "data" / "processed" / "input_prices.csv"
SCEN = ROOT / "data" / "processed" / "scenario_probabilities.csv"
CONFIG = ROOT / "data" / "reference" / "procurement-config.csv"
PURCH = ROOT / "data" / "processed" / "input_purchases.csv"
LOG = ROOT / "data" / "processed" / "procurement_signals.csv"

# benchmark location preference per input (first found wins); local quote location
BENCH = {
    "anhydrous": ["illinois_retail", "tampa", "nola"], "urea": ["nola", "illinois_retail"],
    "uan32": ["illinois_retail", "nola"], "dap": ["nola", "illinois_retail"], "potash": ["nola", "illinois_retail"],
    "diesel_offroad": ["padd2_retail"], "diesel_retail": ["padd2_retail"], "propane": ["conway"],
    "natural_gas": ["henry_hub"], "wti": ["cushing"],
}
LOCAL = "sedgwick_local"
# thresholds (starting values; calibrate at quarterly review)
T = dict(momentum_shock=8.0, driver_shock=15.0, scenario_shock=12.0, retail_lag=10.0,
         pct_low=25.0, pct_high=75.0, pct_shock=75.0)


def load_prices():
    series = defaultdict(list)  # (product, location) -> [(date, price)]
    if not PRICES.exists():
        return series
    with PRICES.open(newline="") as f:
        for r in csv.DictReader(f):
            try:
                series[(r["product"], r["location"])].append((datetime.fromisoformat(r["date"]).date(), float(r["price"])))
            except (ValueError, KeyError):
                continue
    for k in series:
        series[k].sort()
    return series


def pick(series, product, as_of):
    for loc in BENCH.get(product, []):
        s = [p for p in series.get((product, loc), []) if p[0] <= as_of]
        if s:
            return loc, s
    return None, []


def latest(s, as_of, lag_days=0):
    cutoff = as_of - timedelta(days=lag_days)
    pts = [p for p in s if p[0] <= cutoff]
    return pts[-1][1] if pts else None


def percentile(s, value, as_of, years=3):
    hist = [p[1] for p in s if as_of - timedelta(days=365 * years) <= p[0] <= as_of]
    if len(hist) < 10 or value is None:
        return None
    return 100.0 * sum(1 for h in hist if h <= value) / len(hist)


def pct_change(s, as_of, days=30):
    now, then = latest(s, as_of), latest(s, as_of, days)
    if now is None or then in (None, 0):
        return None
    return 100.0 * (now - then) / then


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--as-of", default=date.today().isoformat())
    ap.add_argument("--month", type=int, default=None, help="override current month for seasonal window")
    ap.add_argument("--no-log", action="store_true")
    a = ap.parse_args()
    as_of = datetime.fromisoformat(a.as_of).date()
    month = a.month or as_of.month

    series = load_prices()
    scen = list(csv.DictReader(SCEN.open(newline=""))) if SCEN.exists() else []
    config = list(csv.DictReader(CONFIG.open(newline="")))
    bought = defaultdict(float)
    if PURCH.exists():
        for r in csv.DictReader(PURCH.open(newline="")):
            try:
                bought[r["product"]] += float(r["quantity"])
            except (ValueError, KeyError):
                pass

    rows = []
    print(f"procurement signals as of {as_of} (month {month})")
    print(f"{'input':15}{'call':13}{'price':>9}{'pct3y':>7}{'mom30':>8}{'driver':>8}{'scen':>7}{'lag':>7}  reason")
    for c in config:
        inp = c["input"]
        loc, s = pick(series, inp, as_of)
        price = latest(s, as_of)
        pct = percentile(s, price, as_of)
        mom = pct_change(s, as_of)
        # driver pressure
        driver_moves = []
        for d in filter(None, c["drivers"].split(";")):
            _, ds = pick(series, d, as_of)
            m = pct_change(ds, as_of)
            if m is not None:
                driver_moves.append(m)
        driver = max(driver_moves) if driver_moves else None
        # scenario pressure
        scen_p = 0.0
        for r in scen:
            if inp in r["inputs_affected"].split(";"):
                try:
                    scen_p += float(r["probability_6mo"]) * float(r["impact_pct"])
                except ValueError:
                    pass
        # retail lag: benchmark move vs local quote move
        local = [p for p in series.get((inp, LOCAL), []) if p[0] <= as_of]
        lag = None
        if local and mom is not None:
            lm = pct_change(local, as_of)
            lag = mom - lm if lm is not None else mom
        windows = {int(m) for m in c["seasonal_window_months"].split(",") if m.strip()}
        in_window = month in windows

        reasons, call = [], "HOLD"
        shock_votes = 0
        if mom is not None and mom >= T["momentum_shock"]:
            shock_votes += 1; reasons.append(f"benchmark +{mom:.0f}%/30d")
        if driver is not None and driver >= T["driver_shock"]:
            shock_votes += 1; reasons.append(f"driver +{driver:.0f}%/30d")
        if scen_p >= T["scenario_shock"]:
            shock_votes += 1; reasons.append(f"scenario pressure {scen_p:.0f}%")
        if lag is not None and lag >= T["retail_lag"]:
            shock_votes += 1; reasons.append(f"retail lagging benchmark by {lag:.0f}%")
        if shock_votes >= 2:
            call = "BUY-SHOCK"
        elif pct is not None and pct >= T["pct_high"] and (mom is not None and mom < 0) and scen_p < T["scenario_shock"] / 2:
            call = "DEFER"; reasons.append(f"price {pct:.0f}th pct and easing")
        elif in_window or (pct is not None and pct <= T["pct_low"]):
            call = "BUY-TRANCHE"; reasons.append("seasonal window" if in_window else f"price {pct:.0f}th pct")
        if price is None:
            reasons.append("no price history: log benchmark and local quotes")

        req = float(c["annual_requirement"] or 0)
        remaining = max(req - bought[inp], 0)
        cap_storage = float(c["on_farm_storage_capacity"] or 0) + float(c["contracted_storage"] or 0)
        cap_prepaid = req * float(c["max_prepaid_pct"] or 100) / 100 - bought[inp]
        if call == "BUY-SHOCK":
            qty = max(0.0, min(remaining, cap_storage if cap_storage else remaining, cap_prepaid))
        elif call == "BUY-TRANCHE":
            qty = max(0.0, min(remaining, req * float(c["default_tranche_pct"] or 0) / 100, cap_storage if cap_storage else remaining, cap_prepaid))
        else:
            qty = 0.0
        if req == 0:
            reasons.append("requirement not set in procurement-config.csv")

        fmt = lambda v, w=7, d=0: (f"{v:>{w}.{d}f}" if v is not None else f"{'n/a':>{w}}")
        print(f"{inp:15}{call:13}{fmt(price, 9, 2)}{fmt(pct)}{fmt(mom, 8, 1)}{fmt(driver, 8, 1)}{fmt(scen_p)}{fmt(lag)}  {'; '.join(reasons)}")
        rows.append([as_of.isoformat(), inp, call, price, None if pct is None else round(pct, 1), None if mom is None else round(mom, 1),
                     None if driver is None else round(driver, 1), round(scen_p, 1), None if lag is None else round(lag, 1),
                     round(qty, 1), c["unit"], "; ".join(reasons), "", ""])
    if not a.no_log:
        with LOG.open("a", newline="") as f:
            csv.writer(f).writerows(rows)
        print(f"\nlogged {len(rows)} rows to {LOG}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
