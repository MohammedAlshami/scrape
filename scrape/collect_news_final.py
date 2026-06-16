"""Final comprehensive news collection combining RSS + category pages."""

import json, sys, os, time, re
from datetime import datetime
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import requests
from bs4 import BeautifulSoup
from tools.news.sources import SCRAPERS

BASE = os.path.join(ROOT, "data", "news")
os.makedirs(BASE, exist_ok=True)

session = requests.Session()
session.headers.update({"User-Agent": "ElectionPredictionBot/1.0"})

all_articles = []
article_urls = set()
stats = {}

# =============================================
# 1. DayakDaily RSS
# =============================================
print("=== DayakDaily RSS ===")
try:
    r = session.get("https://dayakdaily.com/feed/", timeout=15)
    root = ET.fromstring(r.content)
    items = []
    for item in root.findall(".//item"):
        items.append({
            "title": item.findtext("title", ""),
            "url": item.findtext("link", ""),
        })
    print(f"  {len(items)} items")
    
    scraper = SCRAPERS["dayakdaily"]()
    count = 0
    for item in items:
        if item["url"] in article_urls:
            continue
        try:
            art = scraper.get_article(item["url"])
        except:
            continue
        if not art or not art.title:
            continue
        all_articles.append({
            "title": art.title, "url": art.url, "source": art.source,
            "published_at": str(art.published_at) if art.published_at else None,
            "author": art.author or "", "categories": art.categories,
            "summary": (art.summary or "")[:500],
        })
        article_urls.add(item["url"])
        count += 1
        stats["dayakdaily_rss"] = stats.get("dayakdaily_rss", 0) + 1
        print(f"  [{count}] {art.title[:70]}")
        if count >= 8:
            break
        time.sleep(1)
except Exception as e:
    print(f"  FAIL: {e}")

# =============================================
# 2. MalayMail RSS
# =============================================
print("\n=== MalayMail RSS ===")
try:
    r = session.get("https://www.malaymail.com/feed/rss", timeout=15)
    root = ET.fromstring(r.content)
    items = []
    for item in root.findall(".//item"):
        items.append({
            "title": item.findtext("title", ""),
            "url": item.findtext("link", ""),
        })
    print(f"  {len(items)} items")
    
    kw = ["election", "anwar", "government", "mahathir", "najib", "parliament",
          "minister", "cabinet", "budget", "malaysia politics", "party", "umno",
          "pas", "pkr", "dap", "bersatu", "ph", "bn", "pn", "ringgit", "economy",
          "subsidy", "madani", "by-election", "opposition", "corruption", "1mdb",
          "sabah", "sarawak", "und18", "voter", "reformasi", "mahathir", "anwar"]
    
    scraper = SCRAPERS["malaymail"]()
    count = 0
    for item in items:
        title_lower = item["title"].lower()
        if not any(k in title_lower for k in kw):
            continue
        if item["url"] in article_urls:
            continue
        try:
            art = scraper.get_article(item["url"])
        except:
            continue
        if not art or not art.title:
            continue
        all_articles.append({
            "title": art.title, "url": art.url, "source": art.source,
            "published_at": str(art.published_at) if art.published_at else None,
            "author": art.author or "", "categories": art.categories,
            "summary": (art.summary or "")[:500],
        })
        article_urls.add(item["url"])
        count += 1
        stats["malaymail_rss"] = stats.get("malaymail_rss", 0) + 1
        print(f"  [{count}] {art.title[:70]}")
        if count >= 8:
            break
        time.sleep(1)
except Exception as e:
    print(f"  FAIL: {e}")

# =============================================
# 3. AstroAwani category pages
# =============================================
print("\n=== AstroAwani Berita Politik ===")
try:
    r = session.get("https://www.astroawani.com/berita-politik", timeout=15)
    soup = BeautifulSoup(r.text, "lxml")
    items = []
    for item in soup.find_all(class_="article-teaser-item"):
        a = item.find("a", href=True)
        title_el = item.find(class_="article-text")
        if a and title_el:
            title = title_el.get_text(strip=True)
            if title and len(title) > 15:
                items.append({"title": title, "url": f"https://www.astroawani.com{a['href']}"})
    print(f"  {len(items)} items")
    
    scraper = SCRAPERS["astroawani"]()
    count = 0
    for item in items:
        if item["url"] in article_urls:
            continue
        try:
            art = scraper.get_article(item["url"])
        except:
            continue
        if not art or not art.title:
            continue
        all_articles.append({
            "title": art.title, "url": art.url, "source": art.source,
            "published_at": str(art.published_at) if art.published_at else None,
            "author": art.author or "", "categories": art.categories,
            "summary": (art.summary or "")[:500],
        })
        article_urls.add(item["url"])
        count += 1
        stats["astroawani_politik"] = stats.get("astroawani_politik", 0) + 1
        print(f"  [{count}] {art.title[:70]}")
        if count >= 8:
            break
        time.sleep(1)
except Exception as e:
    print(f"  FAIL: {e}")

# =============================================
# 4. AstroAwani Berita Malaysia
# =============================================
print("\n=== AstroAwani Berita Malaysia ===")
try:
    r = session.get("https://www.astroawani.com/berita-malaysia", timeout=15)
    soup = BeautifulSoup(r.text, "lxml")
    items = []
    for item in soup.find_all(class_="article-teaser-item"):
        a = item.find("a", href=True)
        title_el = item.find(class_="article-text")
        if a and title_el:
            title = title_el.get_text(strip=True)
            if title and len(title) > 15:
                items.append({"title": title, "url": f"https://www.astroawani.com{a['href']}"})
    print(f"  {len(items)} items")
    
    scraper = SCRAPERS["astroawani"]()
    count = 0
    for item in items:
        if item["url"] in article_urls:
            continue
        try:
            art = scraper.get_article(item["url"])
        except:
            continue
        if not art or not art.title:
            continue
        all_articles.append({
            "title": art.title, "url": art.url, "source": art.source,
            "published_at": str(art.published_at) if art.published_at else None,
            "author": art.author or "", "categories": art.categories,
            "summary": (art.summary or "")[:500],
        })
        article_urls.add(item["url"])
        count += 1
        stats["astroawani_malaysia"] = stats.get("astroawani_malaysia", 0) + 1
        print(f"  [{count}] {art.title[:70]}")
        if count >= 8:
            break
        time.sleep(1)
except Exception as e:
    print(f"  FAIL: {e}")

# =============================================
# Save combined results
# =============================================
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
with open(os.path.join(BASE, f"news_combined_{ts}.json"), "w", encoding="utf-8") as f:
    json.dump({"collected_at": str(datetime.now()), "articles": all_articles}, f, indent=2, ensure_ascii=False)

# Merge with existing index
prev_path = os.path.join(BASE, "news_index.json")
if os.path.exists(prev_path):
    with open(prev_path, "r", encoding="utf-8") as f:
        prev = json.load(f)
    existing = {a["url"] for a in prev["articles"]}
    for a in all_articles:
        if a["url"] not in existing:
            prev["articles"].append(a)
    prev["articles"].sort(key=lambda x: x.get("published_at") or "", reverse=True)
    with open(os.path.join(BASE, "news_index.json"), "w", encoding="utf-8") as f:
        json.dump(prev, f, indent=2, ensure_ascii=False)
    total = len(prev["articles"])
else:
    with open(os.path.join(BASE, "news_index.json"), "w", encoding="utf-8") as f:
        json.dump({"collected_at": str(datetime.now()), "articles": all_articles}, f, indent=2, ensure_ascii=False)
    total = len(all_articles)

print(f"\n{'='*50}")
print(f"New articles: {len(all_articles)}")
for k, v in sorted(stats.items()):
    print(f"  {k}: {v}")
print(f"Total in index: {total}")
print(f"Saved: news_combined_{ts}.json")
print(f"Updated: news_index.json")
