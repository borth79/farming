#!/usr/bin/env python3
"""Trust-supply / Aaron-business split for every finished product.

Model: the trust farm grows the crop and sells it directly to Aaron's business under a
supply agreement (no elevator or broker). The trust must earn at least its best common
crop's net per acre plus a margin. Aaron's business pays the crop's market value plus any
premium needed to meet that floor, and keeps the remaining processing margin.

Inputs: data/processed/finished_products.csv (uplift = margin after buying crop at market value).
Output: data/processed/aaron_business_options.csv and a printed ranking.

Usage: python3 models/supply_agreement.py [--benchmark 159] [--margin-pct 15] [--middleman-saving 25]
  benchmark         best common-crop raw net $/acre the trust would otherwise earn (soybeans 159)
  margin-pct        extra the trust must earn above benchmark
  middleman-saving  $/acre of elevator basis, hauling and handling avoided by selling direct;
                    split 50/50 between trust and Aaron
"""
import argparse, csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/processed/finished_products.csv"
OUT = ROOT / "data/processed/aaron_business_options.csv"
EXCLUDE = ("honey", "colony", "plug", "workshop")
PERENNIAL = "perennial_fruit_nut"

def num(x):
    try: return float(str(x).replace(",", "").replace("$", "").strip())
    except (TypeError, ValueError): return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--benchmark", type=float, default=159.0)
    ap.add_argument("--margin-pct", type=float, default=15.0)
    ap.add_argument("--middleman-saving", type=float, default=25.0)
    a = ap.parse_args()
    floor = a.benchmark * (1 + a.margin_pct / 100)
    rows = list(csv.DictReader(SRC.open(newline="")))
    out = []
    for r in rows:
        if r["product"] == "raw" or any(s in (r["crop"] + r["product"]).lower() for s in EXCLUDE):
            continue
        raw, up = num(r["raw_net_per_acre"]), num(r["uplift_per_acre_over_raw"])
        if raw is None or up is None:
            continue
        acres = num(r["max_acres_by_market"]) or 0.0
        labor = num(r["labor_cost_per_acre_equiv"]) or 0.0
        share = a.middleman_saving / 2
        trust_before_premium = raw + share
        premium = max(0.0, floor - trust_before_premium)
        trust_net = trust_before_premium + premium
        aaron_net = up + share - premium              # business profit per acre after paying trust
        aaron_income = aaron_net + labor              # profit plus wages if Aaron does the labor
        out.append(dict(
            crop=r["crop"], product=r["product"], crop_group=r["crop_group"], verdict_research=r["verdict"],
            trust_raw_net=round(raw), trust_premium=round(premium), trust_net_per_acre=round(trust_net),
            trust_beats_common_crop="yes" if trust_net >= floor - 0.5 else "no",
            aaron_business_net_per_acre=round(aaron_net), aaron_labor_wages_per_acre=round(labor),
            aaron_income_per_acre=round(aaron_income), market_ceiling_acres=acres,
            aaron_business_net_per_year=round(aaron_net * acres), aaron_income_per_year=round(aaron_income * acres),
            trust_net_per_year=round(trust_net * acres), stage1_capital=r["stage1_capital"],
            perennial="yes" if r["crop_group"] == PERENNIAL else "no",
            regulatory=r["regulatory"], confidence=r["confidence"], source_file=r["source_file"]))
    out.sort(key=lambda d: -d["aaron_business_net_per_year"])
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    print(f"trust floor ${floor:.0f}/acre (benchmark {a.benchmark} + {a.margin_pct}%); middleman saving ${a.middleman_saving}/acre split 50/50")
    print(f"wrote {OUT} ({len(out)} products)\n")
    viable = [d for d in out if d["aaron_business_net_per_acre"] > 0 and not d["verdict_research"].lower().startswith("skip")]
    print(f"{'product':46}{'trust $/ac':>11}{'premium':>9}{'Aaron $/ac':>11}{'acres':>7}{'Aaron $/yr':>11}{'w/ wages':>10}{'capital':>9}  per")
    for d in viable[:25]:
        print(f"{(d['crop'][:16]+' | '+d['product'])[:45]:46}{d['trust_net_per_acre']:>11,}{d['trust_premium']:>9,}{d['aaron_business_net_per_acre']:>11,}{d['market_ceiling_acres']:>7}{d['aaron_business_net_per_year']:>11,}{d['aaron_income_per_year']:>10,}{str(d['stage1_capital'])[:8]:>9}  {d['perennial']}")
    print(f"\n{len(viable)} non-skip products leave Aaron a profit with the trust at or above its floor")

if __name__ == "__main__":
    main()
