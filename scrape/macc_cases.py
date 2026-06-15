#!/usr/bin/env python
"""MACC / court cases — corruption probes, trials, verdicts, appeals."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["MACC", "SPRM", "malaysian anti-corruption", "rasuah", "corruption",
            "court", "mahkamah", "trial", "bicara", "charge", "pertuduhan",
            "verdict", "putusan", "guilty", "bersalah", "acquit", "bebas",
            "appeal", "rayuan", "jail", "penjara", "fine", "denda",
            "1MDB", "1MDB trial", "najib trial", "najib jail",
            "muhyiddin trial", "muhyiddin charge",
            "bribery", "suap", "kickback", "komisen",
            "money laundering", "pengubahan wang haram",
            "whistleblower", "pembocor rahsia",
            "MACC arrest", "SPRM tangkap", "MACC remand",
            "prosecution", "pendakwaan", "attorney general", "AG chambers"]
TOPICS = ["MACC malaysia", "SPRM malaysia", "malaysia corruption trial",
          "1MDB trial", "najib razak court", "muhyiddin court",
          "malaysia court verdict", "malaysia corruption case",
          "MACC investigation", "malaysia anti-corruption",
          "malaysia appeal court", "malaysia high court"]
WIKI = ["Malaysian Anti-Corruption Commission", "1MDB scandal",
        "Najib Razak", "1MDB trial", "High Court of Malaya",
        "Federal Court of Malaysia", "Court of Appeal of Malaysia",
        "Attorney General of Malaysia"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    if "--from" in sys.argv: i=sys.argv.index("--from"); p=sys.argv[i+1].split("-"); fd = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    if "--to" in sys.argv: i=sys.argv.index("--to"); p=sys.argv[i+1].split("-"); td = datetime(int(p[0]), int(p[1]), 1, tzinfo=timezone.utc)
    run("MACC / Court Cases", "macc_cases", KEYWORDS, TOPICS, WIKI, fd, td)
