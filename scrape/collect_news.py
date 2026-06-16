"""Collect political news articles using existing scraper tools."""

import json, sys, os
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from tools.news.sources import SCRAPERS

BASE = os.path.join(ROOT, "data", "news")
os.makedirs(BASE, exist_ok=True)

TOPICS = [
    # Election timing & speculation
    "GE16",
    "general election 2026",
    "snap election Malaysia",
    
    # PM & government
    "Anwar Ibrahim government",
    "unity government",
    "Anwar approval rating",
    
    # Political parties
    "Pakatan Harapan",
    "Barisan Nasional",
    "Perikatan Nasional",
    "PAS",
    "BERSATU",
    "PKR",
    "DAP",
    "AMANAH",
    "UMNO",
    "MUDA",
    
    # By-elections & state elections
    "by-election",
    "Sabah election",
    
    # Policy & economy
    "budget 2026",
    "fuel subsidy",
    "Madani",
    "inflation Malaysia",
    "ringgit",
    "subsidi",
    
    # Opposition
    "opposition Malaysia",
    "Green Wave",
    "PN",
]

SOURCES = ["malaymail", "astroawani", "sinardaily", "dayakdaily"]
MAX_PER_TOPIC = 6  # articles per source per topic

def slug(s):
    return s.lower().replace(" ", "_").replace("/", "_").replace("&", "and")[:50]

all_articles = []
stats = {s: 0 for s in SOURCES}
stats["total"] = 0
stats["topics"] = 0

for topic in TOPICS:
    topic_slug = slug(topic)
    stats["topics"] += 1
    print(f"\n--- Topic: {topic} ---")
    
    for src_name in SOURCES:
        try:
            scraper = SCRAPERS[src_name]()
        except Exception as e:
            print(f"  [{src_name}] Init error: {e}")
            continue
        
        print(f"  [{src_name}] Searching...", end=" ")
        try:
            summaries = scraper.search(topic, max_results=MAX_PER_TOPIC)
        except Exception as e:
            print(f"search failed: {e}")
            continue
        
        if not summaries:
            print("no results")
            continue
        
        print(f"{len(summaries)} results, fetching articles...")
        
        for s in summaries:
            try:
                art = scraper.get_article(s.url)
            except Exception as e:
                print(f"    fetch failed: {e}")
                continue
            
            if not art:
                continue
            
            article = {
                "title": art.title,
                "url": art.url,
                "source": art.source,
                "published_at": str(art.published_at) if art.published_at else None,
                "author": art.author or "",
                "categories": art.categories,
                "summary": art.summary or "",
                "topic": topic,
            }
            
            all_articles.append(article)
            stats[src_name] += 1
            stats["total"] += 1
            print(f"    [OK] {art.title[:60]}")

# Save all results
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
index_path = os.path.join(BASE, f"news_index_{timestamp}.json")
with open(index_path, "w", encoding="utf-8") as f:
    json.dump({"collected_at": timestamp, "articles": all_articles}, f, indent=2, ensure_ascii=False)

# Also save latest as news_index.json for easy reference
latest_path = os.path.join(BASE, "news_index.json")
with open(latest_path, "w", encoding="utf-8") as f:
    json.dump({"collected_at": timestamp, "articles": all_articles}, f, indent=2, ensure_ascii=False)

print(f"\n{'='*50}")
print(f"Collection complete!")
print(f"  Topics searched: {stats['topics']}")
print(f"  Sources used: {len(SOURCES)}")
for s in SOURCES:
    print(f"  {s}: {stats[s]} articles")
print(f"  Total articles: {stats['total']}")
print(f"  Saved to: {latest_path}")
print(f"  Backup: {index_path}")
