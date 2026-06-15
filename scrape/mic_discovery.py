#!/usr/bin/env python
"""MIC discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["mic", "malaysian indian congress", "kongres india malaysia", "samy vellu", "vigneswaran", "sivaraj"]
TOPICS = ["mic", "mic malaysia", "malaysian indian congress", "mic party", "mic politics", "mic bn"]
WIKI_PAGES = ["Malaysian Indian Congress", "Kongres India Malaysia", "Samy Vellu", "Barisan Nasional", "List of MIC leaders"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("MIC Discovery", "mic", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
