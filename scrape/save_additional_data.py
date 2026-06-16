"""Save BNM, flood, defection, and approval rating data."""

import os

BASE = os.path.join(os.path.dirname(__file__), "..", "data")

# === BNM / OPR Data ===
opr_content = """# BNM OPR (Overnight Policy Rate) Data

Source: Bank Negara Malaysia, Trading Economics, data.gov.my

## Current OPR: 2.75% (as of May 2026)

## MPC Meeting Schedule & Decisions 2026
| Date | Decision | Rate |
|---|---|---|
| 22 Jan 2026 | Hold | 2.75% |
| 5 Mar 2026 | Hold | 2.75% |
| 7 May 2026 | Hold | 2.75% |
| 9 Jul 2026 | Scheduled | — |
| 3 Sep 2026 | Scheduled | — |
| 5 Nov 2026 | Scheduled | — |

## OPR History (Reconstructed)
| Date | Change | New Rate | Context |
|---|---|---|---|
| Jul 2020 | Cut | 1.75% | COVID-19 emergency (record low) |
| May 2022 | Hike +25bp | 2.00% | Normalization begins |
| Jul 2022 | Hike +25bp | 2.25% | |
| Sep 2022 | Hike +25bp | 2.50% | |
| Nov 2022 | Hike +25bp | 2.75% | |
| Jan 2023 | Hold | 2.75% | |
| May 2023 | Hike +25bp | 3.00% | |
| Jul 2023 | Hold | 3.00% | |
| Sep 2023 | Hold | 3.00% | |
| Nov 2023 | Hold | 3.00% | |
| 2024 (all) | Hold ×6 | 3.00% | Stable year |
| Jan 2025 | Cut -25bp | 2.75% | First cut since 2020 |
| Mar 2025 | Hold | 2.75% | |
| May 2025 | Hold | 2.75% | |
| Jul 2025 | Hold | 2.75% | |
| Sep 2025 | Hold | 2.75% | |
| Nov 2025 | Hold | 2.75% | |
| Jan 2026 | Hold | 2.75% | |
| Mar 2026 | Hold | 2.75% | |
| May 2026 | Hold | 2.75% | |

## Historical Range
- Record Low: 1.75% (Jul 2020)
- Record High: 3.50% (Apr 2006)
- Average since 2004: 2.86%

## Forecast
- 2.75% through end 2026 Q2
- Trending toward 2.50% in 2027

## Commercial Bank FD Rates (from data.gov.my)
Monthly FDR data available 1997-2026 in interest_rates.csv
"""
path = os.path.join(BASE, "dosm", "opr", "opr_summary.md")
with open(path, "w") as f:
    f.write(opr_content)
print(f"Saved: opr_summary.md")

# === Flood / Monsoon Data ===
flood_content = """# Malaysia Flood & Monsoon Data (Election Timing Relevance)

Source: Wikipedia (Floods in Malaysia, Geography of Malaysia)

## Monsoon Seasons
| Season | Months | Impact |
|---|---|---|
| Northeast monsoon | Oct – Mar | HEAVY RAIN. Primary flood season. East coast (Kelantan, Terengganu, Pahang, Johor) worst affected. Peak Dec–Jan. |
| Southwest monsoon | May – Sep | Generally dry. Best window for elections. |
| Inter-monsoon | Mar–Apr, Sep–Oct | Transition periods. Moderate rainfall. |

## Worst Flood Months (Historical)
| Rank | Period | Event | Deaths |
|---|---|---|---|
| 1 | Dec 2014 – Jan 2015 | 2014-15 Malaysia floods | 21 |
| 2 | Dec 2021 – Jan 2022 | 2021-22 Malaysia floods | 54 |
| 3 | Jan 1971 | KL floods | 24 |
| 4 | Nov 2017 | Penang floods | 7 |
| 5 | Dec 2020 – Jan 2021 | 2020-21 floods | 6 |
| 6 | Nov 2024 – Mar 2025 | 2024-25 floods | 6+ |

## Elections Affected by Floods
- **GE15 (2022)**: Baram constituency (Sarawak) — polling suspended on 19 Nov 2022 due to flooding. Completed 21 Nov 2022 instead.
- **GE15 (2022)**: General election held 19 Nov 2022 (NE monsoon). Multiple polling stations reported issues.

## Key Takeaway
- Dec–Jan is the HIGHEST risk period for flood-related disruption
- Feb is unpredictable (2022 was a late flood year)
- Oct–Nov is early monsoon but still risky (GE15 proved this)
- May–Sep is the SAFEST window for elections
- If GE16 is held Oct–Nov 2027, flood contingency plans will be critical
"""
path = os.path.join(BASE, "elections", "timing", "flood_and_monsoon_data.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(flood_content)
print(f"Saved: flood_and_monsoon_data.md")

# === MP Defection Data ===
defection_content = """# MP Defections & Anti-Hopping Law (GE15 to Present)

Source: Wikipedia (Anti-hopping law, BERSATU expulsions)

## Anti-Hopping Law
- Passed: 28 Jul 2022 (Dewan Rakyat, 2/3 majority)
- Gazetted: 5 Oct 2022 (50 days before GE15)
- Effect: MPs who VOLUNTARILY leave their party or vote against party lose their seat → by-election
- KEY LOOPHOLE: Expelled MPs KEEP their seats as independents
- State level: 9/13 states have also passed anti-hopping laws

## BERSATU Defectors (The "6")
Declared support for Anwar starting Oct 2023, BERSATU terminated memberships 2 Jun 2024:
1. Iskandar Dzulkarnain (Kuala Kangsar) — 12 Oct 2023
2. Suhaili Abdul Rahman (Labuan) — 30 Oct 2023
3. Mohd Azizi Abu Naim (Gua Musang) — 7 Nov 2023
4. Zahari Kechik (Jeli) — 8 Nov 2023
5. Syed Abu Hussin Hafiz (Bukit Gantang) — 28 Nov 2023
6. Zulkafperi Hanapi (Tanjong Karang) — 24 Jan 2024

## Further BERSATU Expulsions (2025-2026)
7. Wan Saiful Wan Jan (Tasek Gelugor) — 14 Oct 2025
8. Saifuddin Abdullah (Indera Mahkota) — 6 Jan 2026
9. Hamzah Zainudin (Larut) — 13 Feb 2026
10. Fathul Huzir Ayob (Gerik) — 13 Feb 2026
11. Wan Ahmad Fayhsal (Machang) — 13 Feb 2026
12. Azahari Hasan (Padang Rengas) — 13 Feb 2026

## Other Major Changes
- MUDA left unity government (Sep 2023) → went to opposition
- STAR left GRS (2 Oct 2025) → independent party
- UPKO left PH (10 Nov 2025) → independent
- Rafizi Ramli & Nik Nazmi quit PKR → formed BERSAMA (19 May 2026)
  - Their seats (Pandan, Setiawangsa) now vacant → by-elections coming

## Current Government Seat Count (Jun 2026)
| Bloc | Seats |
|---|---|
| PH (PKR 29 + DAP 40 + AMANAH 8) | 77 |
| BN (UMNO 26 + MCA 2 + MIC 1 + PBRS 1) | 30 |
| GPS (PBB 14 + PRS 5 + PDP 2 + SUPP 2) | 23 |
| GRS (4) | 5 |
| WARISAN | 3 |
| UPKO | 2 |
| STAR | 1 |
| KDM | 2 |
| PBM | 1 |
| Independents (pro-govt) | 6 |
| **TOTAL Govt** | **~151** |
| PN (PAS 43 + BERSATU 19) | 62 |
| Vacant | 2 |
| **TOTAL** | **222** |

## Key Implications for GE16
- Govt majority ~151/222 = comfortable but fraying
- BN-PH cooperation under strain (N9 MB crisis, Johor BN going solo)
- PAS ended cooperation with BERSATU (8 Jun 2026) — PN is fracturing
- New party "WAWASAN" formed by expelled BERSATU faction (13 Jun 2026)
- The anti-hopping law's expulsion loophole means defectors can keep supporting govt without triggering by-elections
- This reduces the risk of govt collapse but also means the govt's majority is soft (independent support can be withdrawn)
"""
path = os.path.join(BASE, "elections", "timing", "mp_defections_and_seats.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(defection_content)
print(f"Saved: mp_defections_and_seats.md")

# === Approval Rating Timeline ===
approval_content = """# Malaysian PM & Govt Approval Ratings Timeline

Source: Merdeka Center Malaysia (https://www.merdeka.org)

## Complete Timeline
| Date | PM | PM Approval | Govt Approval | Survey |
|---|---|---|---|---|
| Aug 2018 | Mahathir | 71% | 67% | 100 Days After GE14 |
| Mar 2019 | Mahathir | 46% | 39% | One Year After GE14 |
| Sep 2020 | Muhyiddin | ~60% (est.) | — | Perceptions Towards Economy |
| Apr 2021 | Muhyiddin | ~55% (est.) | — | PM Approval Amid COVID-19 |
| Feb 2023 | Anwar | **68%** | 54% | Perceptions Post-GE15 |
| Nov 2023 | Anwar | **50%** | — | One Year After GE15 |
| Dec 2024 | Anwar | **54%** | 51% | 2nd Anniversary Unity Govt |
| Jun 2025 | Anwar | **55%** | ~56% (est.) | Mid-Term Survey |

## Demographic Breakdown (Feb 2023)
- Chinese: 73% approve
- Indian: 91% approve
- Sabah/Sarawak Bumiputera: ~70% approve
- Malay voters: 60% approve
- Overall dissatisfied: 20%

## Anwar Ibrahim Approval Trajectory
- Feb 2023: 68% (post-GE15 honeymoon)
- Nov 2023: 50% (after 1 year — steep drop)
- Dec 2024: 54% (recovery in Year 2)
- Jun 2025: 55% (stabilizing, slight uptick)

## Key Insight
Anwar's approval bottomed at ~50% in late 2023, recovered to 54-55% through 2024-2025. This is still below Mahathir's 2018 highs (71%) but far better than Najib's pre-GE14 ratings. The recovery trend favors Anwar — he would want to call GE16 when approval is on an upswing.

## Merdeka Center Reports (accessible PDFs)
- https://merdeka.org/mid-term-survey-may-2025-report-final/
- https://merdeka.org/2nd-anniversary-unity-govt-survey-highlights/
- https://merdeka.org/one-year-after-ge15-survey-report/
- https://merdeka.org/100-days-after-ge14-pms-approval-rating-at-71-government-67/
- https://merdeka.org/getting-into-one-year-after-ge14-pms-approval-rating-at-46-government-at-39/
"""
path = os.path.join(BASE, "polls", "approval_rating_timeline.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(approval_content)
print(f"Saved: approval_rating_timeline.md")

print("All data saved!")
