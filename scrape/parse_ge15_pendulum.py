"""Parse GE15 pendulum data from Wikipedia HTML."""

import requests, csv, os, re
from bs4 import BeautifulSoup

H = {"User-Agent": "ElectionPredictionBot/1.0"}
url = "https://en.wikipedia.org/wiki/Results_of_the_2022_Malaysian_general_election_by_parliamentary_constituency"
r = requests.get(url, headers=H, timeout=15)
soup = BeautifulSoup(r.text, "lxml")

# Find all tables - the seat results table is a large one with many rows
# Look for tables containing "P001" text
for table in soup.find_all("table"):
    if "P001" in table.get_text():
        rows = table.find_all("tr")
        print(f"Found results table: {len(rows)} rows")
        
        seats = []
        for row in rows:
            cells = row.find_all("td")
            if not cells:
                continue
            
            text_cells = [c.get_text(" ", strip=True) for c in cells]
            first_cell = text_cells[0] if text_cells else ""
            
            # Check if this is a seat row (starts with P followed by digits as the first meaningful text)
            p_match = re.match(r"(P\d{3})", first_cell)
            if not p_match:
                continue
            
            code = p_match.group(1)
            seat_data = {"code": code}
            
            # Extract data based on column position
            # Table structure: # | Constituency | Registered | Winner | Votes | Vote% | Majority | Opponent(s) | Votes | Vote% | Valid | Incumbent
            
            col_mapping = {
                0: "num",
                1: "constituency",
                2: "registered",
                3: "winner",
                4: "winner_votes",
                5: "winner_pct",
                6: "majority_votes",
                7: "opponent",
                8: "opponent_votes",
                9: "opponent_pct",
                10: "valid_votes",
                11: "incumbent",
            }
            
            for i, text in enumerate(text_cells):
                if i in col_mapping:
                    # Clean the text
                    text = re.sub(r"\s+", " ", text).strip()
                    if col_mapping[i] == "constituency":
                        # Remove the P code from name
                        text = re.sub(r"^P\d{3}\s*", "", text)
                    seat_data[col_mapping[i]] = text
            
            seats.append(seat_data)
        
        print(f"Parsed {len(seats)} seats")
        
        if seats:
            # Save as CSV
            base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "elections", "ge15")
            os.makedirs(base, exist_ok=True)
            
            csv_path = os.path.join(base, "ge15_pendulum.csv")
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["code", "constituency", "registered", "winner", "winner_votes", "winner_pct", "majority_votes", "opponent", "opponent_votes", "opponent_pct", "valid_votes", "incumbent"])
                for s in seats:
                    w.writerow([s.get(k, "") for k in ["code", "constituency", "registered", "winner", "winner_votes", "winner_pct", "majority_votes", "opponent", "opponent_votes", "opponent_pct", "valid_votes", "incumbent"]])
            print(f"Saved: {csv_path}")
            
            # Print sample
            print(f"\nSample seats:")
            for s in seats[:3]:
                m = s.get("majority_votes", "?")
                w = s.get("winner", "?")
                print(f"  {s['code']} {s.get('constituency','')[:20]}: Winner={w}, Majority={m}")
            
            # Margin distribution
            margins = []
            for s in seats:
                mpct = s.get("opponent_pct", "") or s.get("majority_votes", "") or ""
                # Try to extract a percentage
                pct_match = re.search(r"([\d.]+)%", mpct)
                if pct_match:
                    margins.append(float(pct_match.group(1)))
            
            if margins:
                print(f"\nMargin distribution (from opponent_pct):")
                print(f"  <5%: {sum(1 for m in margins if m < 5)} seats")
                print(f"  5-10%: {sum(1 for m in margins if 5 <= m < 10)} seats")
                print(f"  >10%: {sum(1 for m in margins if m >= 10)} seats")
                print(f"  Average margin: {sum(margins)/len(margins):.1f}%")
        
        break
else:
    print("Table with P001 not found")
    
    # Debug: print info about all large tables
    for i, table in enumerate(soup.find_all("table", class_=lambda c: c and "wikitable" in str(c))):
        print(f"Wiki table {i}:")
        for row in table.find_all("tr")[:3]:
            cells = row.find_all(["th", "td"])
            texts = [c.get_text(strip=True)[:30] for c in cells[:4]]
            print(f"  {texts}")
