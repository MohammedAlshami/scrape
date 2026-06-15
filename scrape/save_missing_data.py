"""Save redelineation and parliament voting data."""

import os

BASE = os.path.join(os.path.dirname(__file__), "..", "data", "elections", "timing")

# ============================================
# 1. Redelineation Analysis
# ============================================
redelineation = """# Malaysia Electoral Redelineation (Boundary Review)

Source: Wikipedia, The Edge, Constitution of Malaysia

## Timeline
- Last redelineation: 2018 (gazetted 29 Mar 2018, used for GE14 & GE15)
- Next eligible: **After March 2026** (8-year minimum under Article 113)
- Must be completed before Parliament dissolution for GE16

## Current Seat Distribution vs Voter Share
| State | Actual Seats | Expected (by voters) | Gap |
|---|---|---|---|
| Selangor | 22 | 39 | **-17** grossly under-represented |
| Johor | 26 | 27 | -1 |
| Penang | 13 | 13 | 0 |
| Sarawak | **31** | 19 | **+12** heavily over-represented |
| Sabah | 25 | 17 | **+8** over-represented |
| Perak | 24 | 21 | +3 |
| Kelantan | 14 | 15 | -1 |
| Terengganu | 8 | 10 | -2 |
| KL/Putrajaya | 12 | ~15 | -3 |

## Extreme Examples (Voter Count per Seat)
| Seat | State | Voters | 
|---|---|---|
| Bangi (P102) | Selangor | **303,430** — largest |
| Igan (P206) | Sarawak | **28,290** — smallest |
| Ratio: Bangi : Igan = **10.7x** |

## Who Benefits from Current Boundaries
- **PN** (PAS/BERSATU): Rural northern states (Perlis, Kedah, Kelantan, Terengganu) with smaller seats
- **GPS**: Sarawak rural seats massively over-represented
- **PH**: Biggest loser — urban seats (Selangor) have 303k vs 28k voters

## Who Could Benefit from Redelineation
- **PH/BN unity govt**: If urban seats split, PH could gain 10-15 seats
- **Sarawak (GPS)**: Could gain additional seats if Article 46 amended (needs 2/3 majority)
- **Sabah**: Also pushing for more federal seats

## Process
1. EC announces review, publishes initial proposals
2. Public display of maps, objection period, local hearings
3. EC submits report to PM
4. PM tables in Dewan Rakyat → simple majority to approve
5. Gazetted with YDPA consent

## Key Unknown
- Will boundaries change within 222 seats? (simple majority)
- Or will Article 46 be amended to increase seats? (needs 2/3 = 148 votes)
- Unity govt currently has ~151 seats — just enough for 2/3
- Sarawak wants 1/3 of parliamentary seats (74/222) — currently has only 31
"""
path = os.path.join(BASE, "redelineation_analysis.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(redelineation)
print(f"Saved: redelineation_analysis.md")

# ============================================
# 2. Parliament Voting Records
# ============================================
voting = """# Malaysian Parliament Voting Records & Government Strength

Source: Wikipedia, Constitution of Malaysia

## Confidence Motions
| Date | Motion | Result | Vote |
|---|---|---|---|
| 19 Dec 2022 | Confidence in PM Anwar Ibrahim | **Passed** | Voice vote (no division recorded) |
| 4 Dec 2020 | No-confidence vs Perak MB Azmin | **Passed** | Recorded division (state level) |

- Anwar's confidence motion passed by voice vote — exact tally not published
- No recorded no-confidence division at federal level since Anwar took office

## Budget Votes
| Year | Budget | Status |
|---|---|---|
| 2023 | Belanjawan 2023 | Passed |
| 2024 | Belanjawan 2024 | Passed |
| 2025 | Belanjawan 2025 | Passed |
| 2026 | Belanjawan 2026 | Passed |

All passed with government's ~151 seat majority. Exact division numbers not published on Wikipedia (would need Hansard).

## Key Legislation Votes
| Date | Bill | Votes For | Votes Against | Result |
|---|---|---|---|---|
| 14 Dec 2021 | MA63 Amendment | 199 | 0 | Passed unanimously |
| Jul 2019 | Constitution Amendment (Undi18) | Majority | — | Passed |
| 28 Jul 2022 | Anti-Hopping Law | 2/3 majority | — | Passed |

## Government Majority Timeline
| Period | Govt Seats | Opposition | Majority |
|---|---|---|---|
| Dec 2022 (formed) | ~148 | ~74 | ~74 |
| 2024 (after 6 BERSATU defections) | ~154 | ~68 | ~86 |
| 2026 (current) | ~151 | ~69 | ~82 |
| Vacant | 2 seats (Pandan, Setiawangsa) | — | — |

## Key Test for GE16
- Govt majority of ~82 is **comfortable** but not invulnerable
- Budget votes are the real test — if any coalition partner (BN, GPS) abstains or votes against, the govt could lose its majority
- BN-PH relations have been strained (N9 MB crisis, Johor BN going solo)
- GPS is reliable but has its own state election concerns
- The govt has NEVER lost a parliamentary vote since taking office
"""
path = os.path.join(BASE, "parliament_voting_records.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(voting)
print(f"Saved: parliament_voting_records.md")

# Updated synthesis
synthesis = """# GE16 Prediction - Complete Synthesis

## All Factors Summary

| Factor | Current State | Impact on Timing |
|---|---|---|
| **Constitutional deadline** | 17 Feb 2028 | Hard stop |
| **Government majority** | ~82 seats comfortable | No rush, can wait |
| **PM approval** | 55% and recovering | Favors waiting (trend is up) |
| **By-election trend** | Govt stable/improving | Can wait, no urgency |
| **PN momentum** | Receded (PAS-BERSATU split) | Less threat, can wait |
| **Economy** | GDP ~5%, inflation ~2%, OPR 2.75% | Stable |
| **Redelineation** | Eligible after Mar 2026 | Favors waiting for new boundaries |
| **State elections** | Malacca (Feb 27), Sarawak (Apr 27), Johor (Jun 27) | Synchronization opportunity |
| **Monsoon** | NE Oct-Mar, SW May-Sep | Favors Jul-Sep window |
| **Festivals** | CNY Jan-Feb, Ramadan Feb-Mar, HRP Mar | Favors Apr-Sep window |
| **Campaign trend** | 12-14 days | Short campaign likely |

## Most Likely Window: July - September 2027
- Dry season (SW monsoon)
- No major festivals
- After state elections (Malacca, Sarawak, Johor done)
- After redelineation completed
- PM approval on upswing
- Economy stable
- PN in disarray (PAS-BERSATU split)
- BN-PH relationship still intact (for now)

## Key Risks
- BN-PH coalition collapses → snap election 2026
- Economy enters recession → government waits longer
- Redelineation delayed → pushes GE16 to early 2028
"""
path = os.path.join(BASE, "ge16_complete_synthesis.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(synthesis)
print(f"Saved: ge16_complete_synthesis.md")

print("\nDone! All missing data collected.")
