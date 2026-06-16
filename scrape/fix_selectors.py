"""Fix Vibes scraper - find correct content selector."""
import requests
from bs4 import BeautifulSoup

H = {"User-Agent": "ElectionPredictionBot/1.0"}

# Test The Vibes
url = "https://www.thevibes.com/articles/news/116210/minister-sarawak-made-right-decision-to-reject-entry-of-rohingya"
r = requests.get(url, headers=H, timeout=10)
soup = BeautifulSoup(r.text, "lxml")

print("=== Checking selectors ===")
for sel in ["article", "main", ".article-content", ".content", "#content", "div.lg\\:container"]:
    el = soup.select_one(sel)
    if el:
        txt = el.get_text(strip=True)
        print(f"  '{sel}': {len(txt)} chars - {txt[:80]}")
    else:
        print(f"  '{sel}': NOT FOUND")

# Check NST
print("\n=== NST ===")
url = "https://www.nst.com.my/news/nation/2026/06/1464274/malaysia-timor-leste-ties-exceptionally-good-says-ramos-horta"
r = requests.get(url, headers=H, timeout=10)
soup = BeautifulSoup(r.text, "lxml")
print(f"  Status: {r.status_code}")
for sel in ["article", "main", ".node__content", ".content", ".field--name-body"]:
    el = soup.select_one(sel)
    if el:
        txt = el.get_text(strip=True)
        print(f"  '{sel}': {len(txt)} chars")
    else:
        print(f"  '{sel}': NOT FOUND")

# Check HMetro
print("\n=== Harian Metro ===")
url = "https://www.hmetro.com.my/utama/2026/06/1370491/tuhan-satukan-kami-untuk-saling-melengkapi"
r = requests.get(url, headers=H, timeout=10)
soup = BeautifulSoup(r.text, "lxml")
print(f"  Status: {r.status_code}")
for sel in ["article", "main", ".story-content", ".content-article", ".field--name-body", ".page-collection-utama"]:
    el = soup.select_one(sel)
    if el:
        txt = el.get_text(strip=True)
        print(f"  '{sel}': {len(txt)} chars")
    else:
        print(f"  '{sel}': NOT FOUND")
