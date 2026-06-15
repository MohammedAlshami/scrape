"""
Fetch Malaysia inflation data from DOSM Open Data API and save as static JSON.

Run: python scrape/dosm_data.py
"""

import json, csv
import requests
import os

API_URL = "https://api.data.gov.my/data-catalogue?id=cpi_annual_inflation"
OUTPUT_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "public", "data", "inflation.json")
OUTPUT_CSV = os.path.join(os.path.dirname(__file__), "..", "data", "dosm", "inflation", "inflation.csv")

ELECTION_TERMS = [
    {"id": "ge10", "label": "GE10", "years": [1999, 2000, 2001, 2002, 2003], "period": "1999 \u2013 2003"},
    {"id": "ge11", "label": "GE11", "years": [2004, 2005, 2006, 2007], "period": "2004 \u2013 2007"},
    {"id": "ge12", "label": "GE12", "years": [2008, 2009, 2010, 2011, 2012], "period": "2008 \u2013 2012"},
    {"id": "ge13", "label": "GE13", "years": [2013, 2014, 2015, 2016, 2017], "period": "2013 \u2013 2017"},
    {"id": "ge14", "label": "GE14", "years": [2018, 2019, 2020, 2021], "period": "2018 \u2013 2021"},
    {"id": "ge15", "label": "GE15", "years": [2022, 2023, 2024, 2025], "period": "2022 \u2013 present"},
]


def fetch():
    resp = requests.get(API_URL, timeout=15)
    resp.raise_for_status()
    raw = resp.json()

    all_data = []
    for entry in raw:
        if entry.get("division") != "overall":
            continue
        year = int(entry["date"][:4])
        if year < 1999:
            continue
        all_data.append({
            "year": year,
            "inflation": round(entry["inflation"], 1),
        })

    all_data.sort(key=lambda x: x["year"])

    out = {"data": all_data, "terms": ELECTION_TERMS}

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"Saved {len(all_data)} years to {OUTPUT_JSON}")

    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    with open(OUTPUT_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "division", "inflation"])
        for entry in raw:
            w.writerow([entry["date"], entry["division"], entry["inflation"]])
    print(f"Saved {len(raw)} rows to {OUTPUT_CSV}")
    return out


if __name__ == "__main__":
    fetch()
