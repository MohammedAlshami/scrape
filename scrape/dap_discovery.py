#!/usr/bin/env python
"""DAP discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["dap", "democratic action party", "parti tindakan demokratik", "lim kit siang", "lim guan eng", "tony pua", "bukit gelugor", "buntong"]
TOPICS = ["dap", "dap malaysia", "dap party", "dap politics", "dap policy", "dap election", "dap government", "dap socialist"]
WIKI_PAGES = ["Democratic Action Party", "Parti Tindakan Demokratik", "Lim Kit Siang", "Lim Guan Eng", "Tony Pua", "DAP Socialist Youth"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc)
    td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    if "--from" in sys.argv: i=sys.argv.index("--from"); p=sys.argv[i+1].split("-"); fd = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    if "--to" in sys.argv: i=sys.argv.index("--to"); p=sys.argv[i+1].split("-"); td = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    run("DAP Discovery", "dap", KEYWORDS, TOPICS, WIKI_PAGES, fd, td)
