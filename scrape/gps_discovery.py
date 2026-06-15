#!/usr/bin/env python
"""GPS discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["gps", "gabungan parti sarawak", "sarawak parties", "pbb", "prs", "pdp", "supp", "abang johari", "sarawak politics"]
TOPICS = ["gps", "gabungan parti sarawak", "sarawak parties", "pbb sarawak", "prs sarawak", "pdp sarawak", "supp sarawak", "sarawak politics"]
WIKI_PAGES = ["Gabungan Parti Sarawak", "Parti Pesaka Bumiputera Bersatu", "Parti Rakyat Sarawak", "Progressive Democratic Party", "Sarawak United Peoples' Party", "Abang Abdul Rahman Johari"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("GPS Discovery", "gps", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
