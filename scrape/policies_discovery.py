#!/usr/bin/env python
"""Policy discovery — GE14 -> today. Resumable."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, timezone
from scraper_base import run

KEYWORDS = [
    "policy", "policies", "budget", "belanjawan", "peruntukan",
    "reform", "reforms", "bill", "undang-undang", "akta",
    "law", "laws", "peraturan", "regulation", "regulations",
    "scheme", "skim", "program", "plan", "plans", "hala tuju",
    "pelan", "initiative", "inisiatif", "subsidy", "subsidies",
    "subsidi", "tax", "taxes", "cukai", "gst", "sst",
    "minimum wage", "upah minimum", "bantuan", "bantuan sara hidup",
    "bsh", "sara hidup", "my-salam", "peka b40", "ptptn",
    "mydigital", "jendela", "5g", "anti-hopping", "voting age",
    "pension", "pencen", "national health", "perumahan",
    "pr1ma", "rumah mampu milik", "subsidi minyak", "ron95",
    "civil service", "penjawat awam", "socso", "perkeso",
    "epf", "kwsp", "foreign workers", "immigration",
    "renewable energy", "palm oil", "agriculture", "pertanian",
    "tvet", "tourism", "pelancongan", "halal", "women", "wanita",
    "child", "kanak-kanak", "disabled", "oku", "ma63",
    "malaysia agreement", "petronas", "cptpp", "rcep",
    "digital bank", "fintech", "public transport",
    "food security", "jaminan makanan", "climate policy",
]

TOPICS = [
    "malaysia policy", "malaysia budget", "malaysia tax",
    "malaysia law", "malaysia subsidy", "malaysia reform",
    "malaysia parliament", "malaysia scheme", "malaysia plan",
    "malaysia education", "malaysia healthcare",
    "malaysia housing", "malaysia pension",
    "malaysia minimum wage", "malaysia epf",
    "malaysia social security", "malaysia immigration",
    "malaysia defence", "malaysia energy", "malaysia agriculture",
    "malaysia digital", "malaysia trade",
    "malaysia transport", "malaysia civil service",
    "malaysia anti-corruption", "malaysia human rights",
    "malaysia ma63", "malaysia sabah",
    "malaysia subsidy minyak", "malaysia gst sst",
    "malaysia belanjawan", "malaysia undi18",
    "malaysia anti lompat", "malaysia ptptn",
    "malaysia bsh", "malaysia pr1ma",
]

WIKI_PAGES = [
    "Budget of Malaysia", "MySalam", "Bantuan Sara Hidup", "PTPTN",
    "Malaysia Digital Economy Corporation",
    "Goods and Services Tax (Malaysia)", "Sales and Services Tax (Malaysia)",
    "Education in Malaysia", "Healthcare in Malaysia", "Economy of Malaysia",
    "Federal Constitution of Malaysia", "Social welfare programmes in Malaysia",
    "1Malaysia People's Aid", "Malaysia COVID-19 pandemic",
    "Cabinet of Malaysia", "List of Malaysian federal legislation",
    "Human rights in Malaysia", "Transport in Malaysia",
    "Energy policy of Malaysia", "Agriculture in Malaysia",
    "Malaysian Anti-Corruption Commission", "Foreign relations of Malaysia",
    "Malaysia Agreement", "MA63",
    "Poverty in Malaysia", "Housing in Malaysia",
    "Women in Malaysia", "Youth in Malaysia",
    "Police in Malaysia", "Military of Malaysia",
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

    run("Policies Discovery", "policies", KEYWORDS, TOPICS, WIKI_PAGES, from_date, to_date)
