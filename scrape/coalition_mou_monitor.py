#!/usr/bin/env python
"""Coalition / MOU monitor — confidence agreements, CSA expiry, coalition shifts."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["confidence agreement", "CSA", "MOU", "memorandum persefahaman",
            "confidence supply", "supply agreement",
            "political stability", "kestabilan politik",
            "coalition agreement", "perjanjian gabungan",
            "MoU expired", "CSA renewal",
            "anwar agreement", "anwar BN", "anwar GPS",
            "PKR BN MoU", "PKR GPS MoU",
            "split", "retak", "breakup", "coalition break",
            "new coalition", "gabungan baru",
            "realignment", "pakatan baru", "political pact",
            "coalition meeting", "coalition supreme council",
            "BN supreme council", "PH presidential council",
            "PN supreme council", "GPS supreme council"]
TOPICS = ["malaysia coalition agreement", "malaysia MOU", "CSA malaysia",
          "malaysia political stability", "confidence agreement malaysia",
          "anwar BN agreement", "anwar GPS agreement",
          "pakatan harapan coalition", "barisan nasional coalition",
          "perikatan nasional coalition", "gabungan parti sarawak"]
WIKI = ["Pakatan Harapan", "Barisan Nasional", "Perikatan Nasional",
        "Gabungan Parti Sarawak", "Anwar Ibrahim cabinet",
        "Sheraton Move"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("Coalition / MOU Monitor", "coalition_mou", KEYWORDS, TOPICS, WIKI, fd, td)
