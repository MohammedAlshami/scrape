"""Test all new RSS scrapers."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.news.sources.rss_scrapers import NST, FMT, VIBES, BORNEO_POST, SINAR_HARIAN, HARIAN_METRO

sources = [
    ("NST", NST),
    ("FMT", FMT),
    ("The Vibes", VIBES),
    ("Borneo Post", BORNEO_POST),
    ("Sinar Harian", SINAR_HARIAN),
    ("Harian Metro", HARIAN_METRO),
]

for name, scraper in sources:
    print(f"\n=== {name} ===")
    results = scraper.search(max_results=3)
    if not results:
        print(f"  No results!")
        continue
    print(f"  Found {len(results)} articles")
    for r in results[:2]:
        art = scraper.get_article(r.url)
        if art:
            print(f"  OK: {art.title[:60]} | {len(art.content)} blocks | {art.source}")
        else:
            print(f"  FAIL: could not fetch {r.url[:60]}")

print("\nDone!")
