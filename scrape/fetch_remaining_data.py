"""Download quarterly GDP, state election data, reserves, and debt data."""

import requests, csv, os

H = {"User-Agent": "ElectionPredictionBot/1.0"}
BASE = os.path.join(os.path.dirname(__file__), "..", "data")

# === Quarterly GDP ===
print("=== Quarterly GDP ===")
for name, dsid in [("gdp_nominal_qtr", "gdp_qtr_nominal"), ("gdp_real_qtr", "gdp_qtr_real")]:
    resp = requests.get(f"https://api.data.gov.my/data-catalogue?id={dsid}", timeout=15, headers=H)
    if resp.status_code == 200:
        rows = resp.json()
        path = os.path.join(BASE, "dosm", "gdp", f"{name}.csv")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", newline="") as f:
            w = csv.writer(f)
            if rows:
                w.writerow(rows[0].keys())
                for r in rows:
                    w.writerow(r.values())
        print(f"  {name}: {len(rows)} rows saved")
    else:
        print(f"  {name}: FAIL {resp.status_code}")

# === State Election Data - Download Wikipedia pages ===
state_el = {
    "2023_Selangor_state_election": "2023_Selangor_state_election",
    "2023_Penang_state_election": "2023_Penang_state_election",
    "2023_Negeri_Sembilan_state_election": "2023_Negeri_Sembilan_state_election",
    "2023_Kedah_state_election": "2023_Kedah_state_election",
    "2023_Kelantan_state_election": "2023_Kelantan_state_election",
    "2023_Terengganu_state_election": "2023_Terengganu_state_election",
    "Results_of_the_2023_state_elections_by_constituency": "Results_of_the_2023_Malaysian_state_elections_by_constituency",
}

el_folder = os.path.join(BASE, "elections", "state_2023")
os.makedirs(el_folder, exist_ok=True)

print("\n=== State Election 2023 Pages ===")
for name, title in state_el.items():
    url = f"https://en.wikipedia.org/w/index.php?title={title}&action=raw"
    resp = requests.get(url, timeout=15, headers=H)
    if resp.status_code == 200:
        path = os.path.join(el_folder, f"{name}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {name}\n\nSource: https://en.wikipedia.org/wiki/{title}\n\n---\n\n{resp.text}")
        print(f"  {name}: {len(resp.text)} chars")
    else:
        print(f"  {name}: FAIL {resp.status_code}")

# === BNM Reserves + Debt Summary ===
reserves_folder = os.path.join(BASE, "dosm", "opr")
os.makedirs(reserves_folder, exist_ok=True)

reserves_debt = """# Malaysia Central Bank Reserves & Government Debt

Source: Wikipedia (Economy of Malaysia, Central Bank of Malaysia)

## BNM International Reserves (US$ billion)
| Date | Reserves |
|---|---|
| Dec 2004 | $66B |
| Jul 2005 | $78B |
| Dec 2007 | $101B |
| Mar 2008 | $120B |
| Dec 2010 | $107B |
| Dec 2012 | $140B |
| Dec 2014 | $116B |
| Dec 2016 | $95B |
| Dec 2018 | $101B |
| Dec 2019 | $104B |
| Dec 2020 | $108B |
| Dec 2021 | $117B |
| Dec 2022 | $115B |
| Dec 2023 | $114B |
| Dec 2024 | $116B |
| Dec 2025 | $126B |

## Government Debt (% of GDP)
| Year | Debt % | Year | Debt % |
|---|---|---|---|
| 1990 | 74.1% | 2008 | 39.4% |
| 1995 | 38.2% | 2013 | 55.7% |
| 2000 | 32.5% | 2018 | 55.6% |
| 2004 | 42.0% | 2020 | 67.7% (COVID peak) |
| 2005 | 40.8% | 2022 | 69.6% |
| 2006 | 39.7% | 2023 | 70.0% |
| 2007 | 39.3% | 2024-27 | ~70% (projected) |

## Key Fiscal Indicators (2024 est.)
- Budget balance: -4.36% of GDP
- Gross external debt: $319 billion
- Revenue: $66.44 billion
- Current account balance: +$13.1 billion (surplus)
- Credit ratings: S&P A-, Moody's A3, Fitch BBB+ (all stable)

## Implications for GE16
- Debt at 70% is high but stable (not growing rapidly)
- Reserves at $126B provide adequate buffer (~5 months of imports)
- Budget deficit at ~4-5% limits pre-election spending sprees
- Malaysia's credit rating (A-/A3) is investment grade - no imminent crisis
- Fiscal space is LIMITED compared to pre-COVID (when debt was ~55%)
"""

path = os.path.join(reserves_folder, "reserves_and_debt.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(reserves_debt)
print(f"\nSaved: reserves_and_debt.md")

print("\nAll done!")
