"""Collect political news from working sources (DayakDaily, AstroAwani)."""

import json, sys, os
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from tools.news.sources import SCRAPERS

BASE = os.path.join(ROOT, "data", "news")
os.makedirs(BASE, exist_ok=True)

TOPICS = [
    "GE16 general election",
    "Anwar Ibrahim government",
    "unity government",
    "Pakatan Harapan Malaysia",
    "Barisan Nasional Malaysia",
    "Perikatan Nasional Malaysia",
    "PAS Malaysia",
    "BERSATU Malaysia",
    "UMNO Malaysia",
    "DAP Malaysia",
    "by-election Malaysia",
    "Sabah state election",
    "fuel subsidy Malaysia",
    "Madani government",
    "Malaysia inflation economy",
    "ringgit Malaysia",
    "opposition Malaysia politics",
    "BNM OPR",
    "Cabinet Malaysia",
    "Sarawak state election",
]

# Only use sources with working search
SOURCES = ["dayakdaily", "astroawani"]
MAX_PER_TOPIC = 4

def slug(s):
    return s.lower().replace(" ", "_").replace("/", "_").replace("&", "and")[:50]

all_articles = []
article_urls = set()
stats = {s: 0 for s in SOURCES}

for topic in TOPICS:
    topic_slug = slug(topic)
    print(f"\n--- {topic} ---")
    
    for src_name in SOURCES:
        try:
            scraper = SCRAPERS[src_name]()
        except Exception as e:
            print(f"  [{src_name}] Init: {e}")
            continue
        
        print(f"  [{src_name}] searching...", end=" ")
        try:
            summaries = scraper.search(topic, max_results=MAX_PER_TOPIC)
        except Exception as e:
            print(f"ERR: {e}")
            continue
        
        if not summaries:
            print("no results")
            continue
        
        print(f"{len(summaries)} articles")
        
        for s in summaries:
            if s.url in article_urls:
                continue
            
            try:
                art = scraper.get_article(s.url)
            except:
                continue
            
            if not art or not art.title:
                continue
            
            article = {
                "title": art.title,
                "url": art.url,
                "source": art.source,
                "published_at": str(art.published_at) if art.published_at else None,
                "author": art.author or "",
                "categories": art.categories,
                "summary": (art.summary or "")[:500],
                "topic": topic,
            }
            
            all_articles.append(article)
            article_urls.add(art.url)
            stats[src_name] += 1
            print(f"    [{stats[src_name]}] {art.title[:70]}")
    
    # Save progress after each topic
    temp_path = os.path.join(BASE, "news_in_progress.json")
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump({"collected_at": str(datetime.now()), "articles": all_articles}, f, indent=2, ensure_ascii=False)

# Final save
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
final_path = os.path.join(BASE, f"news_{timestamp}.json")
latest_path = os.path.join(BASE, "news_index.json")

with open(final_path, "w", encoding="utf-8") as f:
    json.dump({"collected_at": str(datetime.now()), "articles": all_articles}, f, indent=2, ensure_ascii=False)

with open(latest_path, "w", encoding="utf-8") as f:
    json.dump({"collected_at": str(datetime.now()), "articles": all_articles}, f, indent=2, ensure_ascii=False)

print(f"\n{'='*50}")
print(f"Collection complete!")
print(f"  Topics: {len(TOPICS)}")
for s in SOURCES:
    print(f"  {s}: {stats[s]} articles")
print(f"  Unique articles: {len(all_articles)}")
print(f"  Saved: {latest_path}")
