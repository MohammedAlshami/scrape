"""Check AstroAwani RSS and scrape more news."""

import requests
from bs4 import BeautifulSoup

H = {"User-Agent": "Mozilla/5.0"}

# Check for RSS links on AstroAwani
r = requests.get("https://www.astroawani.com", headers=H, timeout=10)
soup = BeautifulSoup(r.text, "lxml")

print("=== RSS/Feed links ===")
for link in soup.find_all("link", type=lambda t: t and ("rss" in t or "atom" in t or "xml" in t)):
    print(f"  Link: {link.get('href')}")

for a in soup.find_all("a", href=True):
    h = a["href"].lower()
    if "rss" in h or "feed" in h:
        print(f"  Anchor: {a['href']}")

# Try alternative RSS URLs
print("\n=== Trying RSS URLs ===")
for url in [
    "https://www.astroawani.com/rss/berita-politik",
    "https://www.astroawani.com/rss/berita-malaysia",
    "https://feeds.astroawani.com/rss",
    "https://www.astroawani.com/feeds/rss",
]:
    r = requests.get(url, headers=H, timeout=10)
    content_type = r.headers.get("Content-Type", "")
    is_xml = "xml" in content_type or r.text.strip().startswith("<?xml")
    print(f"  {url}: {r.status_code}, xml={is_xml}, len={len(r.text)}")
