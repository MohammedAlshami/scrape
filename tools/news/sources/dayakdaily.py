import re
from datetime import datetime
from typing import Optional
import requests
from bs4 import BeautifulSoup, Tag
from ..base import BaseNewsScraper
from ..models import Article, ArticleSummary, ContentBlock, BlockType


class DayakDailyScraper(BaseNewsScraper):
    BASE = "https://dayakdaily.com"

    def __init__(self, user_agent: str = "ElectionPredictionBot/1.0"):
        self._session = requests.Session()
        self._session.headers.update({"User-Agent": user_agent})

    def _parse_content_blocks(self, element: Tag) -> list[ContentBlock]:
        """Extract content blocks from element in document order."""
        blocks = []
        for el in element.find_all(["p", "h1", "h2", "h3", "h4", "ul", "ol", "blockquote", "figure", "img"], recursive=True):
            tag = el.name.lower()
            # Skip elements inside figures (we handle figure itself)
            if tag == "img" and el.parent and el.parent.name == "figure":
                continue

            if tag in ("h1", "h2", "h3", "h4"):
                blocks.append(ContentBlock(type=BlockType(tag), text=el.get_text(strip=True)))
            elif tag == "p":
                text = el.get_text(strip=True)
                if text:
                    blocks.append(ContentBlock(type=BlockType.PARAGRAPH, text=text))
            elif tag in ("ul", "ol"):
                items = [li.get_text(strip=True) for li in el.find_all("li", recursive=False) if li.get_text(strip=True)]
                if items:
                    blocks.append(ContentBlock(
                        type=BlockType.UNORDERED_LIST if tag == "ul" else BlockType.ORDERED_LIST,
                        children=items,
                    ))
            elif tag == "blockquote":
                text = el.get_text(strip=True)
                if text:
                    blocks.append(ContentBlock(type=BlockType.BLOCKQUOTE, text=text))
            elif tag == "figure":
                img = el.find("img")
                if img:
                    src = img.get("src", "") or img.get("data-src", "")
                    alt = img.get("alt", "")
                    if src and "logo" not in src.lower():
                        blocks.append(ContentBlock(type=BlockType.IMAGE, src=src, alt=alt))
        return blocks

    def search(self, query: str, max_results: int = 10) -> list[ArticleSummary]:
        url = f"{self.BASE}/"
        r = self._session.get(url, params={"s": query}, timeout=15)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")
        results = []

        for a in soup.find_all("a", href=True):
            href = a["href"]
            title = a.get_text(strip=True)
            if not href.startswith(self.BASE) or len(title) < 20:
                continue
            results.append(ArticleSummary(title=title, url=href))
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

        h1 = soup.find("h1")
        if h1:
            title = h1.get_text(strip=True)

        for meta in soup.find_all("meta"):
            prop = meta.get("property", "") or meta.get("name", "")
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

        author_el = soup.find(class_="author")
        if author_el:
            author = author_el.get_text(strip=True).replace("By ", "")

        article_tag = soup.find("article")
        content = self._parse_content_blocks(article_tag) if article_tag else []

        if not title:
            return None

        return Article(
            title=title,
            url=url,
            source="dayakdaily",
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
            if href.startswith(self.BASE) and "/" in href:
                parts = href.replace(self.BASE, "").split("/")
                if len(parts) > 1 and parts[1] and len(parts[1]) < 30:
                    cats.add(parts[1])
        return sorted(cats)
