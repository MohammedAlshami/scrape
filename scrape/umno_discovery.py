#!/usr/bin/env python
"""UMNO discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["umno", "united malays national organisation", "pertubuhan kebangsaan melayu bersatu", "bn", "barisan nasional", "umno baharu", "umno baru"]
TOPICS = ["umno", "umno malaysia", "umno party", "umno politics", "umno policy", "umno government", "umno election", "umno president", "umno supreme council", "umno youth", "umno wanita", "umno division", "umno general assembly", "umno sejarah"]
WIKI_PAGES = ["United Malays National Organisation", "Barisan Nasional", "UMNO Youth", "UMNO General Assembly", "Ketua UMNO", "List of UMNO leaders"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    if "--from" in sys.argv: i=sys.argv.index("--from"); p=sys.argv[i+1].split("-"); fd = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    if "--to" in sys.argv: i=sys.argv.index("--to"); p=sys.argv[i+1].split("-"); td = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    run("UMNO Discovery", "umno", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
