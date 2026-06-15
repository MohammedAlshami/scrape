"""Download KLSE (KLCI) historical index data from Yahoo Finance."""

import os, csv, time
from datetime import datetime

BASE = os.path.join(os.path.dirname(__file__), "..", "data", "klse")
os.makedirs(BASE, exist_ok=True)

# KLSE index: ^KLSE on Yahoo Finance
# We can use the CSV download from Yahoo Finance's historical data
# URL pattern: https://query1.finance.yahoo.com/v7/finance/download/%5EKLSE
# Or use the API: https://query1.finance.yahoo.com/v8/finance/chart/%5EKLSE

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Try Yahoo Finance download (period1 = 1998-01-01 in epoch seconds)
period1 = int(datetime(1998, 1, 1).timestamp())
period2 = int(datetime.now().timestamp())
url = f"https://query1.finance.yahoo.com/v7/finance/download/%5EKLSE?period1={period1}&period2={period2}&interval=1d&events=history"

print(f"Fetching KLSE data from Yahoo Finance...")
resp = requests.get(url, headers=HEADERS, timeout=30)

if resp.status_code == 200:
    path = os.path.join(BASE, "klse_daily.csv")
    with open(path, "wb") as f:
        f.write(resp.content)
    lines = resp.text.strip().count("\n")
    print(f"Saved: {path} ({lines} rows)")
else:
    print(f"Yahoo Finance failed ({resp.status_code}), trying Investing.com via API...")
    # Fallback: try a simpler approach
    print("Could not fetch KLSE data. Try installing yfinance: pip install yfinance")

print("Done!")
