import re
from datetime import datetime
from typing import Optional
import requests
from bs4 import BeautifulSoup
from ..base import BaseNewsScraper
from ..models import Article, ArticleSummary


class AstroAwaniScraper(BaseNewsScraper):
    BASE = "https://www.astroawani.com"

    def __init__(self, user_agent: str = "ElectionPredictionBot/1.0"):
        self._session = requests.Session()
        self._session.headers.update({"User-Agent": user_agent})

    def search(self, query: str, max_results: int = 10) -> list[ArticleSummary]:
        url = f"{self.BASE}/search"
        r = self._session.get(url, params={"q": query}, timeout=15)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")
        results = []

        for item in soup.find_all(class_="article-teaser-item"):
            a = item.find("a", href=True)
            if not a:
                continue
            href = a["href"]
            if not href.startswith("/"):
                continue
            title_el = item.find(class_="article-text")
            title = title_el.get_text(strip=True) if title_el else a.get_text(strip=True)
            if not title or len(title) < 15:
                continue
            full_url = f"{self.BASE}{href}"
            results.append(ArticleSummary(title=title, url=full_url))
            if len(results) >= max_results:
                break

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

        h1 = soup.find("h1")
        if h1:
            title = h1.get_text(strip=True)

        for meta in soup.find_all("meta"):
            prop = meta.get("property", "")
            if prop == "article:published_time":
                val = meta.get("content", "")
                try:
                    published_at = datetime.fromisoformat(val.replace("Z", "+00:00"))
                except:
                    pass
            elif prop == "article:section":
                cat = meta.get("content", "")
                if cat:
                    categories.append(cat)
            elif prop == "og:image":
                image_url = meta.get("content", "")
            elif prop == "og:description":
                summary = meta.get("content", "")

        author_el = soup.find(class_="post-author")
        if author_el:
            author = author_el.get_text(strip=True)
            author = re.sub(r"\d{2}/\d{2}/\d{4}.*", "", author).strip()

        body = soup.find(class_="field--name-body")
        content = self._parse_content_blocks(body) if body else []

        if not title:
            return None

        return Article(
            title=title,
            url=url,
            source="astroawani",
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
            if href.startswith("/berita-"):
                parts = href.split("/")
                if len(parts) > 1:
                    section = parts[1].replace("berita-", "")
                    if section:
                        cats.add(section)
        return sorted(cats)
