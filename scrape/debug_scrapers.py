"""Debug failing scrapers - check page structure."""

import sys, os, requests
from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

H = {"User-Agent": "ElectionPredictionBot/1.0"}

# Test URLs from the RSS feeds
tests = [
    ("NST", "https://www.nst.com.my/news/nation/2026/06/1464274/malaysia-timor-leste-ties-exceptionally-good-says-ramos-horta"),
    ("FMT", "https://www.freemalaysiatoday.com/category/nation/2026/06/15/malaysia-upholds-principles-while-engaging-major-powers-says-anwar/"),
    ("Borneo Post", "https://www.theborneopost.com/2026/06/15/will-cannot-revoke-or-supersede-epf-nomination-epf-holders-reminded/"),
    ("H Metro", "https://www.hmetro.com.my/utama/2026/06/1370491/tuhan-satukan-kami-untuk-saling-melengkapi"),
    ("The Vibes", "https://www.thevibes.com/articles/news/116210/minister-sarawak-made-right-decision-to-reject-entry-of-rohingya"),
]

for name, url in tests:
    print(f"\n=== {name} ===")
    try:
        r = requests.get(url, headers=H, timeout=10)
        soup = BeautifulSoup(r.text, "lxml")
        print(f"  Status: {r.status_code}, Size: {len(r.text)}")
        print(f"  Title tag: {soup.title.string[:60] if soup.title else 'NONE'}")
        
        # Find likely article containers
        for cls in ["article", "content", "post-content", "entry-content", "node__content",
                     "field--name-body", "td-post-content", "story-content",
                     "article-body", "article-content", "main-content"]:
            el = soup.find(class_=cls)
            if el:
                text_len = len(el.get_text(strip=True))
                print(f"  class='{cls}': {text_len} chars")
        
        # Find all divs with significant content
        for div in soup.find_all("div"):
            txt = div.get_text(strip=True)
            if len(txt) > 500 and div.get("class"):
                print(f"  div.{'.'.join(div.get('class', []))}: {len(txt)} chars")
                break  # just show first big one
                
    except Exception as e:
        print(f"  ERROR: {e}")
