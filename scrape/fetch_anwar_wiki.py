"""Fetch Wikipedia pages about Anwar Ibrahim and save as .md files."""

import requests, os, re, time

DIR = os.path.join(os.path.dirname(__file__), "..", "data", "anwar_ibrahim")

PAGES = [
    "Anwar Ibrahim",
    "Wan Azizah Wan Ismail",
    "Nurul Izzah Anwar",
    "People%27s Justice Party (Malaysia)",
    "National Justice Party (Malaysia)",
    "Pakatan Harapan",
    "Pakatan Rakyat",
    "Barisan Alternatif",
    "Reformasi (Malaysia)",
    "Malaysia Madani",
    "Anwar Ibrahim sodomy trials",
    "Anwar Ibrahim cabinet",
    "List of international prime ministerial trips made by Anwar Ibrahim",
    "Shadow Cabinet of Anwar Ibrahim",
    "2022 Malaysian general election",
    "2018 Malaysian general election",
    "2020%E2%80%932022 Malaysian political crisis",
    "Kajang Move",
    "Permatang Pauh (federal constituency)",
    "Mahathir Mohamad",
    "UMNO",
    "1998 in Malaysia",
    "1MDB scandal",
    "Democratic Action Party",
    "National Trust Party (Malaysia)",
    "Malaysian United Indigenous Party",
    "Barisan Nasional",
    "Perikatan Nasional",
    "2018 Port Dickson by-election",
    "2008 Permatang Pauh by-election",
    "2015 Permatang Pauh by-election",
    "Prime Minister of Malaysia",
    "Deputy Prime Minister of Malaysia",
    "Leader of the Opposition (Malaysia)",
    "Bersih",
    "Islam Hadhari",
    "Kuala Lumpur Peace Accord",
]

def slug(title):
    return title.replace("%27", "'").replace("%E2%80%93", "–").replace("%2F", "_")

HEADERS = {"User-Agent": "ElectionPredictionBot/1.0 (research project; contact@example.com)"}

def fetch_page(title):
    url = f"https://en.wikipedia.org/w/index.php?title={title}&action=raw"
    resp = requests.get(url, timeout=15, headers=HEADERS)
    if resp.status_code != 200:
        print(f"  FAIL {resp.status_code}: {slug(title)}")
        return None
    return resp.text

def save_page(title, wikitext):
    name = slug(title).replace("/", "_").replace(":", "_").replace("?", "")
    path = os.path.join(DIR, f"{name}.md")
    header = f"# {slug(title)}\n\n*Source: https://en.wikipedia.org/wiki/{title}*\n\n---\n\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(header + wikitext)
    print(f"  Saved: {name}.md ({len(wikitext)} chars)")

os.makedirs(DIR, exist_ok=True)
print(f"Saving to {DIR}")
print(f"Fetching {len(PAGES)} pages...\n")

for i, title in enumerate(PAGES, 1):
    display = slug(title)
    print(f"[{i}/{len(PAGES)}] {display}")
    wikitext = fetch_page(title)
    if wikitext:
        save_page(title, wikitext)
    time.sleep(0.5)

print("\nDone!")
