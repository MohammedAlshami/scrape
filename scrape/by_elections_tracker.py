#!/usr/bin/env python
"""By-election tracker — by-election results, margin swings, voter sentiment."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["by-election", "pilihan raya kecil", "prk", "by election",
            "voter turnout", "undi", "spoiled vote", "majority",
            "by-election result", "by-election malaysia",
            "keputusan pilihan raya", "prk malaysia", "by election result",
            "swing", "marginal seat", "by election campaign"]
TOPICS = ["malaysia by-election", "pilihan raya kecil malaysia",
          "by election result malaysia", "prk malaysia",
          "malaysia by election 2018", "malaysia by election 2019",
          "malaysia by election 2020", "malaysia by election 2021",
          "malaysia by election 2022", "malaysia by election 2023",
          "malaysia by election 2024", "malaysia by election 2025",
          "malaysia by election 2026"]
WIKI = ["By-elections in Malaysia", "List of Malaysian by-elections",
        "Election Commission of Malaysia", "Syarat menjadi calon"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    if "--from" in sys.argv: i=sys.argv.index("--from"); p=sys.argv[i+1].split("-"); fd = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    if "--to" in sys.argv: i=sys.argv.index("--to"); p=sys.argv[i+1].split("-"); td = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    run("By-Election Tracker", "by_elections", KEYWORDS, TOPICS, WIKI, fd, td)
