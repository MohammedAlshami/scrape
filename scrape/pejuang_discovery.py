#!/usr/bin/env python
"""PEJUANG discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["pejuang", "parti pejuang tanah air", "homeland fighter party", "mahathir pejuang", "mukhriz"]
TOPICS = ["pejuang", "parti pejuang tanah air", "pejuang party", "pejuang malaysia", "mahathir pejuang"]
WIKI_PAGES = ["Homeland Fighter's Party", "Parti Pejuang Tanah Air", "Mahathir Mohamad", "Mukhriz Mahathir"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("PEJUANG Discovery", "pejuang", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
