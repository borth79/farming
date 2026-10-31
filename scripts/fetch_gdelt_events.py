#!/usr/bin/env python3
"""Pull recent news volume and headlines for farm-relevant geopolitical topics from the
GDELT DOC 2.0 API (free, no key). Saves raw JSON under data/raw/gdelt/<date>/ and prints
a summary table for the weekly geopolitical scan.

Usage: python3 scripts/fetch_gdelt_events.py [--days 7] [--max 25]
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw" / "gdelt" / date.today().isoformat()

TOPICS = {
    "hormuz": '"Strait of Hormuz" (shipping OR tanker OR fertilizer OR urea)',
    "iran_conflict": 'Iran (strike OR ceasefire OR blockade OR sanctions)',
    "black_sea_grain": '("Black Sea" OR Odesa OR Novorossiysk) (wheat OR grain OR port)',
    "russia_fertilizer": 'Russia (fertilizer OR urea OR ammonia OR potash) (export OR sanctions)',
    "belarus_potash": 'Belarus potash',
    "china_fertilizer_export": 'China (urea OR phosphate) export (quota OR restriction OR inspection)',
    "china_sorghum_soy": 'China (sorghum OR soybean) (tariff OR purchase OR import)',
    "mexico_trade": 'Mexico (tariff OR USMCA) (corn OR wheat OR agriculture)',
    "red_sea_shipping": '("Red Sea" OR Suez OR Houthi) shipping',
    "opec": 'OPEC (output OR production OR quota)',
    "diesel_supply": 'diesel (shortage OR export ban OR refinery outage)',
    "natural_gas_europe": '(TTF OR "European gas") (price OR supply)',
    "india_urea_tender": 'India urea tender',
    "mississippi_river": '"Mississippi River" (low water OR barge OR draft)',
    "gulf_hurricane": 'hurricane ("Gulf Coast" OR Louisiana OR Texas) (refinery OR port)',
    "ag_cyber": 'cyberattack (agriculture OR grain OR cooperative OR pipeline OR rail)',
    "farm_policy": '(USDA OR EPA OR Congress) (farm bill OR "renewable fuel" OR 45Z OR tariff) farmers',
    "animal_disease": '("avian influenza" OR "African swine fever" OR "New World screwworm") (cattle OR hogs OR poultry)',
}

API = "https://api.gdeltproject.org/api/v2/doc/doc"


def query(q: str, days: int, maxrecords: int) -> dict:
    params = {"query": q, "mode": "ArtList", "format": "json", "timespan": f"{days}d",
              "maxrecords": maxrecords, "sort": "DateDesc"}
    url = f"{API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "farming-geoscan/0.1"})
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read().decode("utf-8", errors="replace")
    return json.loads(body) if body.strip().startswith("{") else {"articles": [], "raw": body[:200]}


def main() -> int:
    days = int(sys.argv[sys.argv.index("--days") + 1]) if "--days" in sys.argv else 7
    maxrecords = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 25
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print(f"{'topic':28} {'articles':>8}  latest headline")
    for topic, q in TOPICS.items():
        try:
            data = query(q, days, maxrecords)
        except Exception as e:  # network or rate limit
            print(f"{topic:28} {'ERR':>8}  {e}")
            continue
        (RAW_DIR / f"{topic}.json").write_text(json.dumps(data))
        arts = data.get("articles", [])
        latest = arts[0].get("title", "")[:80] if arts else ""
        print(f"{topic:28} {len(arts):>8}  {latest}")
        time.sleep(1.5)  # GDELT asks for modest request rates
    print(f"\nraw saved to {RAW_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
