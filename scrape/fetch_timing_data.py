"""Download election timing factor Wikipedia pages."""

import requests, os, time

HEADERS = {"User-Agent": "ElectionPredictionBot/1.0"}
BASE = os.path.join(os.path.dirname(__file__), "..", "data", "elections", "timing")
os.makedirs(BASE, exist_ok=True)

PAGES = {
    "Parliament_15th": "Members_of_the_Dewan_Rakyat%2C_15th_Malaysian_Parliament",
    "Parliament_14th": "Members_of_the_Dewan_Rakyat%2C_14th_Malaysian_Parliament",
    "Next_Malaysian_GE": "Next_Malaysian_general_election",
    "Confidence_and_Supply": "Confidence_and_supply",
    "Geography_of_Malaysia": "Geography_of_Malaysia",
    "2025 Sabah state election": "2025_Sabah_state_election",
    "Next Sabah state election": "Next_Sabah_state_election",
    "Malaysian federal budget": "Malaysian_federal_budget",
}

for name, title in PAGES.items():
    print(f"Fetching: {name}")
    url = f"https://en.wikipedia.org/w/index.php?title={title}&action=raw"
    try:
        resp = requests.get(url, timeout=15, headers=HEADERS)
        if resp.status_code == 200:
            path = os.path.join(BASE, f"{name}.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"# {name}\n\n*Source: https://en.wikipedia.org/wiki/{title}*\n\n---\n\n{resp.text}")
            print(f"  OK ({len(resp.text)} chars)")
        else:
            print(f"  FAIL {resp.status_code}")
    except Exception as e:
        print(f"  ERROR: {e}")
    time.sleep(0.3)

# Create summary timing document
summary = """# Malaysia Election Timing Factors

## Parliament Term
- 15th Parliament first sitting: 19 Dec 2022
- Term expires: 17 Feb 2028 (5 years from first sitting)
- Election must be held within 60 days of dissolution

## Parliament Sessions (15th Parliament)
| Meeting | Dates |
|---|---|
| 2022 Special | 19–20 Dec 2022 |
| 2023 1st | 13 Feb – 4 Apr 2023 |
| 2023 2nd | 22 May – 15 Jun 2023 |
| 2023 Special | 11–19 Sep 2023 |
| 2023 3rd | 9 Oct – 30 Nov 2023 |
| 2024 1st | 26 Feb – 27 Mar 2024 |
| 2024 2nd | 24 Jun – 18 Jul 2024 |
| 2024 3rd | 14 Oct – 12 Dec 2024 |
| 2025 1st | 3 Feb – 6 Mar 2025 |
| 2025 Special | 5 May 2025 |
| 2025 2nd | 21 Jul – 28 Aug 2025 |
| 2025 3rd | 6 Oct – 4 Dec 2025 |
| 2026 1st | 19 Jan – 3 Mar 2026 |
| 2026 2nd | 22 Jun – 16 Jul 2026 |
| 2026 3rd | 5 Oct – 8 Dec 2026 |

## Budget Presentation
- Traditionally in October (during 3rd Meeting of Parliament)
- Budget is a confidence measure — dissolution unlikely while budget debated

## Monsoon Seasons
| Monsoon | Months | Impact |
|---|---|---|
| Northeast | Oct – Mar | Heavy rainfall, flooding on east coast (Kelantan, Terengganu) |
| Southwest | May – Sep | Less rain, better for campaigning |
| Transition | Mar, Oct | Shoulder periods |

## State Election Alignment
| State | Latest Possible Date |
|---|---|
| Sabah | Already held (29 Nov 2025) |
| Malacca | ~Feb 2027 |
| Sarawak | ~Apr 2027 |
| Johor | ~Jun 2027 |

## Coalition Status
- Unity Government: PH + BN + GPS + GRS + WARISAN + others
- 153 government seats vs 69 opposition
- Confidence & supply agreements in place
- BERSATU expulsions (Feb-Jun 2026): 6 MPs turned independent, affecting PN strength

## Redelineation
- EC can consider boundary changes after Mar 2026
- Typically avoided close to elections

## Key Takeaway
The earliest likely window for GE16 is late 2026 or early 2027.
The PM would likely avoid:
- Monsoon season (Oct–Mar) on east coast
- Budget period (Oct–Dec)
- State elections (to avoid concurrent campaigning)
Likely windows: Jun–Sep 2026, Mar–Sep 2027
"""

path = os.path.join(BASE, "election_timing_summary.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(summary)
print(f"Saved timing summary ({len(summary)} chars)")
print("Done!")
