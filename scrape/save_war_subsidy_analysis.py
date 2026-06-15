"""Save Iran war, subsidy, and early election analysis to data folder."""

import os

BASE = os.path.join(os.path.dirname(__file__), "..", "data")

# === Iran War & Oil Impact ===
iran = """# US-Iran War & Impact on Malaysia's Economy

Source: Wikipedia (2025-2026 Iran-US negotiations, Economy of Malaysia, Petronas)

## Timeline
| Date | Event | Oil Price Impact |
|---|---|---|
| Mar 2025 | Trump sets 60-day deadline for Iran deal | Stable ~$67 |
| Jun 2025 | Israel strikes Iran. US strikes nuclear sites | Spike |
| 28 Feb 2026 | US+Israel full-scale war on Iran. Khamenei killed | Surge to $80+ |
| Mar 2026 | Iran blockades Strait of Hormuz | $120+, IEA: "largest supply disruption ever" |
| Apr 2026 | Ceasefire agreed | Stabilizing |
| May 2026 | Trump says MOU near, Strait may reopen | Potential drop |

## Impact on Malaysia
| Factor | Effect |
|---|---|
| Oil prices surging | BENEFITS Malaysia (net oil exporter) |
| Petronas dividends | Expected to rise significantly (was RM50bn in 2022) |
| Fuel subsidy cost | Ballooned to RM3.2bn/month (Mar 2026) during crisis |
| Ringgit | Strengthened to RM4.12/USD (Dec 2025) from RM4.80 (Feb 2024) |
| Inflation | Low at 1.2% (May 2025) but global inflation spike coming |
| GDP growth | ~5% (2026 est.) |

## Petronas Revenue to Government
- 15% of federal government revenue (Fitch 2015-2020 avg)
- Cumulative dividends since 1974: RM403.3 billion
- Record: RM67.6bn (2008), RM54bn (2019), RM50bn (2022)
- 2023: US$73bn revenue, US$17bn net income

## Election Timing Implication
- War boosts oil revenue → MORE fiscal space for government
- If peace deal + Hormuz reopens → Iranian oil returns → oil prices DROP → Petronas dividends FALL
- Anwar has incentive to call election WHILE oil revenue is high, before peace deal causes price crash
- BUT: global inflation from war could hurt voters' cost of living
- Subsidy costs ballooned during crisis (RM3.2bn/month) — this is unsustainable
"""
path = os.path.join(BASE, "dosm", "fuel_prices", "iran_war_impact.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(iran)
print(f"Saved: iran_war_impact.md")

# === Subsidy & Budget Analysis ===
subsidy = """# Malaysia Fuel Subsidy & Budget Deficit Analysis

Source: Wikipedia (Economy of Malaysia, Anwar Ibrahim, budget pages)

## Annual Fuel Subsidy Cost
| Year | Fuel Subsidy (RM) | Total Subsidies | Notes |
|---|---|---|---|
| 2022 | RM52 billion | RM70.3bn | Blanket subsidies - fuel = 74% of total |
| 2023 | ~RM50-55bn | ~RM75bn | Still blanket subsidies |
| 2024 | ~RM40bn | ~RM60bn | Diesel cut in June saved RM4bn/yr |
| 2025 | ~RM20bn (petrol only) | ~RM40bn | RON95 capped at 300L/month |
| Mar 2026 | RM3.2bn/month | - | Hormuz crisis ballooned costs |

## Savings from Reforms
| Reform | Date | Annual Saving |
|---|---|---|
| Diesel subsidy removed (Peninsular) | Jun 2024 | RM4 billion |
| RON95 capped at 300L/month | Sep 2025 | ~RM4.2 billion (revised down) |
| Original plan: full top 15% removal | SHELVED | Would have saved RM8bn |

## Budget Deficit
| Year | Deficit (% GDP) | Gov't Debt (% GDP) |
|---|---|---|
| 2022 | 5.6% | 69.6% |
| 2023 | 5.0% | 70.0% |
| 2024 | 4.36% | 66.86% (IMF: 70.0%) |
| 2025 | ~3.8% | 70.2% |
| 2026 (budget) | ~3.5% | 70.2% |

## Fiscal Space Summary
- Debt at 70%+ of GDP (above self-imposed 65% legal limit)
- Deficit narrowing but still above 3%
- 2026 budget: "hit the brakes on new taxes and subsidy cuts" (Straits Times)
- Pre-election budget: no new taxes, RM100 cash handout to every adult
- Credit rating: S&P A- stable, Moody's A3 stable, Fitch BBB+ stable
- RM124bn in foreign reserves

## Key Insight for Election Timing
- Subsidy reforms have ONLY saved ~RM8bn total — not enough for major pre-election spending
- RON95 full removal still pending — the BIG one (RM52bn/year if removed)
- Government is kicking the can: calling election BEFORE full subsidy removal
- Pattern: Najib cut subsidies AFTER GE13, Anwar delaying until after GE16
"""
path = os.path.join(BASE, "dosm", "fuel_prices", "subsidy_budget_analysis.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(subsidy)
print(f"Saved: subsidy_budget_analysis.md")

# === Early Election Motives ===
early = """# Early Election Motives Analysis

Source: Wikipedia, news articles, Oust Anwar rally

## Historical Pattern
| PM | Election | Unpopular Policy | Came Before or After? |
|---|---|---|---|
| Najib Razak | GE13 (May 2013) | Fuel subsidy cuts, GST | AFTER election |
| Najib Razak | GE14 (May 2018) | GST remained | DURING term |
| Anwar Ibrahim | GE16 (?) | RON95 subsidy removal | BEFORE (likely) |

Pattern: Malaysian PMs call elections BEFORE implementing painful reforms.

## Oust Anwar Rally (26 Jul 2025)
- 18,000-25,000 protesters (govt estimate)
- Causes: subsidy cuts, URA, SST, rising prices
- Concessions won: RON95 cut to RM1.99/L, RM100 cash to all adults (RM2.2bn)
- Shows government is VULNERABLE to street pressure

## Factors Favoring Early Election (2026)
| Factor | Details |
|---|---|
| RON95 subsidy removal pending | Will be unpopular — better to vote before cutting |
| Opposition fragmented | PAS-BERSATU split, WAWASAN forming |
| Oil revenue high | War-driven surge in Petronas dividends |
| Economy looks good | GDP ~5%, low unemployment, ringgit recovering |
| PH-BN pact fraying | May not survive until 2027 |
| Rafizi defection (BERSAMA) | New party needs time to organize — strike before they're ready |

## Factors Against Early Election
| Factor | Details |
|---|---|
| Oust Anwar rally showed anger | Voters already unhappy despite subsidies |
| Redelineation not done | New boundaries could help PH |
| State elections (Johor Jul 11) | May want to see results first |
| Anwar prefers full term | Public statements suggest he wants to wait |

## Bottom Line
The strongest argument for a 2026 election is: **call it before the pain hits.** Voters haven't felt full RON95 removal yet. The Iran war is generating revenue today. If peace comes and oil drops, the fiscal picture worsens AND voters will demand cheaper fuel. Strike while the iron is hot.
"""
path = os.path.join(BASE, "elections", "timing", "early_election_motives.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(early)
print(f"Saved: early_election_motives.md")

# === Also save to insights as clean analysis ===
insights_base = os.path.join(os.path.dirname(__file__), "..", "insights")
combined_summary_add = """# Additional Analysis: Iran War, Subsidies & Early Election Motives

## Oil & Iran War Impact
- Current oil prices surging due to Iran war + Hormuz blockade -> BENEFITS Malaysia fiscally
- Peace deal would open Hormuz, flood market with Iranian oil -> oil prices DROP -> hurts Petronas revenue
- Anwar has fiscal incentive to call election BEFORE peace deal

## Subsidy Reform Status
- Diesel reform saved RM4bn/yr (Jun 2024) ✓ done
- RON95 partial reform saved RM4.2bn/yr (Sep 2025) ✓ done  
- Full RON95 top-15% removal = RM8bn savings ✗ SHELVED
- This is the ticking time bomb: voters haven't felt the full pain yet

## Fiscal Position
- Deficit: 5.6% (2022) -> 3.5% (2026 budget) - IMPROVING
- Debt: 70% of GDP - STABLE but high
- Pre-election budget: no new taxes, cash handouts
- Limited space for big spending: RM8bn savings from reforms is modest

## Early Election Case
The government has strong incentive to call GE16 in 2026 BEFORE:
1. Full RON95 subsidy removal takes effect
2. PH-BN cooperation collapses further
3. Peace deal drops oil prices and Petronas revenue
4. Opposition (WAWASAN, BERSAMA) organizes for 2027
5. Global inflation from Iran war hits Malaysian consumers

## Updated GE16 Prediction
If Anwar chooses early election: **Nov-Dec 2026** (after Johor/NS state elections done, before monsoon fully sets in)
If Anwar waits: **Jul-Sep 2027** (best weather, after state elections)
"""
path = os.path.join(insights_base, "combined", "iran_subsidy_early_election.md")
with open(path, "w", encoding="utf-8") as f:
    f.write(combined_summary_add)
print(f"Saved: insights/combined/iran_subsidy_early_election.md")

# === Also update the main timing synthesis ===
synthesis_path = os.path.join(BASE, "elections", "timing", "ge16_complete_synthesis.md")
if os.path.exists(synthesis_path):
    with open(synthesis_path, "a", encoding="utf-8") as f:
        f.write("""

## Updated Analysis (Jun 2026): Iran War, Subsidies & Early Election

### New Factors
- US-Iran war (Feb-Apr 2026) drove oil to $120+ briefly
- Peace deal impending could crash oil prices, reducing fiscal space
- Subsidy reforms saved only ~RM8bn — not enough for pre-election splurge
- Oust Anwar rally (Jul 2025) showed government vulnerable to street pressure

### Revised Scenarios
| Scenario | Probability | Timing | Logic |
|---|---|---|---|
| Early election | ~30% | Nov-Dec 2026 | Before oil drops, before subsidy pain, while opposition divided |
| Full term (was 60%) | ~50% | Jul-Sep 2027 | Best weather, after state elections, redelineation done |
| Late/Deadline | ~15% | Jan-Feb 2028 | Last resort, monsoon risk |
| Snap (crisis) | ~5% | Before Nov 2026 | Coalition collapse (unlikely) |

### Key Uncertainty
The Iran peace deal timing is the wildcard. If deal happens in mid-2026, oil could drop to $60-70 by late 2026, sharply reducing Petronas dividends. Anwar's fiscal space would shrink just as he needs to fund campaign spending. This strongly favors a **late 2026 election**.
""")
print(f"Updated: ge16_complete_synthesis.md")

print("\nAll done!")
