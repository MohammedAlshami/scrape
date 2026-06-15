from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class BlockType(str, Enum):
    HEADING1 = "h1"
    HEADING2 = "h2"
    HEADING3 = "h3"
    PARAGRAPH = "p"
    BOLD = "bold"
    ITALIC = "italic"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"
    LIST_ITEM = "li"
    IMAGE = "img"
    BLOCKQUOTE = "blockquote"
    DIV = "div"


@dataclass
class ContentBlock:
    type: BlockType
    text: str = ""
    children: list = field(default_factory=list)
    src: str = ""
    alt: str = ""


@dataclass
class ArticleSummary:
    title: str
    url: str
    published_at: Optional[datetime] = None
    summary: Optional[str] = None
    image_url: Optional[str] = None


@dataclass
class Article:
    title: str
    url: str
    source: str
    published_at: Optional[datetime] = None
    author: Optional[str] = None
    categories: list = field(default_factory=list)
    image_url: Optional[str] = None
    summary: Optional[str] = None
    content: list = field(default_factory=list)
