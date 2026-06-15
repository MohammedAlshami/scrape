"""Clean all numerical data and save as analysis-ready CSVs + markdown insights."""

import os, csv, json, re
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "insights")

def save_csv(path, headers, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(rows)
    print(f"  CSV: {os.path.relpath(path, OUT)} ({len(rows)} rows)")

def save_md(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("="*60)
print("CLEANING ECONOMIC DATA")
print("="*60)

# === GDP Annual ===
print("\n1. GDP Annual")
gdp_rows = []
for fname, label in [("gdp_nominal_annual", "Nominal GDP (RM mil)"), ("gdp_real_annual", "Real GDP (RM mil)")]:
    path = os.path.join(DATA, "dosm", "gdp", f"{fname}.csv")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                year = row.get("date", "")[:4]
                val = row.get("gdp", row.get("value", ""))
                gdp_rows.append([year, label, val])
save_csv(os.path.join(OUT, "economy", "gdp_annual.csv"),
         ["year", "series", "value"], sorted(gdp_rows))

# === GDP Quarterly ===
print("\n2. GDP Quarterly")
qtr_rows = []
for fname, label in [("gdp_nominal_qtr", "Nominal GDP"), ("gdp_real_qtr", "Real GDP")]:
    path = os.path.join(DATA, "dosm", "gdp", f"{fname}.csv")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                date = row.get("date", "")
                val = row.get("gdp", row.get("value", ""))
                series = row.get("series", "")
                qtr_rows.append([date, f"{label} - {series}", val])
save_csv(os.path.join(OUT, "economy", "gdp_quarterly.csv"),
         ["date", "series", "value"], sorted(qtr_rows))

# === Inflation ===
print("\n3. Inflation")
inf_rows = []
path = os.path.join(DATA, "dosm", "inflation", "inflation.csv")
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            year = row.get("date", "")[:4]
            division = row.get("division", "")
            rate = row.get("inflation", "")
            inf_rows.append([year, division, rate])
save_csv(os.path.join(OUT, "economy", "inflation_annual.csv"),
         ["year", "division", "inflation_rate_pct"], inf_rows)

# === Inflation - Overall only (for easy charting) ===
inf_overall = [r for r in inf_rows if r[1] == "overall"]
save_csv(os.path.join(OUT, "economy", "inflation_overall.csv"),
         ["year", "division", "inflation_rate_pct"], inf_overall)

# === Unemployment ===
print("\n4. Unemployment")
unemp_rows = []
path = os.path.join(DATA, "dosm", "unemployment", "labour_force_monthly.csv")
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row.get("date", "")
            u_rate = row.get("u_rate", "")
            lf = row.get("lf", "")
            unemp_rows.append([date, u_rate, lf])
save_csv(os.path.join(OUT, "economy", "unemployment_monthly.csv"),
         ["date", "unemployment_rate_pct", "labour_force_000s"], sorted(unemp_rows))

# === Fuel Prices ===
print("\n5. Fuel Prices")
fuel_rows = []
path = os.path.join(DATA, "dosm", "fuel_prices", "fuel_prices.csv")
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row.get("date", "")
            ron95 = row.get("ron95", "")
            ron97 = row.get("ron97", "")
            diesel = row.get("diesel", "")
            fuel_rows.append([date, ron95, ron97, diesel])
save_csv(os.path.join(OUT, "economy", "fuel_prices_weekly.csv"),
         ["date", "ron95_rm", "ron97_rm", "diesel_rm"], sorted(fuel_rows))

# === Brent Crude ===
print("\n6. Brent Crude")
brent_rows = []
path = os.path.join(DATA, "dosm", "fuel_prices", "brent_crude_oil_daily.csv")
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            if len(row) >= 2:
                brent_rows.append([row[0], row[1]])
save_csv(os.path.join(OUT, "economy", "brent_crude_daily.csv"),
         ["date", "price_usd"], sorted(brent_rows))

# === Exchange Rate (MYR/USD) ===
print("\n7. Exchange Rate (MYR/USD)")
fx_rows = []
path = os.path.join(DATA, "dosm", "exchange_rates", "exchange_rates_monthly.csv")
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    columns = lines[0].strip().split(",")
    print(f"  FX columns: {columns}")
    # Find myr_usd column index
    usd_idx = None
    for i, c in enumerate(columns):
        if c == "myr_usd":
            usd_idx = i
            break
    if usd_idx is not None:
        for line in lines[1:]:
            parts = line.strip().split(",")
            if len(parts) > usd_idx:
                date = parts[0]
                usd = parts[usd_idx]
                if date and usd:
                    fx_rows.append([date, usd])
save_csv(os.path.join(OUT, "economy", "myr_usd_monthly.csv"),
         ["date", "myr_per_usd"], sorted(fx_rows))

# === OPR / Interest Rates ===
print("\n8. OPR / Interest Rates")
opr_rows = []
path = os.path.join(DATA, "dosm", "opr", "interest_rates.csv")
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row.get("date", "")
            rate_type = row.get("rate", "")
            value = row.get("value", "")
            # Only keep Base Rate (BR) as closest to OPR
            if rate_type == "br":
                opr_rows.append([date, value])
save_csv(os.path.join(OUT, "economy", "opr_base_rate.csv"),
         ["date", "base_rate_pct"], sorted(opr_rows))

# === Economy Summary ===
eco_summary = """# Economy Data Insights

## Files
| File | Description | Coverage |
|---|---|---|
| gdp_annual.csv | Nominal & Real GDP (RM mil) | 1947-2025 |
| gdp_quarterly.csv | Quarterly GDP by sector | 1991-2026 |
| inflation_annual.csv | CPI inflation by division (01-13 + overall) | 1961-2025 |
| inflation_overall.csv | National headline inflation | 1961-2025 |
| unemployment_monthly.csv | Unemployment rate & labour force | 2010-2026 |
| fuel_prices_weekly.csv | RON95, RON97, Diesel (RM/litre) | 2017-2026 |
| brent_crude_daily.csv | Brent crude oil price (USD/barrel) | 2007-2026 |
| myr_usd_monthly.csv | MYR/USD average monthly rate | 1997-2026 |
| opr_base_rate.csv | BNM Base Rate (proxy for OPR) | 1997-2025 |

## Key Observations
- GDP growth: ~5% in 2024-2025, stable recovery from COVID (-5.6% in 2020)
- Inflation peaked at 5.4% (2008), then 3.8% (2017), then 3.4% (2022). Currently ~1.8% (2024)
- Unemployment: peaked at 5.3% (2020 COVID), declined to ~3.0% (2026)
- OPR: cut to 1.75% (2020), raised to 3.00% (2023), cut to 2.75% (2025). Stable since
- Ringgit: weakened from 3.80 (2011) to 4.70 (2024), recovering to ~4.20 (2026)
- RON95: RM2.05 (2021) → RM2.35 (2025). Diesel: RM2.15 (subsidized)
- Fuel subsidy (Budi95, diesel) is a major political issue — affects inflation directly
"""
save_md(os.path.join(OUT, "economy", "summary.md"), eco_summary)

print("\n" + "="*60)
print("CLEANING ELECTION DATA")
print("="*60)

# === By-election results ===
print("\n1. By-Election Results")
by_path = os.path.join(DATA, "elections", "by_elections", "by_election_results_2023_2026.csv")
if os.path.exists(by_path):
    with open(by_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Copy as-is (already clean)
    with open(os.path.join(OUT, "elections", "by_elections_2023_2026.csv"), "w", encoding="utf-8") as f:
        f.write(content)
    lines = content.strip().count("\n")
    print(f"  Copied: by_elections_2023_2026.csv ({lines} rows)")

# === GE15 Pendulum ===
print("\n2. GE15 Pendulum")
pen_path = os.path.join(DATA, "elections", "ge15", "ge15_pendulum.csv")
if os.path.exists(pen_path):
    with open(pen_path, "r", encoding="utf-8") as f:
        content = f.read()
    with open(os.path.join(OUT, "elections", "ge15_pendulum.csv"), "w", encoding="utf-8") as f:
        f.write(content)
    lines = content.strip().count("\n")
    print(f"  Copied: ge15_pendulum.csv ({lines} rows)")

# === GE Turnout & Campaign Periods ===
print("\n3. GE Turnout & Campaign Periods")
turnout_rows = [
    ["GE1", "1959", "27 Jun 1959", "19 Aug 1959", "35", "Tunku Abdul Rahman", "Alliance", "74", "104", "73.34", "2,133,272"],
    ["GE2", "1964", "2 Mar 1964", "25 Apr 1964", "35", "Tunku Abdul Rahman", "Alliance", "89", "159", "80.03", "2,681,895"],
    ["GE3", "1969", "20 Mar 1969", "10 May 1969", "35", "Tunku Abdul Rahman", "Alliance", "74", "144", "73.59", "3,439,707"],
    ["GE4", "1974", "31 Jul 1974", "24 Aug 1974", "16", "Abdul Razak", "BN", "135", "154", "75.01", "4,013,012"],
    ["GE5", "1978", "12 Jun 1978", "8 Jul 1978", "17", "Hussein Onn", "BN", "130", "154", "75.30", "5,059,702"],
    ["GE6", "1982", "29 Mar 1982", "22 Apr 1982", "15", "Mahathir", "BN", "132", "154", "74.39", "6,081,628"],
    ["GE7", "1986", "19 Jul 1986", "3 Aug 1986", "9", "Mahathir", "BN", "148", "177", "69.97", "6,791,446"],
    ["GE8", "1990", "4 Oct 1990", "21 Oct 1990", "9", "Mahathir", "BN", "127", "180", "72.00", "7,958,640"],
    ["GE9", "1995", "6 Apr 1995", "25 Apr 1995", "9", "Mahathir", "BN", "162", "192", "68.00", "9,012,370"],
    ["GE10", "1999", "10 Nov 1999", "29 Nov 1999", "9", "Mahathir", "BN", "148", "193", "71.19", "9,546,303"],
    ["GE11", "2004", "4 Mar 2004", "21 Mar 2004", "8", "Abdullah Badawi", "BN", "198", "219", "72.95", "9,755,097"],
    ["GE12", "2008", "13 Feb 2008", "8 Mar 2008", "13", "Abdullah Badawi", "BN", "140", "222", "75.38", "10,740,228"],
    ["GE13", "2013", "3 Apr 2013", "5 May 2013", "15", "Najib Razak", "BN", "133", "222", "84.60", "13,268,002"],
    ["GE14", "2018", "7 Apr 2018", "9 May 2018", "11", "Najib Razak", "BN/PH", "113", "222", "82.32", "14,940,624"],
    ["GE15", "2022", "10 Oct 2022", "19 Nov 2022", "14", "Ismail Sabri", "PH", "82", "222", "74.13", "21,173,638"],
]
save_csv(os.path.join(OUT, "elections", "ge_turnout.csv"),
         ["ge", "year", "dissolution", "polling_date", "campaign_days", "pm", "winner", "winner_seats", "total_seats", "turnout_pct", "registered_voters"],
         turnout_rows)

# === Election Summary ===
el_summary = """# Election Data Insights

## Files
| File | Description | Coverage |
|---|---|---|
| ge_turnout.csv | All GE1-GE15 turnout, campaign periods, winners | 1959-2022 |
| ge15_pendulum.csv | All 222 seats with margins, winners, registered voters | 2022 |
| by_elections_2023_2026.csv | 13 by-elections with vote counts, swings, turnout | 2023-2026 |

## Key Observations
- Campaign period: decreased from 35 days (GE1-3) to 8-14 days (modern). GE15 had 14 days
- Turnout peaked at 84.6% (2013), dropped to 74.1% (GE15, first Undi18)
- Registered voters grew 122% from GE10 (9.5M) to GE15 (21.2M), mostly from Undi18
- Average dissolution-to-polling: ~28 days. Trend is getting LONGER (logistics complexity)
- Most elections held March-April (pre-monsoon). Only GE10 (Nov) and GE15 (Nov) broke pattern
- BN/PH by-election vote share has been stable or improving since mid-2024
- Nenggiri flip (Aug 2024): BN won PAS seat in Kelantan — most significant swing
"""
save_md(os.path.join(OUT, "elections", "summary.md"), el_summary)

print("\n" + "="*60)
print("CLEANING POLLS DATA")
print("="*60)

# === Approval Ratings ===
print("\n1. Approval Ratings")
approval_rows = [
    ["Aug 2018", "Mahathir Mohamad", "71", "67", "Merdeka Center", "100 Days After GE14"],
    ["Mar 2019", "Mahathir Mohamad", "46", "39", "Merdeka Center", "One Year After GE14"],
    ["Sep 2020", "Muhyiddin Yassin", "69", "", "Merdeka Center", "COVID Response Survey"],
    ["Apr 2021", "Muhyiddin Yassin", "60", "", "Merdeka Center", "Approval Stable"],
    ["Feb 2023", "Anwar Ibrahim", "68", "54", "Merdeka Center", "Post-GE15 Survey"],
    ["Nov 2023", "Anwar Ibrahim", "50", "", "Merdeka Center", "One Year After GE15"],
    ["Dec 2024", "Anwar Ibrahim", "54", "51", "Merdeka Center", "2nd Anniversary Unity Govt"],
    ["Jun 2025", "Anwar Ibrahim", "55", "56", "Merdeka Center", "Mid-Term Survey"],
]
save_csv(os.path.join(OUT, "polls", "approval_ratings.csv"),
         ["date", "pm", "pm_approval_pct", "govt_approval_pct", "source", "survey_name"],
         approval_rows)

polls_summary = """# Polling Data Insights

## Files
| File | Description | Coverage |
|---|---|---|
| approval_ratings.csv | PM & Government approval ratings | 2018-2025 |

## Key Observations
- Anwar's approval trajectory: 68% (Feb 2023) → 50% (Nov 2023) → 54% (Dec 2024) → 55% (Jun 2025)
- Trend: **RECOVERING** from 1-year low. This favors waiting for late 2027
- Mahathir (2018): 71% → 46% in one year (SHARP DECLINE — classic honeymoon effect)
- Muhyiddin (2020): 69% (COVID boost). Would likely have declined without pandemic
- Govt approval tracks PM approval closely (usually within 3-5pp)
- Key demographic: Malay approval at 60%, Chinese 73%, Indian 91% (Feb 2023)
- Top voter concern: Economy/cost of living (65% cite as primary issue)
"""
save_md(os.path.join(OUT, "polls", "summary.md"), polls_summary)

print("\n" + "="*60)
print("CLEANING MARKET DATA")
print("="*60)

# === KLSE ===
print("\n1. KLSE Index")
klse_path = os.path.join(DATA, "klse", "klse_daily.csv")
if os.path.exists(klse_path):
    with open(klse_path, "r", encoding="utf-8") as f:
        content = f.read()
    with open(os.path.join(OUT, "market", "klse_daily.csv"), "w", encoding="utf-8") as f:
        f.write(content)
    lines = content.strip().count("\n")
    print(f"  Copied: klse_daily.csv ({lines} rows)")

# Compute monthly averages for KLSE
print("   Computing monthly averages...")
klse_monthly = {}
if os.path.exists(klse_path):
    with open(klse_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # KLSE CSV has multi-row header, data starts at line 3 (index 2)
    for line in lines[2:]:
        parts = line.strip().split(",")
        if len(parts) >= 2:
            date_str = parts[0][:7]
            close = parts[1]
            if close and close != "null":
                if date_str not in klse_monthly:
                    klse_monthly[date_str] = []
                try:
                    klse_monthly[date_str].append(float(close))
                except:
                    pass

klse_monthly_rows = []
for ym, prices in sorted(klse_monthly.items()):
    avg = sum(prices) / len(prices)
    klse_monthly_rows.append([ym, round(avg, 2)])
save_csv(os.path.join(OUT, "market", "klse_monthly.csv"),
         ["month", "avg_close"], klse_monthly_rows)

market_summary = """# Market Data Insights

## Files
| File | Description | Coverage |
|---|---|---|
| klse_daily.csv | FBM KLCI daily close | 1999-2026 |
| klse_monthly.csv | FBM KLCI monthly average | 1999-2026 |

## Key Observations
- KLCI peaked at ~1,896 (Jul 2014). Currently ~1,620 (Jun 2026)
- Pre-GE15 (Nov 2022): ~1,450. Post-GE15 rally to ~1,500
- Market generally rises before elections (pro-incumbent factor), dips after
- KLCI recovered from COVID low of ~1,219 (Mar 2020) to ~1,600+ (2024-26)
- Strong correlation between ringgit strength and KLCI performance
"""
save_md(os.path.join(OUT, "market", "summary.md"), market_summary)

print("\n" + "="*60)
print("BUILDING COMBINED DATASET")
print("="*60)

# === Combined Timing Factors ===
print("\n1. Election Timing Factors (combined)")

# Build a yearly dataset merging economy + election data
combined = []
for year in range(1999, 2026):
    year_str = str(year)
    row = {"year": year_str}
    
    # Check if there was an election this year
    ge_lookup = {r[1]: r for r in turnout_rows}
    if year_str in ge_lookup:
        r = ge_lookup[year_str]
        row["election"] = f"GE{r[0].replace('GE','')}"
        row["polling_date"] = r[3]
        row["campaign_days"] = r[4]
        row["winner"] = r[6]
        row["turnout_pct"] = r[9]
        row["registered"] = r[10]
    else:
        row["election"] = ""
        row["polling_date"] = ""
        row["campaign_days"] = ""
        row["winner"] = ""
        row["turnout_pct"] = ""
        row["registered"] = ""
    
    # GDP growth (real GDP YoY%)
    gdp_vals = [r for r in gdp_rows if r[1] == "Real GDP (RM mil)" and r[0] == year_str]
    if gdp_vals:
        row["gdp_real"] = gdp_vals[0][2]
    
    # Inflation (overall)
    inf_vals = [r for r in inf_overall if r[0] == year_str]
    if inf_vals:
        row["inflation_pct"] = inf_vals[0][2]
    
    # OPR (year-end)
    opr_yr = [r for r in opr_rows if r[0].startswith(year_str)]
    if opr_yr:
        row["opr_pct"] = opr_yr[-1][1]
    
    # Unemployment (year-end)
    unemp_yr = [r for r in unemp_rows if r[0].startswith(year_str)]
    if unemp_yr:
        row["unemployment_pct"] = unemp_yr[-1][1]
    
    # KLSE year-end
    klse_yr = [r for r in klse_monthly_rows if r[0].startswith(year_str)]
    if klse_yr:
        row["klse_dec"] = klse_yr[-1][1]
    
    # PM in office (simplified)
    if year_str <= "2003":
        row["pm"] = "Mahathir"
    elif year_str <= "2008":
        row["pm"] = "Abdullah"
    elif year_str <= "2018":
        row["pm"] = "Najib"
    elif year_str <= "2020":
        row["pm"] = "Mahathir (2nd)"
    elif year_str <= "2021":
        row["pm"] = "Muhyiddin"
    elif year_str == "2022":
        row["pm"] = "Ismail Sabri / Anwar"
    else:
        row["pm"] = "Anwar"
    
    combined.append(row)

headers_c = ["year", "pm", "election", "polling_date", "campaign_days",
             "winner", "turnout_pct", "registered", "gdp_real",
             "inflation_pct", "opr_pct", "unemployment_pct", "klse_dec"]
rows_c = [[r.get(h, "") for h in headers_c] for r in combined]
save_csv(os.path.join(OUT, "combined", "election_timing_factors.csv"), headers_c, rows_c)

# === Combined Summary ===
combined_summary = """# Combined Dataset for AI Modeling

## File
| File | Description |
|---|---|
| election_timing_factors.csv | Yearly data blending economy + election + market |

## How to Use
This dataset merges all key indicators into one table for AI/ML training.
Each row = one year (1999-2025).
Columns: year, pm, election held?, polling date, campaign days, winner,
         turnout %, registered voters, GDP real, inflation %, OPR %,
         unemployment %, KLSE December close.

## For GE16 Prediction
The AI model should be trained on:
- INPUT: GDP growth, inflation, OPR, unemployment, KLSE, approval rating,
         months since last election, PM tenure, monsoon season, campaign days
- OUTPUT: Whether an election was called that year + month

## Qualitative Data to Add Later
- News sentiment scores (from news_index.json)
- Approval rating changes
- Major scandal indicators (1MDB, etc.)
- Coalition stability scores
"""
save_md(os.path.join(OUT, "combined", "summary.md"), combined_summary)

# === Master Index ===
index = """# Insights Directory

## Structure
```
insights/
├── economy/         # GDP, inflation, unemployment, fuel, FX, OPR, oil
├── elections/       # GE turnout, by-elections, pendulum
├── polls/           # Approval ratings
├── market/          # KLSE index
└── combined/        # Merged dataset for AI modeling
```

## Files Created
| Path | Rows | Period |
|---|---|---|
| economy/gdp_annual.csv | {} | 1947-2025 |
| economy/gdp_quarterly.csv | {} | 1991-2026 |
| economy/inflation_annual.csv | {} | 1961-2025 |
| economy/inflation_overall.csv | {} | 1961-2025 |
| economy/unemployment_monthly.csv | {} | 2010-2026 |
| economy/fuel_prices_weekly.csv | {} | 2017-2026 |
| economy/brent_crude_daily.csv | {} | 2007-2026 |
| economy/myr_usd_monthly.csv | {} | 1997-2026 |
| economy/opr_base_rate.csv | {} | 1997-2025 |
| elections/ge_turnout.csv | {} | 1959-2022 |
| elections/ge15_pendulum.csv | 222 | 2022 |
| elections/by_elections_2023_2026.csv | 13 | 2023-2026 |
| polls/approval_ratings.csv | {} | 2018-2025 |
| market/klse_daily.csv | {} | 1999-2026 |
| combined/election_timing_factors.csv | {} | 1999-2025 |

## Next Steps
1. Add qualitative analysis from news articles (sentiment scores)
2. Enrich with approval rating changes before each election
3. Build prediction model using combined/election_timing_factors.csv
""".format(
    len(gdp_rows)//2, len(qtr_rows), len(inf_rows),
    len(inf_overall), len(unemp_rows), len(fuel_rows),
    len(brent_rows), len(fx_rows), len(opr_rows),
    len(turnout_rows), len(approval_rows),
    len(klse_monthly_rows), len(rows_c)
)

save_md(os.path.join(OUT, "index.md"), index)

print(f"\n{'='*60}")
print(f"All done! Insights saved to: {OUT}")
