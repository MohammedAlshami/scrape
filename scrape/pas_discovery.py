#!/usr/bin/env python
"""PAS discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["pas", "pan malaysian islamic party", "parti islam se malaysia", "pengasuh", "hadi awang", "ulama", "islamic party"]
TOPICS = ["pas", "pas malaysia", "pas party", "pas politics", "pas policy", "pas election", "pas government", "pas president", "pas ulama"]
WIKI_PAGES = ["Pan-Malaysian Islamic Party", "Parti Islam Se-Malaysia", "Abdul Hadi Awang", "PAS Youth", "PAS Dewan Ulama", "Gagasan Sejahtera"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    if "--from" in sys.argv: i=sys.argv.index("--from"); p=sys.argv[i+1].split("-"); fd = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    if "--to" in sys.argv: i=sys.argv.index("--to"); p=sys.argv[i+1].split("-"); td = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    run("PAS Discovery", "pas", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
