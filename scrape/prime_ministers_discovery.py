#!/usr/bin/env python
"""All Prime Ministers of Malaysia (GE10-GE15) — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = [
    "mahathir", "tun mahathir", "mahathir mohamad",
    "abdullah", "abdullah ahmad badawi", "pak lah",
    "najib", "najib razak", "najib tun razak",
    "muhyiddin", "muhyiddin yassin", "tan sri muhyiddin",
    "ismail sabri", "ismail sabri yaakob",
    "perdana menteri", "prime minister malaysia",
    "tun", "datuk seri",
]

TOPICS = [
    "mahathir mohamad", "tun mahathir",
    "abdullah ahmad badawi", "pak lah",
    "najib razak", "najib tun razak",
    "muhyiddin yassin", "tan sri muhyiddin",
    "ismail sabri yaakob",
    "perdana menteri malaysia",
    "prime minister malaysia",
]

WIKI_PAGES = [
    "Mahathir Mohamad", "Abdullah Ahmad Badawi",
    "Najib Razak", "Muhyiddin Yassin",
    "Ismail Sabri Yaakob",
    "List of prime ministers of Malaysia",
    "1Malaysia", "1MDB", "1MDB scandal",
    "Bersih", "Malaysian United Indigenous Party",
    "Perikatan Nasional", "Barisan Nasional",
    "Pakatan Harapan", "Sheraton Move",
    "Malaysian general election, 2018",
    "Malaysian general election, 2022",
    "COVID-19 pandemic in Malaysia",
]

if __name__ == "__main__":
    from_date = datetime(1999, 11, 29, tzinfo=timezone.utc)  # GE10
    to_date = datetime.now(timezone.utc)
    if "--from" in sys.argv:
        i = sys.argv.index("--from")
        p = sys.argv[i + 1].split("-")
        from_date = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    if "--to" in sys.argv:
        i = sys.argv.index("--to")
        p = sys.argv[i + 1].split("-")
        to_date = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)

    run("Prime Ministers (GE10-GE15)", "prime_ministers", KEYWORDS, TOPICS, WIKI_PAGES, from_date, to_date)
