"""Collect news via RSS feeds for reliable article discovery."""

import json, sys, os, time, re
from datetime import datetime
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import requests
from tools.news.sources import SCRAPERS

BASE = os.path.join(ROOT, "data", "news")
os.makedirs(BASE, exist_ok=True)

session = requests.Session()
session.headers.update({"User-Agent": "ElectionPredictionBot/1.0"})

RSS_FEEDS = {
    "malaymail": "https://www.malaymail.com/feed/rss",
    "astroawani": "https://www.astroawani.com/rss",
    "dayakdaily": "https://dayakdaily.com/feed/",
}

POLITICAL_KEYWORDS = [
    "election", "pilihan raya", "PRU", "GE1", "PRN",
    "Anwar", "PM", "prime minister", "perdana menteri",
    "government", "kerajaan", "unity", "perpaduan",
    "Pakatan", "Harapan", "Barisan", "Nasional", "Perikatan",
    "UMNO", "PAS", "PKR", "DAP", "BERSATU", "AMANAH", "GPS", "GRS",
    "MUDA", "Warisan", "Pejuang",
    "parliament", "parlimen", "Dewan Rakyat",
    "minister", "menteri", "cabinet", "kabinet",
    "budget", "belanjawan",
    "subsidy", "subsidi",
    "Madani",
    "opposition", "pembangkang",
    "by-election", "pilihan raya kecil",
    "vote", "undi", "polling",
    "approval rating",
    "policy", "dasar",
    "reform", "reformasi",
    "corruption", "rasuah",
    "economy", "ekonomi",
    "inflation", "inflasi",
    "ringgit",
    "BNM", "OPR", "bank negara",
    "Sabah", "Sarawak",
    "Chinese", "Indian", "Malay", "Bumiputera",
    "fuel", "minyak", "RON95", "diesel",
    "constitution", "perlembagaan",
    "royal", "Agong", "king", "yang di-pertuan",
    "pandemic", "COVID", "health",
    "education", "pendidikan",
    "flood", "banjir",
    "housing", "perumahan",
    "tax", "cukai", "GST", "SST",
]

def is_political(title, summary=""):
    text = (title + " " + summary).lower()
    for kw in POLITICAL_KEYWORDS:
        if kw.lower() in text:
            return True
    return False

def parse_rss(xml_text):
    root = ET.fromstring(xml_text)
    items = []
    for item in root.findall(".//item"):
        title = item.findtext("title", "")
        link = item.findtext("link", "")
        pub_date = item.findtext("pubDate", "")
        description = item.findtext("description", "")
        items.append({"title": title, "url": link, "date": pub_date, "summary": description})
    return items

all_articles = []
article_urls = set()
stats = {}

for src_name, feed_url in RSS_FEEDS.items():
    print(f"\n=== {src_name} RSS ===")
    try:
        r = session.get(feed_url, timeout=15)
        r.raise_for_status()
        items = parse_rss(r.text)
    except Exception as e:
        print(f"  RSS FAIL: {e}")
        continue
    
    print(f"  {len(items)} items in feed")
    
    political = [it for it in items if is_political(it["title"], it["summary"])]
    print(f"  {len(political)} political items")
    
    scraper = SCRAPERS.get(src_name)
    if scraper:
        scraper = scraper()
    
    count = 0
    for item in political:
        if item["url"] in article_urls:
            continue
        
        try:
            if scraper:
                art = scraper.get_article(item["url"])
            else:
                art = None
        except Exception as e:
            print(f"  FETCH FAIL: {item['title'][:50]} - {e}")
            continue
        
        if not art or not art.title:
            article_urls.add(item["url"])
            continue
        
        article = {
            "title": art.title,
            "url": art.url,
            "source": art.source,
            "published_at": str(art.published_at) if art.published_at else None,
            "author": art.author or "",
            "categories": art.categories,
            "summary": (art.summary or "")[:500],
        }
        
        all_articles.append(article)
        article_urls.add(item["url"])
        count += 1
        stats[src_name] = stats.get(src_name, 0) + 1
        print(f"  [{count}] {art.title[:70]}")
        
        if count >= 8:
            break
        
        time.sleep(1)
    
    # Save progress
    with open(os.path.join(BASE, "news_in_progress.json"), "w", encoding="utf-8") as f:
        json.dump({"articles": all_articles}, f, indent=2, ensure_ascii=False)

# Final save
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
with open(os.path.join(BASE, f"news_rss_{ts}.json"), "w", encoding="utf-8") as f:
    json.dump({"collected_at": str(datetime.now()), "articles": all_articles}, f, indent=2, ensure_ascii=False)
with open(os.path.join(BASE, "news_rss.json"), "w", encoding="utf-8") as f:
    json.dump({"collected_at": str(datetime.now()), "articles": all_articles}, f, indent=2, ensure_ascii=False)

# Merge with previous news_index if it exists
prev_path = os.path.join(BASE, "news_index.json")
if os.path.exists(prev_path):
    with open(prev_path, "r", encoding="utf-8") as f:
        prev = json.load(f)
    existing_urls = {a["url"] for a in prev["articles"]}
    for a in all_articles:
        if a["url"] not in existing_urls:
            prev["articles"].append(a)
    with open(os.path.join(BASE, "news_index.json"), "w", encoding="utf-8") as f:
        json.dump(prev, f, indent=2, ensure_ascii=False)
    total = len(prev["articles"])
else:
    # Create combined index
    combined = {"collected_at": str(datetime.now()), "articles": all_articles}
    with open(os.path.join(BASE, "news_index.json"), "w", encoding="utf-8") as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)
    total = len(all_articles)

print(f"\n{'='*50}")
print(f"Done! RSS collected: {len(all_articles)} articles")
for k, v in sorted(stats.items()):
    print(f"  {k}: {v}")
print(f"Total in index: {total}")
