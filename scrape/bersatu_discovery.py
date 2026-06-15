#!/usr/bin/env python
"""BERSATU discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["bersatu", "ppbm", "parti pribumi bersatu malaysia", "malaysian united indigenous party", "muhyiddin", "mahathir bersatu"]
TOPICS = ["bersatu", "bersatu malaysia", "ppbm", "parti pribumi bersatu", "bersatu party", "bersatu politics", "bersatu election"]
WIKI_PAGES = ["Malaysian United Indigenous Party", "Parti Pribumi Bersatu Malaysia", "BERSATU", "Perikatan Nasional", "Muhyiddin Yassin"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    if "--from" in sys.argv: i=sys.argv.index("--from"); p=sys.argv[i+1].split("-"); fd = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    if "--to" in sys.argv: i=sys.argv.index("--to"); p=sys.argv[i+1].split("-"); td = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    run("BERSATU Discovery", "bersatu", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
