"""Save festival calendar, by-election trends, and timing analysis."""

import os

BASE = os.path.join(os.path.dirname(__file__), "..", "data", "elections", "timing")
os.makedirs(BASE, exist_ok=True)

# Festival calendar
festival = """# Malaysia Festival & Holiday Calendar for Election Timing

Source: Wikipedia (Public holidays in Malaysia, Culture of Malaysia)

## Major Festivals (Moving Dates)
| Festival | 2026 | 2027 | 2028 | Impact |
|---|---|---|---|---|
| Chinese New Year | 17 Feb | 6 Feb | 26 Jan | Major — avoid campaigning/polling |
| Ramadan starts | ~18 Feb | ~7 Feb | ~27 Jan | Campaigning difficult (day fasting) |
| Hari Raya Puasa | ~19-20 Mar | ~8-9 Mar | ~25-26 Feb | Major — avoid 1 week before/after |
| Hari Raya Haji | ~27-28 May | ~16-17 May | ~4-5 May | Moderate |
| Deepavali | ~8 Nov | ~28 Oct | ~16 Nov | Major — avoid (esp. west coast) |
| Christmas | 25 Dec | 25 Dec | 25 Dec | Moderate |

## Fixed Holidays
| Date | Holiday |
|---|---|
| 1 May | Labour Day |
| 1st Mon Jun | Agong's Birthday |
| 31 Aug | National Day (Merdeka) |
| 16 Sep | Malaysia Day |

## Recommended Windows for GE16
| Window | Months | Risk | Notes |
|---|---|---|---|
| BEST | **Jul – Sep 2027** | LOW | Dry SW monsoon, no major festivals, best campaigning weather |
| GOOD | **Apr 2027** | LOW-MOD | After CNY & Hari Raya Puasa, before Hari Raya Haji |
| OK | **Aug – Sep 2026** | LOW-MOD | Also viable but redelineation may not be done |
| RISKY | **Oct – Nov 2027** | MOD-HIGH | Deepavali + NE monsoon start + school exams |
| AVOID | Dec–Feb | HIGH | Monsoon, CNY, Ramadan |
| AVOID | Oct–Nov | HIGH | Monsoon + Deepavali |

Polling day can be declared a public holiday (Holidays Act 1951).
"""

# By-election trend analysis
by_trend = """# By-Election Vote Swing Trend (2022-2025)

Source: Wikipedia by-election pages, collected data

## Government (PH+BN) vs PN Vote Share Trend
| Date | By-election | Govt% | PN% | Trend |
|---|---|---|---|---|
| Aug 2023 | Kuala Terengganu | 23.6% | 76.4% | PAS stronghold |
| Sep 2023 | Pulai | **61.6%** | 37.8% | PH holds, govt strong |
| Sep 2023 | Simpang Jeram | **56.5%** | 42.2% | PH holds |
| Oct 2023 | Pelangai | **62.4%** | 37.3% | BN holds |
| Dec 2023 | Kemaman | 29.9% | **70.1%** | PAS stronghold |
| May 2024 | Kuala Kubu Baharu | **57.2%** | 41.4% | PH holds, margin stable |
| Jul 2024 | Sungai Bakap | 41.4% | **58.6%** | ⚠ PN GAINED in Penang |
| Aug 2024 | Nenggiri | **61.4%** | 38.7% | ★ FLIPPED from PN to BN |
| Apr 2025 | Ayer Kuning | **60.7%** | 33.2% | BN majority surged |

## Key Insights
- Govt (PH+BN) wins in mixed/urban seats (Pulai, KKB, Pelangai, Ayer Kuning)
- PN dominates in Malay heartland (KT, Kemaman)
- **Nenggiri flip** (Aug 2024) is the most significant — BN won a PAS seat in Kelantan
- **Sungai Bakap** (Jul 2024) is the warning sign — PN gained ground in Penang
- Trend: Govt vote share has been STABLE or IMPROVING since mid-2024
- PN's "Green Wave" has NOT expanded beyond PAS strongholds

## Turnout Trend
- Sep 2023: 47-61%
- Oct 2023: 72%
- May-Jul 2024: 61-63%
- Aug 2024: 74%
- Apr 2025: 58%
Trend: Turnout varies widely (47-74%). Low turnout generally favors incumbents.
"""

# Constitution timing
constitution = """# Constitutional Timeline for GE16

Source: Constitution of Malaysia, Article 55, Next Malaysian general election page

## Key Dates
| Event | Date |
|---|---|
| First sitting of 15th Parliament | 19 Dec 2022 |
| Maximum term (5 years) | 18 Dec 2027 |
| Election must be held within 60 days of dissolution | 17 Feb 2028 (latest) |
| Earliest dissolution possible | Any time on PM's advice |

## Dissolution Rules (Article 55)
- Parliament lasts 5 years from first meeting
- YDPA (King) dissolves on PM's advice
- YDPA MAY withhold consent (Article 40(2)(b)) — has never done so
- Election within 60 days of dissolution
- Parliament must reconvene within 120 days

## State Assembly Expiry (Latest Possible Dates)
| State | Latest Election |
|---|---|
| Malacca | 25 Feb 2027 |
| Sarawak | 15 Apr 2027 |
| Johor | 20 Jun 2027 |
| Perlis | Same as GE16 (Dec 2027) |
| Pahang | 27 Feb 2028 |
| Penang | 28 Oct 2028 |
| Selangor | 18 Nov 2028 |
| Kedah | 24 Nov 2028 |

## Anwar's Stated Position
- No public statements on Wikipedia about calling early election
- Focus on economic recovery and unity government stability
- Opposition (PN) pushing for simultaneous state+federal elections

## Current Opinion Polls (as of Nov 2024)
PH 36%, PN 29%, BN 20%, GPS 8%, GRS 5%, WARISAN 2%
Source: Cited in Wikipedia Next GE page
"""

for name, content in [
    ("festival_calendar.md", festival),
    ("by_election_trend_analysis.md", by_trend),
    ("constitutional_timeline.md", constitution),
]:
    path = os.path.join(BASE, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved: {name}")

print("\nDone!")
