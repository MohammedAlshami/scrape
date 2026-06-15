#!/usr/bin/env python
"""Defections / floor crossing tracker — MP switches, anti-hopping law cases."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["defect", "lompat", "cross floor", "party hop", "lompat parti",
            "anti-hopping", "anti lompat", "anti party hopping law",
            "MP switch", "ADUN switch", "wakil rakyat lompat",
            "seat vacancy", "kerusi kosong", "by election triggered",
            "bersatu defector", "umno defector", "pkr defector",
            "anwar supporter", "MP support", "SD declare",
            "statutory declaration", "akuan sumpah",
            "loyalty", "setia", "party discipline",
            "suspend", "gantung", "expelled", "pecat",
            "keluar parti", "quit party",
            "show cause letter", "surat tunjuk sebab",
            "government majority", "majoriti kerajaan",
            "lose majority", "hilang majoriti"]
TOPICS = ["malaysia party hopping", "lompat parti malaysia",
          "malaysia anti hopping law", "MP defection malaysia",
          "malaysia MP switch", "pindah parti malaysia",
          "ADUN lompat", "wakil rakyat lompat",
          "anti lompat undang undang", "malaysia SD"]
WIKI = ["Anti-hopping law in Malaysia", "Article 48 of the Constitution of Malaysia",
        "List of Malaysian by-elections", "Sheraton Move",
        "Malaysian United Indigenous Party", "People's Justice Party (Malaysia)"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("Defections Tracker", "defections", KEYWORDS, TOPICS, WIKI, fd, td)
