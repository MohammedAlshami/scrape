#!/usr/bin/env python
"""Economic monitor — GDP, inflation, unemployment, BNM, DOSM."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["GDP", "KDNK", "economy", "ekonomi", "inflation", "inflasi",
            "unemployment", "pengangguran", "consumer price", "CPI", "IHK",
            "bank negara", "BNM", "central bank", "interest rate", "OPR",
            "monetary policy", "fiscal policy", "national debt", "hutang",
            "deficit", "current account", "trade balance", "export",
            "ringgit", "MYR", "currency", "mata wang",
            "inflation rate", "core inflation", "headline inflation",
            "economic growth", "pertumbuhan ekonomi",
            "gross domestic product", "keluaran dalam negara kasar",
            "dosm", "department of statistics", "stats malaysia",
            "consumer sentiment", "business confidence",
            "recession", "kemelesetan", "economic recovery"]
TOPICS = ["malaysia GDP", "malaysia inflation", "malaysia economy",
          "bank negara malaysia", "BNM policy", "malaysia OPR",
          "malaysia unemployment", "malaysia trade",
          "malaysia economic growth", "DOSM malaysia",
          "malaysia consumer price", "malaysia fiscal"]
WIKI = ["Economy of Malaysia", "Bank Negara Malaysia", "Malaysian ringgit",
        "Poverty in Malaysia", "Malaysian National Budget",
        "Government of Malaysia", "Khazanah Nasional"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    if "--from" in sys.argv: i=sys.argv.index("--from"); p=sys.argv[i+1].split("-"); fd = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    if "--to" in sys.argv: i=sys.argv.index("--to"); p=sys.argv[i+1].split("-"); td = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    run("Economic Monitor", "economic", KEYWORDS, TOPICS, WIKI, fd, td)
