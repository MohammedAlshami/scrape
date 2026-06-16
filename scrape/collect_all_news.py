"""Collect news from ALL sources - existing + new RSS scrapers."""

import json, sys, os, time
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from tools.news.sources import SCRAPERS

BASE = os.path.join(ROOT, "data", "news")
os.makedirs(BASE, exist_ok=True)

# All sources to try, ordered by reliability
ALL_SOURCES = [
    # Existing (tested working)
    "dayakdaily",
    "astroawani",
    "nst",
    "fmt",
    "thevibes",
    "borneopost",
    "sinarharian",
    "hmetro",
    "malaymail",
]

all_articles = []
article_urls = set()
stats = {}

for src_name in ALL_SOURCES:
    print(f"\n=== {src_name} ===")
    try:
        scraper = SCRAPERS[src_name]()
    except Exception as e:
        print(f"  Init FAIL: {e}")
        continue
    
    try:
        results = scraper.search("", max_results=6)
    except Exception as e:
        print(f"  Search FAIL: {e}")
        continue
    
    if not results:
        print(f"  No results")
        continue
    
    count = 0
    for r in results:
        if r.url in article_urls:
            continue
        
        try:
            art = scraper.get_article(r.url)
        except:
            art = None
        
        if not art or not art.title:
            # Still save what we have from RSS metadata
            article = {
                "title": r.title,
                "url": r.url,
                "source": src_name,
                "published_at": str(r.published_at) if r.published_at else None,
                "author": "",
                "categories": [],
                "summary": (r.summary or "")[:500],
                "content_len": 0,
            }
            if r.url not in article_urls:
                all_articles.append(article)
                article_urls.add(r.url)
                count += 1
                stats[src_name] = stats.get(src_name, 0) + 1
                print(f"  [{count}] {r.title[:65]} | metadata only")
                if count >= 5:
                    break
            continue
        
        article = {
            "title": art.title,
            "url": art.url,
            "source": art.source,
            "published_at": str(art.published_at) if art.published_at else None,
            "author": art.author or "",
            "categories": art.categories,
            "summary": (art.summary or "")[:500],
            "content_len": len(art.content),
        }
        
        all_articles.append(article)
        article_urls.add(r.url)
        count += 1
        stats[src_name] = stats.get(src_name, 0) + 1
        print(f"  [{count}] {art.title[:65]} | content={len(art.content)}")
        
        if count >= 5:
            break
        
        time.sleep(0.5)
    
    # Save progress
    with open(os.path.join(BASE, "news_in_progress.json"), "w", encoding="utf-8") as f:
        json.dump({"articles": all_articles}, f, indent=2, ensure_ascii=False)

# Save this batch
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
batch_file = os.path.join(BASE, f"news_all_sources_{ts}.json")
with open(batch_file, "w", encoding="utf-8") as f:
    json.dump({"collected_at": str(datetime.now()), "articles": all_articles}, f, indent=2, ensure_ascii=False)

# Merge into master index
index_path = os.path.join(BASE, "news_index.json")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        index = json.load(f)
    existing = {a["url"] for a in index["articles"]}
    for a in all_articles:
        if a["url"] not in existing:
            index["articles"].append(a)
    index["articles"].sort(key=lambda x: x.get("published_at") or "", reverse=True)
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    total = len(index["articles"])
else:
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump({"collected_at": str(datetime.now()), "articles": all_articles}, f, indent=2, ensure_ascii=False)
    total = len(all_articles)

print(f"\n{'='*50}")
print(f"This batch: {len(all_articles)} articles")
for k, v in sorted(stats.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
print(f"Total in index: {total}")
print(f"Saved: {batch_file}")
