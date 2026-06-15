#!/usr/bin/env python
"""Think tanks & surveys — Merdeka Center, Ipsos, O2, public opinion polls."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["survey", "poll", "tinjauan", "opinion poll", "kajian pendapat",
            "approval rating", "popularity", "satisfaction", "keyakinan",
            "merdeka center", "merdeka survey", "merdeka poll",
            "ipsos malaysia", "ipsos survey",
            "O2 malaysia", "O2 research",
            "voter sentiment", "pengundi", "voter intention",
            "voter preference", "undian", "pilihan pengundi",
            "trust index", "trust malaysia",
            "public opinion", "pendapat umum",
            "political trust", "kepercayaan politik",
            "government satisfaction", "kepuasan kerajaan",
            "PM approval", "anwar approval", "PM rating",
            "party preference", "party support",
            "BN support", "PH support", "PN support",
            "GE16 prediction", "GE16 projection",
            "marginal seat", "kerusi marginal",
            "swing", "peralihan undi"]
TOPICS = ["merdeka center malaysia", "ipsos malaysia", "O2 malaysia",
          "malaysia opinion poll", "malaysia survey", "voter survey malaysia",
          "malaysia approval rating", "malaysia political survey",
          "malaysia public opinion", "anwar approval poll",
          "voter intention malaysia", "GE16 malaysia poll"]
WIKI = ["Opinion polling in Malaysia", "Merdeka Center", "Ipsos",
        "Public opinion", "Elections in Malaysia"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("Think Tanks & Surveys", "surveys", KEYWORDS, TOPICS, WIKI, fd, td)
