#!/usr/bin/env python3
"""Fetch weekly EIA price series relevant to farm input costs and append to
data/processed/input_prices.csv. Raw responses are saved under data/raw/eia/<date>/.

Requires the EIA_API_KEY environment variable (free key from https://www.eia.gov/opendata/).
Usage: python3 scripts/fetch_eia_prices.py [--weeks N]
"""
import csv
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed" / "input_prices.csv"
RAW_DIR = ROOT / "data" / "raw" / "eia" / date.today().isoformat()

# series_id -> (product, location, unit)
SERIES = {
    "PET.EMD_EPD2D_PTE_R20_DPG.W": ("diesel_retail", "padd2_retail", "usd_per_gal"),
    "PET.RWTC.W": ("wti", "cushing", "usd_per_bbl"),
    "NG.RNGWHHD.W": ("natural_gas", "henry_hub", "usd_per_mmbtu"),
}

API = "https://api.eia.gov/v2/seriesid/{sid}"


def fetch(series_id: str, api_key: str, length: int) -> dict:
    params = urllib.parse.urlencode({"api_key": api_key, "length": length, "sort[0][column]": "period", "sort[0][direction]": "desc"})
    with urllib.request.urlopen(f"{API.format(sid=series_id)}?{params}", timeout=60) as r:
        return json.load(r)


def existing_keys() -> set:
    if not PROCESSED.exists():
        return set()
    with PROCESSED.open() as f:
        return {(row["date"], row["product"], row["location"], row["source"]) for row in csv.DictReader(f)}


def main() -> int:
    api_key = os.environ.get("EIA_API_KEY")
    if not api_key:
        print("EIA_API_KEY not set; see data/reference/data-sources.md", file=sys.stderr)
        return 2
    weeks = 104
    if "--weeks" in sys.argv:
        weeks = int(sys.argv[sys.argv.index("--weeks") + 1])

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    seen = existing_keys()
    new_rows = []
    for sid, (product, location, unit) in SERIES.items():
        data = fetch(sid, api_key, weeks)
        (RAW_DIR / f"{sid}.json").write_text(json.dumps(data))
        for rec in data.get("response", {}).get("data", []):
            period, value = rec.get("period"), rec.get("value")
            if value is None:
                continue
            key = (period, product, location, "eia")
            if key in seen:
                continue
            seen.add(key)
            new_rows.append([period, product, location, unit, value, "eia", sid, ""])

    write_header = not PROCESSED.exists() or PROCESSED.stat().st_size == 0
    with PROCESSED.open("a", newline="") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(["date", "product", "location", "unit", "price", "source", "series_id", "note"])
        w.writerows(sorted(new_rows))
    print(f"appended {len(new_rows)} rows to {PROCESSED}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
