"""Save flood stats, by-election CSV, and voter turnout data."""

import os, csv

BASE = os.path.join(os.path.dirname(__file__), "..", "data")

# === Flood Statistics with Numbers ===
flood_stats = """# Malaysia Major Flood Events - Statistics

| Year | Month(s) | Deaths | Displaced/Evacuated | Damage Cost (USD) | States Affected |
|---|---|---|---|---|---|
| 1971 | Jan | 32 | 180,000 affected | — | Kuala Lumpur |
| 2006-07 | Dec-Jan | 6-15 | 60,000-70,000 evacuated | $395M | Johor, Melaka, Pahang, N.Sembilan |
| 2010 | Oct-Nov | 4 | ~50,000 evacuated | — | Kedah, Perlis, Kelantan |
| 2014-15 | Dec-Jan | 21 | 500,000+ affected, 200,000+ evacuated | $560M | 11 states |
| 2017 | Nov | 7 | 7,294+ evacuated | $76.3M | Kedah, Penang, Perak |
| 2020-21 | Nov-Jan | 9 | Tens of thousands evacuated | — | Pahang, Johor, Terengganu, Kelantan, Perak, Selangor, Sabah |
| 2021-22 | Dec-Jan | 54 | 125,490+ cumulative | $1.27-1.55B (govt) / $4.77B (unofficial) | Selangor, KL, Pahang, Perak, N.Sembilan, Melaka, Kelantan, Terengganu, Sabah |

Source: Wikipedia - Floods in Malaysia

## Monthly Flood Risk Assessment
| Month | Monsoon | Flood Risk | Historical Major Events |
|---|---|---|---|
| Jan | NE monsoon peak | EXTREME | 1971 (32 dead), 2015 (21 dead), 2022 (54 dead) |
| Feb | Late NE monsoon | HIGH | 2022 east coast floods (unexpected timing) |
| Mar | Transition | MODERATE | — |
| Apr | Inter-monsoon | LOW | — |
| May | SW monsoon start | LOW | — |
| Jun | SW monsoon | LOW | — |
| Jul | SW monsoon | LOW | — |
| Aug | SW monsoon | LOW | — |
| Sep | SW monsoon / transition | LOW-MOD | 2017 Penang |
| Oct | NE monsoon start | MODERATE | 2010 (4 dead) |
| Nov | NE monsoon | HIGH | 2017 (7 dead), 2020 start |
| Dec | NE monsoon peak | EXTREME | 2006, 2014, 2020, 2021 all started |

## Election Flood Risk
- GE15 (19 Nov 2022) was held during NE monsoon → Baram polling STATIONS WERE FLOODED, delayed 2 days
- Dec-Jan is the HIGHEST risk period - avoid for election
- May-Sep is the SAFEST window
"""
path = os.path.join(BASE, "elections", "timing", "flood_statistics.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(flood_stats)
print(f"Saved: flood_statistics.md")

# === Voter Turnout ===
turnout = """# Malaysian General Election Voter Turnout (GE10-GE15)

| Election | Date | Registered Voters | Turnout % | Total Votes | Notes |
|---|---|---|---|---|---|
| GE10 (1999) | 29 Nov 1999 | 9,546,303 | 71.19% | ~6,795,000 | Mahathir's last election |
| GE11 (2004) | 21 Mar 2004 | 9,755,097 | 72.95% | ~7,116,000 | Abdullah's landslide |
| GE12 (2008) | 8 Mar 2008 | 10,740,228 | 75.38% | ~8,096,000 | BN lost 2/3 majority |
| GE13 (2013) | 5 May 2013 | 13,268,002 | 84.60% | ~11,224,000 | Highest turnout ever |
| GE14 (2018) | 9 May 2018 | 14,940,624 | 82.32% | ~12,299,000 | First regime change |
| GE15 (2022) | 19 Nov 2022 | 21,173,638 | 74.13% | ~15,696,000 | First Undi18 election |

## Trends
- Turnout peaked at 84.6% in 2013 (the "Malaysian Spring")
- Declined sharply to 74.13% in GE15 (first election with Undi18/auto-registration)
- The 6 million new voters (Undi18) had lower turnout propensity in GE15
- By GE16, these voters will be more experienced - turnout may recover slightly to 75-78%
- Higher turnout generally favors opposition (more young, urban voters)
- Lower turnout generally favors incumbents (older, rural voters more reliable)

## Registered Voters Growth
- GE10 to GE15: 9.5M → 21.2M (+123% in 23 years)
- GE13 to GE15 alone: 13.3M → 21.2M (+59%) due to Undi18
- By GE16: estimated 22-23M registered voters
"""
path = os.path.join(BASE, "elections", "timing", "voter_turnout.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(turnout)
print(f"Saved: voter_turnout.md")

# === By-election Results CSV ===
by_el_folder = os.path.join(BASE, "elections", "by_elections")
os.makedirs(by_el_folder, exist_ok=True)

by_el_data = [
    ["2023-11-04", "Jepak", "State", "Sarawak", "GPS(PBB)", "GPS(PBB)", "Iskandar Turkee", "PBB", "GPS", 9638, 88.24, 18.80, "Stevenson Joseph Sumbang", "PBK", "", 854, 7.82, 1.33, "Chieng Lea Ping", "ASPIRASI", "", 431, 3.95, 3.95, 48.57, 8784, "", "Death of incumbent"],
    ["2023-12-02", "Kemaman", "Federal", "Terengganu", "PN(PAS)", "PN(PAS)", "Ahmad Samsuri Mokhtar", "PAS", "PN", 64998, 70.06, 11.95, "Raja Mohamed Affandi", "Direct Member", "BN", 27778, 29.94, -4.13, "", "", "", 0, 0, 0, 65.76, 37220, 40.12, "Seat vacated (vote buying)"],
    ["2023-08-12", "Kuala Terengganu", "Federal", "Terengganu", "PN(PAS)", "PN(PAS)", "Ahmad Amzad Hashim", "PAS", "PN", 68369, 76.41, 19.69, "Azan Ismail", "PKR", "PH", 21103, 23.59, 3.70, "", "", "", 0, 0, 0, 73.34, 47266, "", "Incumbent disqualified (corruption)"],
    ["2023-10-07", "Pelangai", "State", "Pahang", "BN(UMNO)", "BN(UMNO)", "Amizar Abu Adam", "UMNO", "BN", 7324, 62.35, 4.64, "Kasim Samat", "PAS", "PN", 4375, 37.25, 11.51, "Haslihelmey D.Z.", "IND", "", 47, 0.40, 0.40, 72.12, 2949, "", "Death of incumbent (plane crash)"],
    ["2023-09-09", "Pulai", "Federal", "Johor", "PH(AMANAH)", "PH(AMANAH)", "Suhaizan Kayat", "AMANAH", "PH", 48283, 61.55, 6.22, "Zulkifli Jaafar", "BERSATU", "PN", 29642, 37.78, 20.15, "Samsudin M.F.", "IND", "", 528, 0.67, 0.67, 47.33, 18641, "", "Death of incumbent Salahuddin"],
    ["2023-09-09", "Simpang Jeram", "State", "Johor", "PH(AMANAH)", "PH(AMANAH)", "Nazri Abdul Rahman", "AMANAH", "PH", 13844, 56.54, 15.60, "Mohd Mazri Yahya", "PAS", "PN", 10330, 42.19, 12.47, "Jeganathan S.", "IND", "", 311, 1.27, 1.27, 60.85, 3514, "", "Same day as Pulai"],
    ["2024-05-11", "Kuala Kubu Baharu", "State", "Selangor", "PH(DAP)", "PH(DAP)", "Pang Sock Tao", "DAP", "PH", 14000, 57.21, 2.81, "Khairul Azhari Saut", "BERSATU", "PN", 10131, 41.40, 2.07, "Eris Nyau K.X.", "IND", "", 188, 0.77, 0.77, 61.51, 3869, 15.80, "Hafizah Zainuddin (PRM) 152 votes 0.62%"],
    ["2024-09-28", "Mahkota", "State", "Johor", "BN(UMNO)", "BN(UMNO)", "Syed Hussien S.A.", "UMNO", "BN", 27995, 79.21, 33.35, "Mohamad Haizan J.", "BERSATU", "PN", 7347, 20.79, -0.23, "", "", "", 0, 0, 0, 53.84, 20648, 57.83, "PH gave way to BN"],
    ["2024-08-17", "Nenggiri", "State", "Kelantan", "PN(BERSATU)", "BN(UMNO)", "Mohd Azmawi F.A.G.", "UMNO", "BN", 9091, 61.35, 14.61, "Mohd Rizwadi I.", "BERSATU", "PN", 5739, 38.65, -14.61, "", "", "", 0, 0, 0, 73.88, 3352, 22.70, "FLIPPED! BN won PAS seat"],
    ["2024-07-06", "Sungai Bakap", "State", "Penang", "PN(PAS)", "PN(PAS)", "Abidin Ismail", "PAS", "PN", 14489, 58.63, 5.94, "Joohari Ariffin", "PKR", "PH", 10222, 41.37, -5.94, "", "", "", 0, 0, 0, 63.45, 4267, 17.26, "PN increased majority"],
    ["2025-04-26", "Ayer Kuning", "State", "Perak", "BN(UMNO)", "BN(UMNO)", "Mohamad Yusri Bakir", "UMNO", "BN", 11065, 60.70, 21.97, "Abdul Muhaimin M.", "PAS", "PN", 6059, 33.23, 3.93, "Bawani Kaniapan", "PSM", "", 1106, 6.07, 3.57, 58.06, 5006, 27.47, "BN majority surged"],
    ["2026-01-24", "Kinabatangan", "Federal", "Sabah", "BN(UMNO)", "BN(UMNO)", "Mohd Kurniawan N.M.", "UMNO", "BN", 19852, 75.09, 17.66, "Saddi Abdul Rahman", "WARISAN", "", 5638, 21.33, -21.29, "Goldam Hamid", "IND", "", 946, 3.58, 3.58, 55.06, 14214, 53.76, "GRS/PN did not contest"],
    ["2026-01-24", "Lamag", "State", "Sabah", "BN(UMNO)", "BN(UMNO)", "Mohd Ismail Ayob", "Direct", "BN", 7269, 82.07, 42.93, "Mazliwati A.M.C.", "WARISAN", "", 1588, 17.93, 14.50, "", "", "", 0, 0, 0, 64.93, 5681, 64.14, "Same day as Kinabatangan"],
]

header = ["Date", "Seat", "Type", "State", "Prev_Holder", "Winner", "Cand1_Name", "Cand1_Party", "Cand1_Alliance", "Cand1_Votes", "Cand1_Pct", "Cand1_Swing", "Cand2_Name", "Cand2_Party", "Cand2_Alliance", "Cand2_Votes", "Cand2_Pct", "Cand2_Swing", "Cand3_Name", "Cand3_Party", "Cand3_Alliance", "Cand3_Votes", "Cand3_Pct", "Cand3_Swing", "Turnout", "Majority_Votes", "Majority_Pct", "Notes"]
path = os.path.join(by_el_folder, "by_election_results_2023_2026.csv")
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(by_el_data)
print(f"Saved: by_election_results_2023_2026.csv ({len(by_el_data)} rows)")

print("\nAll done!")
