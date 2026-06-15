import requests
import wikipediaapi
from typing import Optional


class WikipediaTool:
    API = "https://en.wikipedia.org/w/api.php"

    def __init__(self, user_agent: str = "ElectionPredictionBot/1.0"):
        self._ua = user_agent
        self._api = wikipediaapi.Wikipedia(
            language="en",
            user_agent=user_agent,
            extract_format=wikipediaapi.ExtractFormat.WIKI,
        )
        self._session = requests.Session()
        self._session.headers.update({"User-Agent": user_agent})

    def search(self, query: str, results: int = 10) -> list[str]:
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srlimit": results,
            "format": "json",
        }
        r = self._session.get(self.API, params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
        return [s["title"] for s in data.get("query", {}).get("search", [])]

    def summary(self, title: str, sentences: int = 5) -> str:
        page = self._api.page(title)
        if not page.exists():
            return ""
        text = page.summary
        parts = text.split(". ")
        return ". ".join(parts[:sentences]) + ("." if parts else "")

    def page(self, title: str) -> Optional["wikipediaapi.WikipediaPage"]:
        page = self._api.page(title)
        return page if page.exists() else None

    def content(self, title: str) -> Optional[str]:
        page = self.page(title)
        return page.text if page else None

    def sections(self, title: str) -> Optional[list[str]]:
        page = self.page(title)
        if not page:
            return None
        result = []
        self._walk_sections(page.sections, result)
        return result

    def _walk_sections(self, sections: list, acc: list, depth: int = 0):
        for s in sections:
            acc.append(s.title)
            self._walk_sections(s.sections, acc, depth + 1)

    def section(self, title: str, section_title: str) -> Optional[str]:
        page = self._api.page(title)
        if not page.exists():
            return None
        sec = page.section_by_title(section_title)
        return sec.text if sec else None

    def links(self, title: str) -> Optional[list[str]]:
        page = self.page(title)
        if not page:
            return None
        return list(page.links.keys())

    def categories(self, title: str) -> Optional[list[str]]:
        page = self.page(title)
        if not page:
            return None
        return [c.split(":")[-1] for c in page.categories.keys()]

    def search_and_pick(self, query: str) -> Optional[str]:
        page = self._api.page(query)
        if page.exists():
            return query
        results = self.search(query, results=5)
        return results[0] if results else None
