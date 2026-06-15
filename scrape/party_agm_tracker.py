#!/usr/bin/env python
"""Party AGM / internal election tracker — AGM dates, leadership changes."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["AGM", "general assembly", "perhimpunan agung", "PAU",
            "party election", "pemilihan parti", "party congress",
            "delegates", "perwakilan", "party president",
            "timbalan presiden", "naib presiden", "vice president",
            "party supreme council", "majlis tertinggi",
            "party youth", "pemuda parti", "party women", "wanita parti",
            "UMNO assembly", "PKR congress", "PAS mukhtamar",
            "DAP congress", "BERSATU assembly",
            "party manifesto", "party campaign", "party strategy",
            "party coalition meeting", "component party"]
TOPICS = ["UMNO general assembly", "PKR congress", "PAS mukhtamar",
          "DAP congress", "BERSATU assembly", "AMANAH congress",
          "malaysia party election", "perhimpunan agung umno",
          "party election malaysia", "malaysia political party"]
WIKI = ["United Malays National Organisation", "People's Justice Party (Malaysia)",
        "Pan-Malaysian Islamic Party", "Democratic Action Party",
        "Malaysian United Indigenous Party", "National Trust Party (Malaysia)"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("Party AGM Tracker", "party_agms", KEYWORDS, TOPICS, WIKI, fd, td)
