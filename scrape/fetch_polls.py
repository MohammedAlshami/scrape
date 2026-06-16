"""Save Merdeka Center and approval ratings data."""

import requests, os

HEADERS = {"User-Agent": "ElectionPredictionBot/1.0"}
BASE = os.path.join(os.path.dirname(__file__), "..", "data", "polls")
os.makedirs(BASE, exist_ok=True)

pages = {
    "Merdeka Center": "Merdeka_Center",
    "List of heads of the executive by approval rating": "List_of_heads_of_the_executive_by_approval_rating",
}

for name, title in pages.items():
    url = f"https://en.wikipedia.org/w/index.php?title={title}&action=raw"
    resp = requests.get(url, timeout=15, headers=HEADERS)
    if resp.status_code == 200:
        fname = name.replace(" ", "_").replace("(", "").replace(")", "")
        path = os.path.join(BASE, f"{fname}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {name}\n\n*Source: https://en.wikipedia.org/wiki/{title}*\n\n---\n\n{resp.text}")
        print(f"Saved: {fname}.md ({len(resp.text)} chars)")
    else:
        print(f"FAIL {resp.status_code}: {name}")

summary = """# Malaysian Approval Ratings Summary

Source: Merdeka Center (https://www.merdeka.org)

## Anwar Ibrahim Approval Rating
- Feb 2023: 68%
- Dec 2024 (Year 2 of Madani govt): 54% (up from 50% in Year 1)

## Federal Government Approval Rating
- Dec 2024: 51% (up from 46% in Year 1)

## Notes
- Merdeka Center founded 2003 by Ibrahim Suffian & Hazman Hamid
- Predicted 2013 GE popular vote within 0.1% accuracy
- Predicted 2022 GE seats within 1 seat accuracy
- No centralized Wikipedia page for Malaysian PM approval ratings exists
- Malaysia not included in global "List of heads of the executive by approval rating" table
"""
path = os.path.join(BASE, "approval_ratings_summary.md")
with open(path, "w") as f:
    f.write(summary)
print(f"Saved: approval_ratings_summary.md")
print("Done!")
