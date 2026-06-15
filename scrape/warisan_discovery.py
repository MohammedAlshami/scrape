#!/usr/bin/env python
"""WARISAN discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["warisan", "parti warisan sabah", "heritage party", "shafie apdal", "warisan sabah"]
TOPICS = ["warisan", "warisan sabah", "parti warisan sabah", "warisan party", "warisan politics", "shafie apdal"]
WIKI_PAGES = ["Heritage Party (Malaysia)", "Parti Warisan Sabah", "Shafie Apdal", "Warisan", "Sabah politics"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("WARISAN Discovery", "warisan", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
