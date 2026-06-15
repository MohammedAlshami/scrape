#!/usr/bin/env python
"""State election monitor — state assembly terms, election dates."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["state election", "pilihan raya negeri", "PRN",
            "state assembly", "dewan undangan negeri", "DUN",
            "state dissolve", "state sitting",
            "menteri besar", "MB", "ketua menteri", "chief minister",
            "state government", "negeri", "state coalition",
            "kelantan election", "terengganu election", "kedah election",
            "penang election", "selangor election", "perak election",
            "johor election", "pahang election", "negeri sembilan election",
            "melaka election", "perlis election", "sabah election",
            "sarawak election",
            "state budget", "belanjawan negeri",
            "state term", "negeri parliament dissolved",
            "serentak", "simultaneous election"]
TOPICS = ["malaysia state election", "PRN malaysia",
          "kelantan state election", "terengganu state election",
          "kedah state election", "penang state election",
          "selangor state election", "perak state election",
          "johor state election", "pahang state election",
          "negeri sembilan state election", "melaka state election",
          "perlis state election", "sabah state election",
          "sarawak state election",
          "malaysia state assembly term"]
WIKI = ["State governments of Malaysia", "Menteri Besar", "Ketua Menteri",
        "Elections in Malaysia", "Election Commission of Malaysia",
        "Sabah state election", "Sarawak state election",
        "Johor state election", "Melaka state election"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("State Election Monitor", "state_elections", KEYWORDS, TOPICS, WIKI, fd, td)
