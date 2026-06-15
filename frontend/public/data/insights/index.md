# Insights Directory

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
| economy/gdp_annual.csv | 134 | 1947-2025 |
| economy/gdp_quarterly.csv | 260 | 1991-2026 |
| economy/inflation_annual.csv | 545 | 1961-2025 |
| economy/inflation_overall.csv | 65 | 1961-2025 |
| economy/unemployment_monthly.csv | 196 | 2010-2026 |
| economy/fuel_prices_weekly.csv | 929 | 2017-2026 |
| economy/brent_crude_daily.csv | 4700 | 2007-2026 |
| economy/myr_usd_monthly.csv | 8096 | 1997-2026 |
| economy/opr_base_rate.csv | 44 | 1997-2025 |
| elections/ge_turnout.csv | 15 | 1959-2022 |
| elections/ge15_pendulum.csv | 222 | 2022 |
| elections/by_elections_2023_2026.csv | 13 | 2023-2026 |
| polls/approval_ratings.csv | 8 | 2018-2025 |
| market/klse_daily.csv | 330 | 1999-2026 |
| combined/election_timing_factors.csv | 27 | 1999-2025 |

## Next Steps
1. Add qualitative analysis from news articles (sentiment scores)
2. Enrich with approval rating changes before each election
3. Build prediction model using combined/election_timing_factors.csv
