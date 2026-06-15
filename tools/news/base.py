from abc import ABC, abstractmethod
from typing import Optional
from bs4 import BeautifulSoup, Tag
from .models import Article, ArticleSummary, ContentBlock, BlockType


class BaseNewsScraper(ABC):
    @abstractmethod
    def search(self, query: str, max_results: int = 10) -> list[ArticleSummary]:
        ...

    @abstractmethod
    def get_article(self, url: str) -> Optional[Article]:
        ...

    @abstractmethod
    def get_categories(self) -> list[str]:
        ...

    def _parse_content_blocks(self, element: Tag) -> list[ContentBlock]:
        blocks = []
        for el in element.children:
            if not isinstance(el, Tag):
                continue
            tag = el.name.lower()

            if tag in ("h1", "h2", "h3"):
                blocks.append(ContentBlock(type=BlockType(tag), text=el.get_text(strip=True)))

            elif tag == "p":
                blocks.append(self._parse_paragraph(el))

            elif tag == "ul":
                items = []
                for li in el.find_all("li", recursive=False):
                    items.append(li.get_text(strip=True))
                blocks.append(ContentBlock(type=BlockType.UNORDERED_LIST, children=items))

            elif tag == "ol":
                items = []
                for li in el.find_all("li", recursive=False):
                    items.append(li.get_text(strip=True))
                blocks.append(ContentBlock(type=BlockType.ORDERED_LIST, children=items))

            elif tag == "blockquote":
                blocks.append(ContentBlock(type=BlockType.BLOCKQUOTE, text=el.get_text(strip=True)))

            elif tag == "img":
                src = el.get("src", "") or el.get("data-src", "")
                alt = el.get("alt", "")
                if src and "logo" not in src.lower():
                    blocks.append(ContentBlock(type=BlockType.IMAGE, src=src, alt=alt))

            elif tag == "div":
                blocks.extend(self._parse_content_blocks(el))

        return blocks

    def _parse_paragraph(self, el: Tag) -> ContentBlock:
        text = ""
        children = []
        for child in el.children:
            if isinstance(child, Tag):
                if child.name in ("strong", "b"):
                    children.append(ContentBlock(type=BlockType.BOLD, text=child.get_text(strip=True)))
                elif child.name in ("i", "em"):
                    children.append(ContentBlock(type=BlockType.ITALIC, text=child.get_text(strip=True)))
                elif child.name == "a":
                    children.append(ContentBlock(type=BlockType.BOLD, text=child.get_text(strip=True)))
                else:
                    text += child.get_text()
            else:
                text += str(child)
        t = (text or "").strip()
        if t or children:
            if children:
                return ContentBlock(type=BlockType.PARAGRAPH, text=t, children=children)
            return ContentBlock(type=BlockType.PARAGRAPH, text=t)
        return ContentBlock(type=BlockType.PARAGRAPH, text=t)
