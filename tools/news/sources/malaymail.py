import re
from datetime import datetime
from typing import Optional
import requests
from bs4 import BeautifulSoup
from ..base import BaseNewsScraper
from ..models import Article, ArticleSummary


class MalayMailScraper(BaseNewsScraper):
    BASE = "https://www.malaymail.com"

    def __init__(self, user_agent: str = "ElectionPredictionBot/1.0"):
        self._session = requests.Session()
        self._session.headers.update({"User-Agent": user_agent})

    def search(self, query: str, max_results: int = 10) -> list[ArticleSummary]:
        url = f"{self.BASE}/search"
        r = self._session.get(url, params={"q": query}, timeout=15)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")
        results = []
        seen = set()
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if not href.startswith(self.BASE):
                continue
            if "/news/" not in href or "/20" not in href:
                continue
            if href in seen:
                continue
            seen.add(href)
            title = a.get_text(strip=True)
            if not title or len(title) < 10:
                continue
            results.append(ArticleSummary(title=title, url=href))
            if len(results) >= max_results:
                break

        # Fetch og:image for each result in parallel
        if results:
            import concurrent.futures
            def fetch_image(art):
                try:
                    r2 = self._session.get(art.url, timeout=8)
                    if r2.status_code == 200:
                        s2 = BeautifulSoup(r2.text, "html.parser")
                        for meta in s2.find_all("meta"):
                            if meta.get("property") == "og:image":
                                art.image_url = meta.get("content", "")
                                break
                except:
                    pass
                return art
            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
                results = list(pool.map(fetch_image, results))

        return results

    def get_article(self, url: str) -> Optional[Article]:
        if not url.startswith("http"):
            url = self.BASE + url
        r = self._session.get(url, timeout=15)
        if r.status_code != 200:
            return None
        soup = BeautifulSoup(r.text, "lxml")

        title = ""
        published_at = None
        author = ""
        categories = []
        image_url = ""
        summary = ""

        # Title
        h1 = soup.find("h1", class_="article-title")
        if h1:
            title = h1.get_text(strip=True)

        # Date
        for t in soup.find_all("time"):
            dt = t.get("datetime", "")
            if dt:
                try:
                    published_at = datetime.fromisoformat(dt.replace("Z", "+00:00"))
                except:
                    pass
                break
        if not published_at:
            for meta in soup.find_all("meta"):
                if meta.get("property") == "article:published_time":
                    val = meta.get("content", "")
                    try:
                        published_at = datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
                    except:
                        try:
                            published_at = datetime.fromisoformat(val)
                        except:
                            pass

        # Author
        byline = soup.find("div", class_="article-byline")
        if byline:
            author = byline.get_text(strip=True).replace("By ", "")

        # Category
        for meta in soup.find_all("meta"):
            if meta.get("property") == "article:section":
                cat = meta.get("content", "")
                if cat:
                    categories.append(cat)

        # Image
        for meta in soup.find_all("meta"):
            if meta.get("property") == "og:image":
                image_url = meta.get("content", "")
                break

        # Summary (og:description)
        for meta in soup.find_all("meta"):
            if meta.get("property") == "og:description":
                summary = meta.get("content", "")

        # Article body
        body = soup.find(class_="article-body")
        content = self._parse_content_blocks(body) if body else []

        if not title:
            return None

        return Article(
            title=title,
            url=url,
            source="malaymail",
            published_at=published_at,
            author=author,
            categories=categories,
            image_url=image_url,
            summary=summary,
            content=content,
        )

    def get_categories(self) -> list[str]:
        r = self._session.get(self.BASE, timeout=15)
        soup = BeautifulSoup(r.text, "lxml")
        cats = set()
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if "/news/" in href:
                parts = href.split("/")
                if len(parts) > 4:
                    section = parts[4]
                    if section and section not in ("search",):
                        cats.add(section)
        return sorted(cats)
