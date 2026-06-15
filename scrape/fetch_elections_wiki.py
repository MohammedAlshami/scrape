"""Download Wikipedia election pages for GE10-GE15 and by-elections."""

import requests, os, time

HEADERS = {"User-Agent": "ElectionPredictionBot/1.0"}
BASE = os.path.join(os.path.dirname(__file__), "..", "data", "elections")

ELECTIONS = {
    "ge10": [
        "1999 Malaysian general election",
        "1999 Malaysian state elections",
    ],
    "ge11": [
        "2004 Malaysian general election",
        "Results of the 2004 Malaysian general election by parliamentary constituency",
    ],
    "ge12": [
        "2008 Malaysian general election",
        "Results of the 2008 Malaysian general election by parliamentary constituency",
        "2008 Malaysian opposition wave",
    ],
    "ge13": [
        "2013 Malaysian general election",
        "Results of the 2013 Malaysian general election by parliamentary constituency",
        "Results of the 2013 Malaysian state elections by constituency",
        "2013 Malaysian general election protest",
    ],
    "ge14": [
        "2018 Malaysian general election",
        "Results of the 2018 Malaysian general election by parliamentary constituency",
        "Results of the 2018 Malaysian state elections by constituency",
        "List of candidates in the 2018 Malaysian general election",
        "International reactions to the 2018 Malaysian general election",
        "Endorsements in the 2018 Malaysian general election",
    ],
    "ge15": [
        "2022 Malaysian general election",
        "Results of the 2022 Malaysian general election by parliamentary constituency",
        "Results of the 2022 Malaysian state elections by constituency",
        "List of candidates in the 2022 Malaysian general election",
        "Endorsements in the 2022 Malaysian general election",
    ],
    "by_elections": [
        "List of parliamentary by-elections in Malaysia",
        "List of state by-elections in Malaysia",
    ],
    "reference": [
        "Elections in Malaysia",
        "Next Malaysian general election",
        "List of Malaysian electoral districts",
        "List of the winning political parties in the Malaysian general election by parliamentary constituency",
    ],
}

total = sum(len(v) for v in ELECTIONS.values())
done = 0

def slug(t):
    return t.replace("'", "").replace("–", "-").replace("(", "").replace(")", "").replace(",", "").replace(" ", "_")

for folder, titles in ELECTIONS.items():
    fpath = os.path.join(BASE, folder)
    os.makedirs(fpath, exist_ok=True)
    for title in titles:
        done += 1
        encoded = title.replace(" ", "_")
        print(f"[{done}/{total}] {folder}: {title}")
        url = f"https://en.wikipedia.org/w/index.php?title={encoded}&action=raw"
        try:
            resp = requests.get(url, timeout=15, headers=HEADERS)
            if resp.status_code == 200:
                name = slug(title)
                path = os.path.join(fpath, f"{name}.md")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(f"# {title}\n\n*Source: https://en.wikipedia.org/wiki/{encoded}*\n\n---\n\n{resp.text}")
                print(f"  -> saved ({len(resp.text)} chars)")
            else:
                print(f"  FAIL {resp.status_code}")
        except Exception as e:
            print(f"  ERROR: {e}")
        time.sleep(0.3)

print(f"\nDone! {done} pages")
