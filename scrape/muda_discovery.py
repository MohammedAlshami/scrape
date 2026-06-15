#!/usr/bin/env python
"""MUDA discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["muda", "parti muda", "malaysian democratic alliance", "syed saddiq", "young malaysia"]
TOPICS = ["muda", "parti muda", "muda malaysia", "muda party", "muda politics", "syed saddiq"]
WIKI_PAGES = ["Malaysian United Democratic Alliance", "Parti Muda", "Syed Saddiq"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("MUDA Discovery", "muda", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
