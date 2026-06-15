"""Download DOSM economic indicator datasets as CSV files."""

import requests, os, time

HEADERS = {"User-Agent": "ElectionPredictionBot/1.0"}
BASE = os.path.join(os.path.dirname(__file__), "..", "data", "dosm")

DATASETS = {
    "gdp": {
        "url": "https://storage.data.gov.my/national-accounts/gdp_gni_annual_nominal.csv",
        "path": "gdp/gdp_nominal_annual.csv",
    },
    "gdp_real": {
        "url": "https://storage.data.gov.my/national-accounts/gdp_gni_annual_real.csv",
        "path": "gdp/gdp_real_annual.csv",
    },
    "unemployment": {
        "url": "https://storage.data.gov.my/labour/lfs_month.csv",
        "path": "unemployment/labour_force_monthly.csv",
    },
    "fuel_prices": {
        "url": "https://storage.data.gov.my/commodities/fuelprice.csv",
        "path": "fuel_prices/fuel_prices.csv",
    },
    "exchange_rates": {
        "url": "https://storage.data.gov.my/finsector/exchangerates.csv",
        "path": "exchange_rates/exchange_rates_monthly.csv",
    },
    "interest_rates": {
        "url": "https://storage.data.gov.my/finsector/interest_rates.csv",
        "path": "opr/interest_rates.csv",
    },
}

for key, info in DATASETS.items():
    path = os.path.join(BASE, info["path"])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print(f"[{key}] Downloading {info['url']}...")
    try:
        resp = requests.get(info["url"], timeout=30, headers=HEADERS)
        resp.raise_for_status()
        with open(path, "wb") as f:
            f.write(resp.content)
        lines = resp.text.strip().count("\n")
        print(f"  -> {path} ({lines} rows, {len(resp.content)} bytes)")
    except Exception as e:
        print(f"  FAIL: {e}")
    time.sleep(0.5)

print("\nDone!")
