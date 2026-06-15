#!/usr/bin/env python
"""EPF / withdrawal tracker — EPF special withdrawals, i-Lestari, i-Sinar, i-Citra."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["EPF", "KWSP", "employee provident fund",
            "EPF withdrawal", "pengeluaran KWSP",
            "i-Lestari", "i-Sinar", "i-Citra",
            "special withdrawal", "pengeluaran khas",
            "EPF savings", "EPF balance", "simpanan KWSP",
            "contribution cut", "potongan caruman",
            "minimum savings", "simpanan minima",
            "EPF dividend", "dividen KWSP",
            "EPF restructuring", "KWSP penyusunan semula",
            "EPF account", "akaun KWSP", "account 1", "account 2",
            "EPF member", "ahli KWSP",
            "EPF withdrawal pression", "tekanan pengeluaran KWSP",
            "withdrawal request", "permohonan pengeluaran",
            "EPF loan", "KWSP pinjaman",
            "EPF investment", "KWSP pelaburan"]
TOPICS = ["EPF malaysia", "KWSP malaysia", "EPF withdrawal",
          "EPF i-Lestari", "EPF i-Sinar", "EPF i-Citra",
          "pengeluaran KWSP", "KWSP account", "EPF dividend",
          "simpanan KWSP"]
WIKI = ["Employees Provident Fund (Malaysia)", "Social welfare programmes in Malaysia"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("EPF / Withdrawal Tracker", "epf_withdrawals", KEYWORDS, TOPICS, WIKI, fd, td)
