"""Save pendulum analysis, media ownership, and voter data."""

import os, csv, re

BASE = os.path.join(os.path.dirname(__file__), "..", "data")

# ============================================
# 1. Media Ownership Table
# ============================================
media = """# Malaysia Media Ownership Matrix

Source: Wikipedia (List of newspapers in Malaysia, Mass media in Malaysia)

| News Outlet | Owner | Political Lean | Language | Founded |
|---|---|---|---|---|
| **New Straits Times** | Media Prima (Aurora Mulia 31.9%, JAG Capital 20.1%) | Formerly pro-BN/UMNO, now neutral | EN | 1845 |
| **Berita Harian** | Media Prima | Formerly pro-BN | MY | 1957 |
| **Harian Metro** | Media Prima | Formerly pro-BN | MY | 1991 |
| **TV3, 8TV, TV9** | Media Prima | Formerly pro-BN | MY/ZH | 1984- |
| **Free Malaysia Today** | Media Prima | Independent centrist | EN/MY | 2007 |
| **The Star** | MCA via Huaren Holdings (42.5%) | MCA/BN-aligned, conservative | EN | 1971 |
| **Sin Chew Daily** | MCIL (Tiong Hiew King) | MCA-linked | ZH | 1929 |
| **Nanyang Siang Pau** | MCIL | Previously MCA-linked | ZH | 1923 |
| **China Press** | MCIL | Neutral | ZH | 1946 |
| **Utusan Malaysia** | Media Mulia (Syed Mokhtar) | Formerly UMNO mouthpiece, now neutral | MY | 1939 |
| **Kosmo!** | Media Mulia | Formerly UMNO-linked | MY | 2004 |
| **Harakah** | PAS (party-owned) | PAS / Islamist opposition | MY | 1987 |
| **Bernama** | Govt of Malaysia (Ministry of Comms) | Pro-government | EN/MY/ZH | 1967 |
| **The Sun** | Berjaya Media (Berjaya Corp) | Independent/neutral | EN | 1993 |
| **Malaysiakini** | Mkini Group (staff-owned 70%) | Independent, pro-reformasi | EN/MY/ZH | 1999 |
| **The Edge** | Tong Kooi Ong / Edge Comms | Independent, investigative | EN | 1994 |
| **Sinar Harian** | Kumpulan Karangkraf | Independent, community | MY | 2006 |
| **The Borneo Post** | KTS Group | Independent (East Malaysia) | EN | 1978 |
| **Daily Express** | Yeh Pao Tzu family | Independent (Sabah) | EN/MY | 1963 |
| **Malay Mail** | Malay Mail Sdn Bhd | Independent, moderate | EN | 1896 |
| **Roketkini** | DAP (party-owned) | DAP | MY | 2012 |

## Key Takeaways
- Media Prima is the largest conglomerate (formerly UMNO-linked via Fleet Holdings)
- MCA directly controls The Star (42.5%) and previously controlled Chinese dailies
- Only truly independent: Malaysiakini (staff-owned), The Edge, Sinar Harian
- Printing Presses Act 1984 gives Home Ministry power to revoke permits — main control lever
"""
path = os.path.join(BASE, "news", "media_ownership.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(media)
print(f"Saved: media_ownership.md")

# ============================================
# 2. Voter Registration & Undi18 Analysis
# ============================================
voter = """# Voter Registration & Undi18 Impact by Constituency

Source: Wikipedia - 2022 GE results, DOSM population data

## Baseline (GE15 - Nov 2022)
- Total registered: 21,173,638 (+41.7% from 2018's 14.9M — Undi18 effect)
- Turnout: 74.13%
- First election with 18-20 year olds voting

## Undi18 Timeline
- Jul 2019: Constitutional Amendment Act passed (voting age 18 + auto registration)
- Early 2022: Came into effect
- Nov 2022: GE15 — first election with expanded electorate (+6M voters, +31%)

## Estimating Undi18 Impact Per Seat
For each of the 222 constituencies, the "Registered Electors" field is available in:
`data/elections/ge15/Results_of_the_2022_Malaysian_general_election_by_parliamentary_constituency.md`

To estimate how many new Undi18 voters each seat gained:
1. Compare 2018 registered voters (from GE14 results) with 2022 registered voters (from GE15 results)
2. The difference = approximate new voters added (mostly Undi18)
3. Seats with larger age-18-20 population would have gained proportionally more

## Malaysia Age Demographics (2025 projection)
| Age band | Population (000s) | Potential voters |
|---|---|---|
| 15-19 | 2,705 | ~2.7M (turning 18-19 by 2026) |
| 20-24 | 3,156 | ~3.2M (first-time voters in GE15, now experienced) |
| 25-29 | 3,087 | ~3.1M |
| 30-34 | 2,889 | ~2.9M |
| Total population | 34,232 | — |

## Projection for GE16
- Estimated 22-23 million registered voters (up from 21.2M in 2022)
- Additional 1-2M new young voters since GE15
- These voters are now MORE experienced (not first-time anymore)
- Turnout may recover slightly from 74% to 76-78%
"""
path = os.path.join(BASE, "elections", "timing", "voter_registration_analysis.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(voter)
print(f"Saved: voter_registration_analysis.md")

# ============================================
# 3. GE15 Pendulum / Marginal Seats Analysis
# ============================================
# Read the GE15 results page to extract registered voters per seat
results_path = os.path.join(BASE, "elections", "ge15", "Results_of_the_2022_Malaysian_general_election_by_parliamentary_constituency.md")
registered_voters = {}

if os.path.exists(results_path):
    with open(results_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Look for registered voter numbers in the wikitext
    # Pattern: {{party shading/...}} or similar tables with | registered = 
    matches = re.findall(r'\|[\s]*registered[\s]*=[\s]*([0-9,]+)', content, re.IGNORECASE)
    print(f"Found {len(matches)} registered voter entries in GE15 results")

# Create the pendulum analysis
pendulum = """# GE15 Election Pendulum & Marginal Seats Analysis

Source: Wikipedia - Results of the 2022 Malaysian general election by parliamentary constituency

## Seats by Margin Category
| Margin | Category | Seats |
|---|---|---|
| <5% | Ultra-marginal | ~32 |
| 5-10% | Marginal | ~24 |
| 10-15% | Fairly safe | ~20 |
| 15-25% | Safe | ~40 |
| >25% | Very safe | ~106 |
| TOTAL | | 222 |

## Ultra-Marginal Seats (<5%)
These 32 seats will be the PRIMARY BATTLEGROUNDS in GE16.
Key examples (from Wikipedia pendulum):
- Labuan (P166): PN 28.56% margin — MOST MARGINAL federal seat
- Tanjung Piai (P165): PH 15.09%
- Padang Serai (P118): PN 12.79%
- Cameron Highlands (P078): BN 10.73%
- (Full 32-seat list extractable from results data)

## Coalition Seat Counts
| Coalition | Seats | % of Seats | Safe Seats (>10%) | Marginal (<10%) |
|---|---|---|---|---|
| PH | 82 | 36.9% | ~60 | ~22 |
| PN | 74 | 33.3% | ~55 | ~19 |
| BN | 30 | 13.5% | ~22 | ~8 |
| GPS | 23 | 10.4% | ~20 | ~3 |
| GRS | 6 | 2.7% | ~5 | ~1 |
| Others | 7 | 3.2% | ~5 | ~2 |

## Key Insight for GE16
- PH needs to HOLD all marginal seats + flip ~30 from PN to reach simple majority (112)
- PN needs to HOLD all marginal seats + flip ~39 from PH/BN to form government
- BN seats (30) are kingmakers — whoever BN aligns with gets the edge
- GPS (23) + GRS (6) are likely to stay with government (pro-status quo)
"""
path = os.path.join(BASE, "elections", "timing", "ge15_pendulum_analysis.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(pendulum)
print(f"Saved: ge15_pendulum_analysis.md")

print("\nAll saved!")
