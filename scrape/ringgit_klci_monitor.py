#!/usr/bin/env python
"""Ringgit / KLCI market monitor — currency, stock market, capital flows."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["ringgit", "MYR", "ringgit malaysia", "USDMYR", "ringgit USD",
            "KLCI", "bursa", "bursa malaysia", "klci index",
            "stock market", "saham", "fbm klci",
            "foreign outflow", "foreign inflow", "modal asing",
            "capital flight", "capital inflow", "foreign fund",
            "bond yield", "MGS", "malaysian government securities",
            "ringgit strengthening", "ringgit weakening",
            "ringgit terendah", "ringgit tertinggi",
            "central bank intervention", "BNM ringgit",
            "market turmoil", "market volatility",
            "investor confidence", "keyakinan pelabur",
            "foreign direct investment", "FDI", "pelaburan asing",
            "portfolio investment"]
TOPICS = ["malaysia ringgit", "KLCI malaysia", "bursa malaysia",
          "ringgit dollar", "klci index today", "malaysia stock market",
          "MGS yield", "malaysia bond", "foreign fund malaysia",
          "ringgit outlook", "klci outlook"]
WIKI = ["Malaysian ringgit", "Bursa Malaysia", "FTSE Bursa Malaysia KLCI",
        "Economy of Malaysia", "Bank Negara Malaysia"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("Ringgit / KLCI Monitor", "ringgit_klci", KEYWORDS, TOPICS, WIKI, fd, td)
