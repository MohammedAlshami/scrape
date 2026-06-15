#!/usr/bin/env python
"""Agong / Royal monitor — royal addresses, decrees, king speeches."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["Agong", "Yang di-Pertuan Agong", "king malaysia", "raja malaysia",
            "royal address", "royal decree", "titah", "titah diraja",
            "king speech", "agong speech", "opening parliament",
            "royal assent", "perkenan diraja", "royal consent",
            "sultan", "majlis raja-raja", "conference of rulers",
            "royal palace", "istana negara", "istiadat",
            "agong meeting PM", "agong anwar", "agong advice",
            "royal rebuke", "teguran diraja",
            "agong dissolve parliament", "royal dissolution"]
TOPICS = ["Yang di-Pertuan Agong", "agong malaysia", "titah agong",
          "king malaysia speech", "royal address malaysia",
          "agong parliament", "majlis raja raja", "istana negara",
          "malaysia royal decree", "agong meeting"]
WIKI = ["Yang di-Pertuan Agong", "Conference of Rulers", "Istana Negara, Kuala Lumpur",
        "List of Yang di-Pertuan Agong", "Monarchy of Malaysia",
        "Sultan of Johor", "Sultan of Kedah", "Sultan of Kelantan",
        "Sultan of Pahang", "Sultan of Perak", "Sultan of Selangor",
        "Sultan of Terengganu", "Raja of Perlis", "Yang di-Pertuan Besar of Negeri Sembilan"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("Agong / Royal Monitor", "agong_royal", KEYWORDS, TOPICS, WIKI, fd, td)
