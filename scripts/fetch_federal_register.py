#!/usr/bin/env python3
"""Fetch recent Federal Register documents relevant to the farm from the free Federal
Register API (no key). Saves raw JSON under data/raw/federal_register/<date>/ and prints
a summary table for the legislative scan.

Usage: python3 scripts/fetch_federal_register.py [--days 31] [--max 100]
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "federal_register" / date.today().isoformat()
API = "https://www.federalregister.gov/api/v1/documents.json"

AGENCIES = ["agriculture-department", "farm-service-agency", "risk-management-agency",
            "natural-resources-conservation-service", "agricultural-marketing-service",
            "environmental-protection-agency", "commodity-credit-corporation",
            "internal-revenue-service", "trade-representative-office-of-united-states"]
TERMS = ["farm bill", "price loss coverage", "agriculture risk coverage", "crop insurance",
         "renewable fuel standard", "clean fuel production credit", "pesticide registration",
         "dicamba", "atrazine", "waters of the united states", "tariff agricultural",
         "sorghum", "hard red winter wheat", "conservation stewardship", "environmental quality incentives",
         "H-2A", "fertilizer", "right to repair"]


def fetch(params):
    url = f"{API}?{urllib.parse.urlencode(params, doseq=True)}"
    req = urllib.request.Request(url, headers={"User-Agent": "farming-policy-scan/0.1"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=31)
    ap.add_argument("--max", type=int, default=100)
    a = ap.parse_args()
    since = (date.today() - timedelta(days=a.days)).isoformat()
    RAW.mkdir(parents=True, exist_ok=True)
    seen, out = set(), []
    for term in TERMS:
        params = {"conditions[term]": term, "conditions[publication_date][gte]": since,
                  "conditions[agencies][]": AGENCIES, "per_page": min(a.max, 100), "order": "newest",
                  "fields[]": ["document_number", "title", "type", "publication_date", "agencies", "html_url",
                               "comments_close_on", "effective_on", "abstract"]}
        try:
            data = fetch(params)
        except Exception as e:
            print(f"{term!r}: fetch failed ({e})", file=sys.stderr)
            continue
        (RAW / f"{term.replace(' ', '_')}.json").write_text(json.dumps(data))
        for d in data.get("results", []):
            if d["document_number"] in seen:
                continue
            seen.add(d["document_number"])
            d["_term"] = term
            out.append(d)
    out.sort(key=lambda d: d["publication_date"], reverse=True)
    print(f"{len(out)} documents since {since}\n")
    print(f"{'date':11}{'type':14}{'comments close':15}{'agency':28} title")
    for d in out:
        ag = (d.get("agencies") or [{}])[0].get("name", "")[:27]
        print(f"{d['publication_date']:11}{(d.get('type') or '')[:13]:14}{(d.get('comments_close_on') or ''):15}{ag:28} {d['title'][:90]}")
        print(f"{'':68}{d['html_url']}")
    print(f"\nraw saved to {RAW}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
