#!/usr/bin/env python
"""MCA discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["mca", "malaysian chinese association", "persatuan cina malaysia", "liow tiong lai", "wee ka siong", "chinese malaysia"]
TOPICS = ["mca", "mca malaysia", "malaysian chinese association", "mca party", "mca politics", "mca bn"]
WIKI_PAGES = ["Malaysian Chinese Association", "Persatuan Cina Malaysia", "Liow Tiong Lai", "Wee Ka Siong", "Barisan Nasional"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("MCA Discovery", "mca", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
