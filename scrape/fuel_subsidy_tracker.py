#!/usr/bin/env python
"""Fuel subsidy / RON95 tracker — subsidy rationalization, price changes."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = ["fuel subsidy", "subsidi minyak", "RON95", "RON97", "diesel",
            "fuel price", "harga minyak", "fuel rationalization",
            "subsidi ditetapkan", "petrol price", "minyak petrol",
            "fuel subsidy removal", "subsidi fuel", "targeted subsidy",
            "subsidi sasar", "B40 fuel", "M40 fuel",
            "fuel hike", "minyak naik", "fuel protest",
            "pengurangan subsidi", "subsidi apung",
            "CPI fuel", "inflation fuel", "fuel impact",
            "minyak masak subsidy", "cooking oil subsidy",
            "electric tariff", "tariff elektrik", "TNB tariff"]
TOPICS = ["malaysia fuel subsidy", "RON95 malaysia", "subsidi minyak malaysia",
          "malaysia petrol price", "fuel rationalization malaysia",
          "targeted subsidy malaysia", "malaysia diesel subsidy",
          "harga minyak malaysia", "subsidi sasar malaysia"]
WIKI = ["Fuel subsidies in Malaysia", "Oil and gas in Malaysia",
        "Petronas", "Economy of Malaysia"]

if __name__ == "__main__":
    fd = datetime(2018, 5, 9, tzinfo=timezone.utc); td = datetime.now(timezone.utc)
    if "--all" in sys.argv: fd = datetime(1999, 11, 29, tzinfo=timezone.utc)
    run("Fuel Subsidy Tracker", "fuel_subsidy", KEYWORDS, TOPICS, WIKI, fd, td)
