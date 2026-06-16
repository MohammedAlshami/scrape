"""Check what HTML structure Vibes and NST actually have."""
import requests
from bs4 import BeautifulSoup

H = {"User-Agent": "ElectionPredictionBot/1.0"}

for name, url in [
    ("Vibes", "https://www.thevibes.com/articles/news/116210/minister-sarawak-made-right-decision-to-reject-entry-of-rohingya"),
    ("NST", "https://www.nst.com.my/news/nation/2026/06/1464274/malaysia-timor-leste-ties-exceptionally-good-says-ramos-horta"),
]:
    print(f"\n=== {name} ===")
    r = requests.get(url, headers=H, timeout=10)
    soup = BeautifulSoup(r.text, "lxml")
    
    # Show all tag names with their classes and text length
    for tag in soup.find_all(True):
        cls = tag.get("class", [])
        txt = tag.get_text(strip=True)
        if len(txt) > 200:
            print(f"  <{tag.name}> .{'.'.join(cls) if cls else ''} -> {len(txt)} chars")
            print(f"    Text starts: {txt[:100]}")
            break
    else:
        print("  No element with >200 chars found")
