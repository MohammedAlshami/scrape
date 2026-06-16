"""Scrape news category pages directly instead of using search."""

import json, sys, os, time
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import requests
from bs4 import BeautifulSoup
from tools.news.models import Article, ArticleSummary
from tools.news.sources import SCRAPERS

BASE = os.path.join(ROOT, "data", "news")
os.makedirs(BASE, exist_ok=True)

session = requests.Session()
session.headers.update({"User-Agent": "ElectionPredictionBot/1.0"})

SOURCES_CONFIG = [
    {
        "name": "malaymail_politics",
        "url": "https://www.malaymail.com/news/politics",
        "source": "malaymail",
        "scraper": None,
    },
    {
        "name": "malaymail_malaysia",
        "url": "https://www.malaymail.com/news/malaysia",
        "source": "malaymail",
        "scraper": None,
    },
    {
        "name": "astroawani_politik",
        "url": "https://www.astroawani.com/berita-politik",
        "source": "astroawani",
        "scraper": None,
    },
    {
        "name": "astroawani_ekonomi",
        "url": "https://www.astroawani.com/berita-ekonomi",
        "source": "astroawani",
        "scraper": None,
    },
    {
        "name": "astroawani_malaysia",
        "url": "https://www.astroawani.com/berita-malaysia",
        "source": "astroawani",
        "scraper": None,
    },
    {
        "name": "dayakdaily",
        "url": "https://dayakdaily.com",
        "source": "dayakdaily",
        "scraper": None,
    },
]

for cfg in SOURCES_CONFIG:
    try:
        cfg["scraper"] = SCRAPERS[cfg["source"]]()
    except:
        pass

def extract_malaymail_articles(html):
    soup = BeautifulSoup(html, "lxml")
    articles = []
    seen = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "malaymail.com/news/" not in href or "/20" not in href:
            continue
        if href in seen:
            continue
        seen.add(href)
        title = a.get_text(strip=True)
        if title and len(title) > 15:
            articles.append(ArticleSummary(title=title, url=href))
    return articles

def extract_astroawani_articles(html):
    soup = BeautifulSoup(html, "lxml")
    articles = []
    for item in soup.find_all(class_="article-teaser-item"):
        a = item.find("a", href=True)
        if not a:
            continue
        href = a["href"]
        if not href.startswith("/"):
            continue
        title_el = item.find(class_="article-text")
        title = title_el.get_text(strip=True) if title_el else ""
        if not title or len(title) < 15:
            continue
        articles.append(ArticleSummary(title=title, url=f"https://www.astroawani.com{href}"))
    return articles

def extract_dayakdaily_articles(html):
    soup = BeautifulSoup(html, "lxml")
    articles = []
    seen = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "dayakdaily.com" not in href:
            continue
        if href in seen:
            continue
        seen.add(href)
        title = a.get_text(strip=True)
        if title and len(title) > 20:
            articles.append(ArticleSummary(title=title, url=href))
    return articles

extractors = {
    "malaymail": extract_malaymail_articles,
    "astroawani": extract_astroawani_articles,
    "dayakdaily": extract_dayakdaily_articles,
}

all_articles = []
article_urls = set()
stats = {}

for cfg in SOURCES_CONFIG:
    name = cfg["name"]
    print(f"\n--- {name} ---")
    
    try:
        r = session.get(cfg["url"], timeout=15)
        r.raise_for_status()
    except Exception as e:
        print(f"  FAIL: {e}")
        continue
    
    extractor = extractors.get(cfg["source"])
    if not extractor:
        print(f"  No extractor for {cfg['source']}")
        continue
    
    summaries = extractor(r.text)
    print(f"  Found {len(summaries)} article links")
    
    scraper = cfg["scraper"]
    count = 0
    
    for s in summaries:
        if s.url in article_urls:
            continue
        
        try:
            art = scraper.get_article(s.url) if scraper else None
        except:
            art = None
        
        if not art or not art.title:
            article_urls.add(s.url)
            continue
        
        article = {
            "title": art.title,
            "url": art.url,
            "source": art.source,
            "published_at": str(art.published_at) if art.published_at else None,
            "author": art.author or "",
            "categories": art.categories,
            "summary": (art.summary or "")[:500],
            "section": name,
        }
        
        all_articles.append(article)
        article_urls.add(s.url)
        count += 1
        stats[name] = stats.get(name, 0) + 1
        print(f"  [{count}] {art.title[:70]}")
        
        if count >= 6:
            break
        
        time.sleep(1)
    
    # Save progress
    with open(os.path.join(BASE, "news_in_progress.json"), "w", encoding="utf-8") as f:
        json.dump({"articles": all_articles}, f, indent=2, ensure_ascii=False)

# Final save
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
with open(os.path.join(BASE, f"news_categories_{ts}.json"), "w", encoding="utf-8") as f:
    json.dump({"collected_at": str(datetime.now()), "articles": all_articles}, f, indent=2, ensure_ascii=False)
with open(os.path.join(BASE, "news_categories.json"), "w", encoding="utf-8") as f:
    json.dump({"collected_at": str(datetime.now()), "articles": all_articles}, f, indent=2, ensure_ascii=False)

print(f"\n{'='*50}")
print(f"Done! {len(all_articles)} articles from {len(SOURCES_CONFIG)} sections")
for k, v in sorted(stats.items()):
    print(f"  {k}: {v}")
