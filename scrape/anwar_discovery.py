#!/usr/bin/env python
"""Anwar Ibrahim discovery — resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = [
    "anwar", "anwar ibrahim", "dato seri anwar", "pm anwar",
    "keadilan", "parti keadilan rakyat", "pkr",
    "pakatan harapan", "ph",
    "mahathir anwar", "anwar sodomy", "anwar jail", "anwar prison",
    "anwar royal pardon", "anwar cabinet", "anwar government",
    "anwar budget", "anwar reformasi", "anwar madani",
    "anwar economy", "anwar umno", "anwar politics",
    "ibrahim",
]

TOPICS = [
    "anwar ibrahim", "dato seri anwar", "pm anwar ibrahim",
    "anwar ibrahim policy", "anwar ibrahim budget",
    "anwar ibrahim cabinet", "anwar ibrahim government",
    "anwar ibrahim reformasi", "anwar ibrahim madani",
    "anwar ibrahim economy", "anwar ibrahim pkr",
    "anwar ibrahim pakatan harapan", "anwar ibrahim mahathir",
    "anwar ibrahim sodomy", "anwar ibrahim prison",
    "anwar ibrahim royal pardon", "anwar ibrahim umno",
    "anwar ibrahim interview", "anwar ibrahim speech",
    "siapa anwar ibrahim", "anwar ibrahim perdana menteri",
    "anwar ibrahim kewangan", "anwar ibrahim dasar",
    "anwar ibrahim belanjawan", "anwar ibrahim keadilan",
]

WIKI_PAGES = [
    "Anwar Ibrahim", "Anwar Ibrahim sodomy trials",
    "Reformasi (Malaysia)", "People's Justice Party (Malaysia)",
    "Pakatan Harapan", "Pakatan Rakyat", "1998 Malaysian Reformasi",
    "Mahathir Mohamad", "Mahathir\u2013Anwar Ibrahim political feud",
    "2008 Malaysian general election", "2013 Malaysian general election",
    "2018 Malaysian general election", "2022 Malaysian general election",
    "Anwar Ibrahim cabinet", "Madani Economy",
    "Malaysian United Indigenous Party", "Sheraton Move",
]

if __name__ == "__main__":
    from_date = datetime(2018, 5, 9, tzinfo=timezone.utc)
    to_date = datetime.now(timezone.utc)
    if "--all" in sys.argv:
        from_date = datetime(1999, 11, 29, tzinfo=timezone.utc)
    if "--from" in sys.argv:
        i = sys.argv.index("--from")
        p = sys.argv[i + 1].split("-")
        from_date = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    if "--to" in sys.argv:
        i = sys.argv.index("--to")
        p = sys.argv[i + 1].split("-")
        to_date = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)

    run("Anwar Ibrahim Discovery", "anwar_ibrahim", KEYWORDS, TOPICS, WIKI_PAGES, from_date, to_date)
