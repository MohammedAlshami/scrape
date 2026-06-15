#!/usr/bin/env python
"""PKR discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["pkr", "keadilan", "parti keadilan rakyat", "people justice party", "anwar", "wan azizah", "rafizi"]
TOPICS = ["pkr", "keadilan", "parti keadilan rakyat", "pkr malaysia", "pkr party", "pkr politics", "pkr policy", "pkr election", "pkr reformasi"]
WIKI_PAGES = ["People's Justice Party (Malaysia)", "Parti Keadilan Rakyat", "PKR Youth", "PKR Women", "List of PKR leaders"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    if "--from" in sys.argv: i=sys.argv.index("--from"); p=sys.argv[i+1].split("-"); fd = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    if "--to" in sys.argv: i=sys.argv.index("--to"); p=sys.argv[i+1].split("-"); td = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    run("PKR Discovery", "pkr", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
