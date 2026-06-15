#!/usr/bin/env python
"""AMANAH discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["amanah", "parti amanah negara", "national trust party", "mohamad sabu", "mat sabu", "amanah malaysia"]
TOPICS = ["amanah", "amanah malaysia", "parti amanah negara", "amanah party", "amanah politics", "amanah election"]
WIKI_PAGES = ["National Trust Party (Malaysia)", "Parti Amanah Negara", "Mohamad Sabu", "Pakatan Harapan"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("AMANAH Discovery", "amanah", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
