"""Download DUN-level state election results from Wikipedia."""

import requests, os, time

HEADERS = {"User-Agent": "ElectionPredictionBot/1.0"}
BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "elections")

PAGES = {
    "state_2023": {
        "folder": "state_2023",
        "pages": [
            ("Results_of_the_2023_Malaysian_state_elections_by_constituency", "Results_of_the_2023_Malaysian_state_elections_by_constituency"),
        ]
    },
    "state_johor_2022": {
        "folder": "state_johor_2022",
        "pages": [
            ("2022_Johor_state_election", "2022_Johor_state_election"),
            ("Results_of_the_2022_Johor_state_election", "Results_of_the_2022_Johor_state_election"),
        ]
    },
    "state_sarawak_2021": {
        "folder": "state_sarawak_2021",
        "pages": [
            ("2021_Sarawak_state_election", "2021_Sarawak_state_election"),
            ("Results_of_the_2021_Sarawak_state_election", "Results_of_the_2021_Sarawak_state_election"),
        ]
    },
    "state_sabah_2020": {
        "folder": "state_sabah_2020",
        "pages": [
            ("2020_Sabah_state_election", "2020_Sabah_state_election"),
            ("Results_of_the_2020_Sabah_state_election", "Results_of_the_2020_Sabah_state_election"),
        ]
    },
    "state_2018": {
        "folder": "state_2018",
        "pages": [
            ("Results_of_the_2018_Malaysian_state_elections_by_constituency", "Results_of_the_2018_Malaysian_state_elections_by_constituency"),
            ("2018_Sabah_state_election", "2018_Sabah_state_election"),
            ("2018_Johor_state_election", "2018_Johor_state_election"),
            ("2018_Malacca_state_election", "2018_Malacca_state_election"),
            ("2018_Perak_state_election", "2018_Perak_state_election"),
        ]
    },
    "state_2016_sarawak": {
        "folder": "state_2016_sarawak",
        "pages": [
            ("2016_Sarawak_state_election", "2016_Sarawak_state_election"),
        ]
    },
}

total = sum(len(v["pages"]) for v in PAGES.values())
done = 0

for group_name, group in PAGES.items():
    folder_path = os.path.join(BASE, group["folder"])
    os.makedirs(folder_path, exist_ok=True)
    
    for fname, title in group["pages"]:
        done += 1
        print(f"[{done}/{total}] {group_name}: {fname}")
        
        url = f"https://en.wikipedia.org/w/index.php?title={title}&action=raw"
        try:
            resp = requests.get(url, timeout=15, headers=HEADERS)
            if resp.status_code == 200:
                path = os.path.join(folder_path, f"{fname}.md")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(f"# {fname}\n\n*Source: https://en.wikipedia.org/wiki/{title}*\n\n---\n\n{resp.text}")
                print(f"  OK ({len(resp.text)} chars)")
            else:
                print(f"  FAIL {resp.status_code}")
        except Exception as e:
            print(f"  ERROR: {e}")
        
        time.sleep(0.5)

print(f"\nDone! {done} pages downloaded")
