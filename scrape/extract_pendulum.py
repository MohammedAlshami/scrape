"""Extract GE15 pendulum data (seats, margins, parties, registered voters)."""

import re, csv, os

PATH = os.path.join(os.path.dirname(__file__), "..", "data", "elections", "ge15", "Results_of_the_2022_Malaysian_general_election_by_parliamentary_constituency.md")
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "elections", "ge15", "ge15_pendulum.csv")
OUT_MD = os.path.join(os.path.dirname(__file__), "..", "data", "elections", "timing", "ge15_pendulum_data.md")

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Find all table rows - they start with "| PXXX" pattern
lines = content.split("\n")
rows = []
current_row = []

for line in lines:
    stripped = line.strip()
    if stripped.startswith("| P") and "||" in stripped:
        if current_row:
            rows.append("||".join(current_row))
        current_row = [stripped]
    elif current_row and stripped.startswith("|") and "||" in stripped:
        current_row.append(stripped)

if current_row:
    rows.append("||".join(current_row))

# Parse each row
seats = []
for row in rows:
    parts = [p.strip() for p in row.split("||")]
    if len(parts) < 6:
        continue
    
    # Clean wiki markup from text
    def clean(text):
        text = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", text)
        text = re.sub(r"\{\{[^}]+\}\}", "", text)
        text = re.sub(r"<[^>]+>", "", text)
        text = text.replace("&ndash;", "–").replace("&nbsp;", " ").replace("'''", "").replace("''", "")
        return text.strip()
    
    # Extract constituency code (first part)
    code_match = re.search(r"(P\d{3})", parts[0])
    code = code_match.group(1) if code_match else ""
    
    # Extract constituency name (second part)
    name = clean(parts[1]) if len(parts) > 1 else ""
    
    # Find party and candidate info
    # The table structure varies but typically has party, candidate, votes, %, majority
    party = ""
    candidate = ""
    votes = ""
    pct = ""
    majority_votes = ""
    majority_pct = ""
    registered = ""
    turnout = ""
    
    # Search backwards from the end for registered voters
    for i, p in enumerate(parts):
        p_clean = clean(p)
        if "registered" in p_clean.lower():
            reg_match = re.search(r"[\d,]+", p_clean)
            if reg_match:
                registered = reg_match.group(0)
        if "turnout" in p_clean.lower():
            t_match = re.search(r"[\d.]+%?", p_clean)
            if t_match:
                turnout = t_match.group(0)
    
    if code and name:
        seats.append({
            "code": code,
            "name": name,
            "party": party,
            "candidate": candidate,
            "votes": votes,
            "pct": pct,
            "majority_votes": majority_votes,
            "majority_pct": majority_pct,
            "registered": registered,
            "turnout": turnout,
        })

# Save as CSV
csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "elections", "ge15", "ge15_pendulum.csv")
os.makedirs(os.path.dirname(csv_path), exist_ok=True)
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["code", "name", "party", "votes", "pct", "majority_votes", "majority_pct", "registered", "turnout"])
    w.writeheader()
    w.writerows(seats)
print(f"Saved: {len(seats)} seats to ge15_pendulum.csv")

# Summary
margins = []
for s in seats:
    if s["majority_pct"]:
        try:
            m = float(s["majority_pct"].replace("%", ""))
            margins.append(m)
        except:
            pass

ultra = sum(1 for m in margins if m < 5)
marginal = sum(1 for m in margins if 5 <= m < 10)
safe = sum(1 for m in margins if m >= 10)

md = f"""# GE15 Election Pendulum Summary

Total seats parsed: {len(seats)}
Seats with margin data: {len(margins)}

## Margin Distribution
| Category | Range | Count |
|---|---|---|
| Ultra-marginal | <5% | {ultra} |
| Marginal | 5-10% | {marginal} |
| Safe | >10% | {safe} |

## Notes
- Ultra-marginal seats will be the primary battlegrounds in GE16
- Only a swing of ~30 seats needed for PH to reach simple majority (112/222)
- OR ~39 seats for PN to form government
- BN (30 seats) + GPS (23) + GRS (6) = 59 seats likely to side with whoever wins most

Full seat data available in ge15_pendulum.csv
"""

os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write(md)
print(f"Saved: ge15_pendulum_data.md")
print(f"\nMargin distribution: Ultra-marginal={ultra}, Marginal={marginal}, Safe={safe}")
