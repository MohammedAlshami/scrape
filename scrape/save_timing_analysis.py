"""Save GE16 timing analysis data."""

import requests, os

HEADERS = {"User-Agent": "ElectionPredictionBot/1.0"}
BASE = os.path.join(os.path.dirname(__file__), "..", "data", "elections", "timing")
os.makedirs(BASE, exist_ok=True)

# Save by-election trend data
by_election_trend = """# By-Election Trends 2024-2026 (GE16 Leading Indicators)

## Results Table
| By-election | Date | Held By | Result | Majority Swing | Signal |
|---|---|---|---|---|---|
| Sungai Bakap (Penang) | 6 Jul 2024 | PN | PN hold | +5.94pp for PN | PN still strong in rural Malay seats |
| Kuala Kubu Baharu (Selangor) | 11 May 2024 | PH | PH hold | +2.81pp for PH | PH holds mixed urban seat |
| Nenggiri (Kelantan) | 17 Aug 2024 | PN | **FLIPPED to BN** | +14.61pp for BN | BN can win in PAS heartland |
| Mahkota (Johor) | 28 Sep 2024 | BN | BN hold (landslide) | +33.35pp for BN | BN fortress in Johor intact |
| Ayer Kuning (Perak) | 26 Apr 2025 | BN | BN hold | +21.97pp for BN | BN gaining in Perak |
| Kinabatangan (Sabah) | 24 Jan 2026 | BN | BN hold (landslide) | +17.66pp for BN | Sabah solid for BN/GRS |
| Lamag (Sabah) | 24 Jan 2026 | BN | BN hold (landslide) | +42.93pp for BN | Sabah solid for BN/GRS |

## Analysis
- **PN momentum peaked at GE15** (2022) and has slightly receded
- **BN/PH (Unity Govt) has won 5/7 by-elections** since 2024, with increased majorities
- **Nenggiri flip** in Kelantan is the most significant — BN can still win in PAS territory
- **Turnout declining** across all by-elections (-3% to -16%) — low salience elections
- **PN's "Green Wave" has not expanded** beyond its GE15 gains
- **Sabah remains BN/GRS territory** — no PN presence in recent by-elections
"""

# Save historical dissolution data
dissolution_data = """# Historical Malaysian Election Dissolution Dates

| Election | Parliament | Dissolution Date | Election Date | Days Diff | Campaign | PM at Dissolution | Result |
|---|---|---|---|---|---|---|---|
| GE10 (1999) | 9th | ~10 Nov 1999 | 29 Nov 1999 | ~19 | 13 days | Mahathir Mohamad | BN win (148/193) |
| GE11 (2004) | 10th | 2 Mar 2004 | 21 Mar 2004 | 19 | 8 days | Abdullah Badawi | BN landslide (198/219) |
| GE12 (2008) | 11th | 13 Feb 2008 | 8 Mar 2008 | 24 | 13 days | Abdullah Badawi | BN lost 2/3 (140/222) |
| GE13 (2013) | 12th | 3 Apr 2013 | 5 May 2013 | 32 | 15 days | Najib Razak | BN win (133/222) |
| GE14 (2018) | 13th | 7 Apr 2018 | 9 May 2018 | 32 | 11 days | Najib Razak | PH win (113/222) |
| GE15 (2022) | 14th | 10 Oct 2022 | 19 Nov 2022 | 40 | 14 days | Ismail Sabri | Hung parliament |

## Trends
- Dissolution-to-election period: **19 to 40 days**, trending longer (avg ~28 days)
- Campaign period: **8 to 15 days**
- All elections since GE11 were **snap elections** (called before 5-year term expiry)
- 4 of last 6 elections were called in **Mar-Apr** (GE11, GE12, GE13, GE14)
- GE15 was called in **Oct** (atypical, during monsoon)
- Most elections held on **Saturday** (GE14 was Wednesday — first time)
"""

# Save GE16 timing prediction
ge16_prediction = """# GE16 Timing Prediction

## Parliament Timeline
- First sitting of 15th Parliament: **19 Dec 2022**
- Maximum term (5 years): **18 Dec 2027** (dissolution must happen by then)
- Latest possible election: **17 Feb 2028** (60 days after dissolution deadline)

## Key Timing Constraints

### Fixed Dates (Calendar 2026-2027)
| Date | Event | Impact |
|---|---|---|
| **2026** | | |
| 19 Jan – 3 Mar | Parliament sitting | Can dissolve during or after |
| 5 Oct – 8 Dec | Budget 2027 tabled | Budget = confidence vote, unlikely to dissolve during |
| **2027** | | |
| ~Feb | Malacca state election due | Avoid concurrent federal election |
| ~Apr | Sarawak state election due | Avoid concurrent federal election |
| ~Jun | Johor state election due | Avoid concurrent federal election |
| ~Jun–Aug | 6 state elections due (Penang, Selangor, NS, Kedah, Kelantan, Terengganu) | These are the BIG ones |
| 18 Dec | Parliament automatically dissolves | Hard deadline |

### Monsoon Constraints
| Season | Months | Impact |
|---|---|---|
| Northeast monsoon | Oct – Mar | Flooding on east coast (Kelantan, Terengganu) — avoid |
| Southwest monsoon | May – Sep | Generally dry — best for elections |
| Inter-monsoon | Mar–Apr, Sep–Oct | Transition periods — acceptable |

## Scenarios

### Scenario A (Most Likely ~60%): Late 2027 / Early 2028
- Parliament runs close to full term
- State elections held separately mid-2027 (Jun–Aug)
- GE16 called **Oct–Nov 2027** (after SW monsoon, before NE monsoon fully sets in)
- OR **Jan–Feb 2028** (after NE monsoon peak, before term expires)
- Pros: Maximum time in power, economy recovery, redelineation completed
- Cons: Tight with state election schedule

### Scenario B (Moderate ~25%): Mid 2027 (synchronized)
- Dissolve in **Jun 2027** to align with 6 state elections
- Election in **Jul–Aug 2027**
- Pros: Cost savings, coattail effects, lower turnout helps incumbents
- Cons: Anwar gives up ~6 months of term, risks if economy not fully recovered

### Scenario C (Unlikely ~10%): 2026 snap election
- Dissolve in **Aug–Sep 2026** (after SW monsoon, before budget)
- Election in **Sep–Oct 2026**
- Pros: Capitalize on strong by-election results, economy improving
- Cons: Redelineation not done, looks opportunistic, PN could campaign on "broken promise"

### Scenario D (Very Unlikely ~5%): Early 2026 or sooner
- Would require government collapse or major crisis

## Prediction: GE16 in **October–November 2027** (55% probability)
- Realistic snapshot: Election in Nov 2027, just before monsoon, after state elections are done
- Back-up: Feb 2028 (last feasible window)
"""

for name, content in [
    ("by_election_trends_2024_2026.md", by_election_trend),
    ("historical_dissolution_dates.md", dissolution_data),
    ("ge16_timing_prediction.md", ge16_prediction),
]:
    path = os.path.join(BASE, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved: {name}")

print("Done!")
