#!/usr/bin/env python
"""Ratings & outlook — Moody's, S&P, Fitch sovereign ratings, outlook changes."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["Moody", "Moody's", "Standard Poor", "S&P", "Fitch",
            "sovereign rating", "credit rating", "rating outlook",
            "rating upgrade", "rating downgrade", "rating affirm",
            "negative outlook", "positive outlook", "stable outlook",
            "investment grade", "junk status", "rating action",
            "A3", "BBB+", "BBB-", "Baa3",
            "malaysia rating", "malaysia credit rating",
            "rating agency", "RAM rating", "MARC rating"]
TOPICS = ["malaysia credit rating", "Moody malaysia", "S&P malaysia",
          "Fitch malaysia", "malaysia sovereign rating", "malaysia rating outlook",
          "RAM malaysia", "MARC malaysia"]
WIKI = ["Economy of Malaysia", "Malaysian ringgit", "Sovereign credit rating"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("Ratings & Outlook", "ratings", KEYWORDS, TOPICS, WIKI, fd, td)
