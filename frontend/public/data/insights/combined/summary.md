# Combined Dataset for AI Modeling

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
