#!/usr/bin/env python
"""EC / Election Commission monitor — voter rolls, redelineation, election prep."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["Election Commission", "Suruhanjaya Pilihan Raya", "SPR",
            "voter roll", "daftar pemilih", "automatic registration",
            "undi 18", "undi18", "voting age", "18 year old vote",
            "redelineation", "delimitation", "persempadanan",
            "constituency", "kawasan pilihan raya",
            "electoral boundary", "semakan sempadan",
            "gerrymandering", "gerimander",
            "election preparation", "persiapan pilihan raya",
            "election logistics", "logistik PRU",
            "voter list", "senarai pemilih", "cleaning roll",
            "election fund", "peruntukan pilihan raya",
            "SPR chairman", "SPR meeting", "EC chairman",
            "election campaign", "kempen pilihan raya",
            "election observer", "pemerhati pilihan raya",
            "nomination", "penamaan calon"]
TOPICS = ["SPR malaysia", "election commission malaysia",
          "voter registration malaysia", "undi 18 malaysia",
          "redelineation malaysia", "persempadanan malaysia",
          "daftar pemilih malaysia", "automatic voter malaysia",
          "SPR chairman malaysia", "SPR proposal"]
WIKI = ["Election Commission of Malaysia", "Undi18", "Voting age",
        "Elections in Malaysia", "Redelineation in Malaysia"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("EC / Election Commission", "ec_monitor", KEYWORDS, TOPICS, WIKI, fd, td)
