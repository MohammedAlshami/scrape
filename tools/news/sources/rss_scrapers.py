"""Generic RSS-based news scraper for multiple Malaysian sources."""

import re
from datetime import datetime
from typing import Optional
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup
from ..base import BaseNewsScraper
from ..models import Article, ArticleSummary, ContentBlock, BlockType


class RSSNewsScraper(BaseNewsScraper):
    """Scraper that discovers articles via RSS feed and parses pages with configurable selectors."""

    def __init__(self, feed_url: str, base_url: str, source_key: str,
                 title_sel: str = "h1", date_sel: str = 'meta[property="article:published_time"]',
                 author_sel: str = "", body_sel: str = "article",
                 summary_sel: str = 'meta[property="og:description"]',
                 category_sel: str = 'meta[property="article:section"]',
                 user_agent: str = "ElectionPredictionBot/1.0"):
        self.feed_url = feed_url
        self.BASE = base_url
        self.source = source_key
        self.title_sel = title_sel
        self.date_sel = date_sel
        self.author_sel = author_sel
        self.body_sel = body_sel
        self.summary_sel = summary_sel
        self.category_sel = category_sel
        self._session = requests.Session()
        self._session.headers.update({"User-Agent": user_agent})

    def search(self, query: str = "", max_results: int = 10) -> list[ArticleSummary]:
        """Read RSS feed and optionally filter by query."""
        try:
            r = self._session.get(self.feed_url, timeout=15)
            r.raise_for_status()
            root = ET.fromstring(r.content)
        except Exception:
            return []

        results = []
        for item in root.findall(".//item"):
            title = item.findtext("title", "")
            link = item.findtext("link", "")
            if not title or not link:
                continue
            if query and query.lower() not in title.lower():
                continue
            results.append(ArticleSummary(title=title, url=link))
            if len(results) >= max_results:
                break

        # Fallback: if no query match, return first N items
        if query and not results:
            for item in list(root.findall(".//item"))[:max_results]:
                title = item.findtext("title", "")
                link = item.findtext("link", "")
                if title and link:
                    results.append(ArticleSummary(title=title, url=link))

        return results

    def get_article(self, url: str) -> Optional[Article]:
        try:
            r = self._session.get(url, timeout=15)
            r.raise_for_status()
        except Exception:
            return None

        soup = BeautifulSoup(r.text, "lxml")

        title_el = soup.select_one(self.title_sel)
        title = title_el.get_text(strip=True) if title_el else ""

        published_at = None
        try:
            meta = soup.select_one(self.date_sel)
            if meta:
                val = meta.get("content", "")
                published_at = datetime.fromisoformat(val.replace("Z", "+00:00"))
        except Exception:
            pass

        author = ""
        if self.author_sel:
            el = soup.select_one(self.author_sel)
            if el:
                author = el.get_text(strip=True)

        categories = []
        if self.category_sel:
            meta = soup.select_one(self.category_sel)
            if meta:
                cat = meta.get("content", "")
                if cat:
                    categories.append(cat)

        summary = ""
        if self.summary_sel:
            meta = soup.select_one(self.summary_sel)
            if meta:
                summary = meta.get("content", "")

        image_url = ""
        for meta in soup.find_all("meta"):
            if meta.get("property") == "og:image":
                image_url = meta.get("content", "")
                break

        body = soup.select_one(self.body_sel)
        content = self._parse_content_blocks(body) if body else []
        if not content and body:
            content = [ContentBlock(type=BlockType.PARAGRAPH, text=body.get_text(strip=True)[:5000])]

        if not title:
            return None

        return Article(
            title=title, url=url, source=self.source,
            published_at=published_at, author=author,
            categories=categories, image_url=image_url,
            summary=summary, content=content,
        )

    def get_categories(self) -> list[str]:
        return []


# Pre-configured instances for easy import
NST = RSSNewsScraper(
    feed_url="https://www.nst.com.my/feed",
    base_url="https://www.nst.com.my",
    source_key="nst",
    body_sel="article, .node__content, main",
    title_sel="h1",
)

FMT = RSSNewsScraper(
    feed_url="https://www.freemalaysiatoday.com/feed/",
    base_url="https://www.freemalaysiatoday.com",
    source_key="fmt",
    body_sel="article, main, .post-content",
    title_sel="h1",
)

VIBES = RSSNewsScraper(
    feed_url="https://www.thevibes.com/rss",
    base_url="https://www.thevibes.com",
    source_key="thevibes",
    body_sel="html",
    title_sel="h1",
)

BORNEO_POST = RSSNewsScraper(
    feed_url="https://www.theborneopost.com/feed/",
    base_url="https://www.theborneopost.com",
    source_key="borneopost",
    body_sel="article, .post-content, .entry-content",
    title_sel="h1.entry-title",
)

SINAR_HARIAN = RSSNewsScraper(
    feed_url="http://www.sinarharian.com.my/rssFeed/211",
    base_url="https://www.sinarharian.com.my",
    source_key="sinarharian",
    body_sel=".content-article, article, .field--name-body",
    title_sel="h1",
)

HARIAN_METRO = RSSNewsScraper(
    feed_url="http://www.hmetro.com.my/utama.xml",
    base_url="https://www.hmetro.com.my",
    source_key="hmetro",
    body_sel="article, main, .page-collection-utama",
    title_sel="h1",
)
