"""Download 2026 state election pages."""

import requests, os, time

HEADERS = {"User-Agent": "ElectionPredictionBot/1.0"}
BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "elections")

pairs = [
    ("state_johor_2026", "2026_Johor_state_election", "2026_Johor_state_election"),
    ("state_ns_2026", "2026_Negeri_Sembilan_state_election", "2026_Negeri_Sembilan_state_election"),
]

for folder, fname, title in pairs:
    path = os.path.join(BASE, folder)
    os.makedirs(path, exist_ok=True)
    
    url = f"https://en.wikipedia.org/w/index.php?title={title}&action=raw"
    print(f"Fetching: {title}")
    resp = requests.get(url, timeout=15, headers=HEADERS)
    
    if resp.status_code == 200:
        fpath = os.path.join(path, f"{fname}.md")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(f"# {fname}\n\n*Source: https://en.wikipedia.org/wiki/{title}*\n\n---\n\n{resp.text}")
        print(f"  Saved: {len(resp.text)} chars")
    else:
        print(f"  FAIL: {resp.status_code}")
    
    time.sleep(0.5)

print("\nDone!")
