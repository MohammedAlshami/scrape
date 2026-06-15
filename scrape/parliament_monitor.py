#!/usr/bin/env python
"""Parliament monitor — sittings, bills, confidence motions, Hansard."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["parliament", "dewan rakyat", "dewan negara", "speaker", "sitting", "session",
            "bill", "rang undang-undang", "vote", "undi", "confidence", "no-confidence",
            "motion", "usul", "question time", "minister question",
            "hansard", "proceeding", "committee", "select committee",
            "speech", "address", "royal address", "king speech", "agong speech",
            "adjourn", "prorogue", "dissolve", "parliament dissolve",
            "MP", "member of parliament", "ahli parlimen",
            "budget reading", "budget speech", "supply bill"]
TOPICS = ["malaysia parliament", "dewan rakyat", "parliament sitting", "malaysia bill",
          "malaysia law passed", "parliament session", "hansard malaysia",
          "parliament committee", "malaysia motion", "parliament vote",
          "malaysia king speech", "agong parliament", "parliament dissolve"]
WIKI = ["Parliament of Malaysia", "Dewan Rakyat", "Dewan Negara", "Speaker of the Dewan Rakyat",
        "List of Malaysian federal legislation", "Yang di-Pertuan Agong"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    if "--from" in sys.argv: i=sys.argv.index("--from"); p=sys.argv[i+1].split("-"); fd = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    if "--to" in sys.argv: i=sys.argv.index("--to"); p=sys.argv[i+1].split("-"); td = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    run("Parliament Monitor", "parliament", KEYWORDS, TOPICS, WIKI, fd, td)
