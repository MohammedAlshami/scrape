#!/usr/bin/env python
"""Pension / civil service reform — pension changes, retirement age, civil service pay."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["pension", "pencen", "civil service", "penjawat awam",
            "public service", "perkhidmatan awam", "government servant",
            "retirement", "persaraan", "retirement age",
            "pension reform", "pembaharuan pencen",
            "EPF", "KWSP", "employee provident fund",
            "contributions", "caruman", "employer contribution",
            "minimum pension", "pencen minimum",
            "civil service pay", "gaji penjawat awam",
            "public sector wage", "imbalan", "civil service allowance",
            "pensionable", "pencen boleh", "government pension",
            "pension cut", "pension removal",
            "pension scheme", "skim pencen", "new pension",
            "contract appointment", "jawatan kontrak",
            "public service commission", "SPA", "suruhanjaya perkhidmatan awam"]
TOPICS = ["malaysia pension reform", "civil service malaysia",
          "penjawat awam malaysia", "malaysia pension scheme",
          "EPF malaysia", "KWSP malaysia",
          "malaysia retirement age", "gaji penjawat awam",
          "pembaharuan pencen malaysia"]
WIKI = ["Employees Provident Fund (Malaysia)", "Pensions in Malaysia",
        "Civil service in Malaysia", "Public Service Commission of Malaysia"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("Pension / Civil Service", "pension_civil_service", KEYWORDS, TOPICS, WIKI, fd, td)
