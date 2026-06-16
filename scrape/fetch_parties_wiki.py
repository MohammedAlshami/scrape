"""Fetch Wikipedia pages for all Malaysian political parties and save as .md files."""

import requests, os, time, json

HEADERS = {"User-Agent": "ElectionPredictionBot/1.0 (research project; contact@example.com)"}
BASE = os.path.join(os.path.dirname(__file__), "..", "data", "parties")

PARTIES = {
    "barisan_nasional": {
        "name": "Barisan Nasional",
        "pages": [
            "Barisan Nasional",
            "Alliance Party (Malaysia)",
            "Muafakat Nasional",
        ]
    },
    "perikatan_nasional": {
        "name": "Perikatan Nasional",
        "pages": ["Perikatan Nasional"]
    },
    "pakatan_harapan": {
        "name": "Pakatan Harapan",
        "pages": ["Pakatan Harapan", "Buku Jingga", "Seventh Mahathir cabinet"]
    },
    "pakatan_rakyat": {
        "name": "Pakatan Rakyat",
        "pages": ["Pakatan Rakyat"]
    },
    "barisan_alternatif": {
        "name": "Barisan Alternatif",
        "pages": ["Barisan Alternatif"]
    },
    "gabungan_parti_sarawak": {
        "name": "Gabungan Parti Sarawak",
        "pages": ["Gabungan Parti Sarawak"]
    },
    "gabungan_rakyat_sabah": {
        "name": "Gabungan Rakyat Sabah",
        "pages": ["Gabungan Rakyat Sabah"]
    },
    "umno": {
        "name": "UMNO",
        "pages": [
            "UMNO",
            "United Malays National Organisation leadership elections",
            "President of the United Malays National Organisation",
            "UMNO Youth",
            "1987 United Malays National Organisation leadership election",
            "2009 United Malays National Organisation leadership election",
            "2018 United Malays National Organisation leadership election",
            "2023 United Malays National Organisation leadership election",
            "United Malays National Organisation of Sabah",
        ]
    },
    "pas": {
        "name": "PAS",
        "pages": [
            "Malaysian Islamic Party",
            "Green Wave (Malaysia)",
            "Pan-Malaysian Islamic Front",
        ]
    },
    "dap": {
        "name": "DAP",
        "pages": [
            "Democratic Action Party",
            "2025 Democratic Action Party National Congress",
        ]
    },
    "pkr": {
        "name": "PKR",
        "pages": [
            "People%27s Justice Party (Malaysia)",
            "National Justice Party (Malaysia)",
            "2018 People%27s Justice Party leadership election",
            "2022 People%27s Justice Party leadership election",
            "2025 People%27s Justice Party leadership election",
        ]
    },
    "bersatu": {
        "name": "BERSATU",
        "pages": [
            "Malaysian United Indigenous Party",
            "2020 Malaysian United Indigenous Party leadership election",
            "2024 Malaysian United Indigenous Party leadership election",
        ]
    },
    "amanah": {
        "name": "AMANAH",
        "pages": ["National Trust Party (Malaysia)"]
    },
    "mic": {
        "name": "MIC",
        "pages": [
            "Malaysian Indian Congress",
            "Malaysian Indian Muslim Congress",
            "All Malaysian Indian Progressive Front",
            "Malaysian Indian People%27s Party",
        ]
    },
    "mca": {
        "name": "MCA",
        "pages": ["Malaysian Chinese Association"]
    },
    "gerakan": {
        "name": "GERAKAN",
        "pages": ["Parti Gerakan Rakyat Malaysia"]
    },
    "muda": {
        "name": "MUDA",
        "pages": ["Malaysian United Democratic Alliance"]
    },
    "pbm": {
        "name": "PBM",
        "pages": ["Parti Bangsa Malaysia"]
    },
    "pejuang": {
        "name": "PEJUANG",
        "pages": ["Homeland Fighter%27s Party", "Gerakan Tanah Air"]
    },
    "psm": {
        "name": "PSM",
        "pages": ["Socialist Party of Malaysia"]
    },
    "ppp": {
        "name": "PPP",
        "pages": ["People%27s Progressive Party (Malaysia)"]
    },
    "putra": {
        "name": "PUTRA",
        "pages": ["Parti Bumiputera Perkasa Malaysia"]
    },
    "prm": {
        "name": "PRM",
        "pages": ["Parti Rakyat Malaysia"]
    },
    "warisan": {
        "name": "WARISAN",
        "pages": ["Heritage Party (Malaysia)"]
    },
    "pbs": {
        "name": "PBS",
        "pages": ["United Sabah Party"]
    },
    "gagasan": {
        "name": "GAGASAN",
        "pages": ["Parti Gagasan Rakyat Sabah"]
    },
    "upko": {
        "name": "UPKO",
        "pages": ["United Progressive Kinabalu Organisation"]
    },
    "pbb": {
        "name": "PBB",
        "pages": ["Parti Pesaka Bumiputera Bersatu"]
    },
    "supp": {
        "name": "SUPP",
        "pages": ["Sarawak United Peoples%27 Party"]
    },
    "prs_sarawak": {
        "name": "PRS",
        "pages": ["Sarawak Peoples%27 Party", "Parti Bansa Dayak Sarawak"]
    },
    "pdp": {
        "name": "PDP",
        "pages": ["Progressive Democratic Party (Malaysia)"]
    },
    "psb_sarawak": {
        "name": "PSB",
        "pages": ["Parti Sarawak Bersatu"]
    },
    "snap": {
        "name": "SNAP",
        "pages": ["Sarawak National Party"]
    },
    "kdm": {
        "name": "KDM",
        "pages": ["Social Democratic Harmony Party"]
    },
    "elections": {
        "name": "Elections",
        "pages": [
            "Elections in Malaysia",
            "1959 Malaysian general election",
            "1964 Malaysian general election",
            "1969 Malaysian general election",
            "1974 Malaysian general election",
            "1978 Malaysian general election",
            "1982 Malaysian general election",
            "1986 Malaysian general election",
            "1990 Malaysian general election",
            "1995 Malaysian general election",
            "1999 Malaysian general election",
            "2004 Malaysian general election",
            "2008 Malaysian general election",
            "2013 Malaysian general election",
            "2018 Malaysian general election",
            "2022 Malaysian general election",
            "Next Malaysian general election",
            "2022 Johor state election",
            "2023 Malaysian state elections",
            "2025 Sabah state election",
            "2021 Sarawak state election",
            "Results of the 2022 Malaysian general election by parliamentary constituency",
            "Results of the 2018 Malaysian general election by parliamentary constituency",
            "List of the winning political parties in the Malaysian general election by parliamentary constituency",
        ]
    },
    "related": {
        "name": "Related Concepts",
        "pages": [
            "Politics of Malaysia",
            "List of political parties in Malaysia",
            "Malaysia",
            "Ketuanan Melayu",
            "13 May incident",
            "2020%E2%80%932022 Malaysian political crisis",
            "Frog (Malaysian politics)",
            "Big tent (Malaysian politics)",
            "Green Wave (Malaysia)",
            "Grand coalition",
            "Perkasa",
            "Buku Jingga",
        ]
    },
}

skipped = set()

def fetch_page(title):
    url = f"https://en.wikipedia.org/w/index.php?title={title}&action=raw"
    try:
        resp = requests.get(url, timeout=15, headers=HEADERS)
        if resp.status_code == 200:
            return resp.text
        print(f"    FAIL {resp.status_code}: {title}")
    except Exception as e:
        print(f"    ERROR: {title} - {e}")
    skipped.add(title)
    return None

def slug(title):
    return title.replace("%27", "'").replace("%E2%80%93", "–").replace("%2F", "_").replace("%27", "'")

total_pages = sum(len(v["pages"]) for v in PARTIES.values())
done = 0
start = time.time()

for folder, info in PARTIES.items():
    folder_path = os.path.join(BASE, folder)
    os.makedirs(folder_path, exist_ok=True)

    for title in info["pages"]:
        done += 1
        display = slug(title)
        print(f"[{done}/{total_pages}] {info['name']} -> {display}")

        wikitext = fetch_page(title)
        if wikitext:
            name = display.replace("/", "_").replace(":", "_").replace("?", "").replace("|", "_")
            path = os.path.join(folder_path, f"{name}.md")
            header = f"# {display}\n\n*Source: https://en.wikipedia.org/wiki/{title}*\n\n---\n\n"
            with open(path, "w", encoding="utf-8") as f:
                f.write(header + wikitext)

        time.sleep(0.3)

elapsed = time.time() - start
print(f"\nDone! {done} pages in {elapsed:.0f}s")
if skipped:
    print(f"Skipped {len(skipped)}: {', '.join(sorted(skipped))}")
