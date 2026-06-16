"""Download individual Malaysian by-election Wikipedia pages."""

import requests, os, time

HEADERS = {"User-Agent": "ElectionPredictionBot/1.0"}
BASE = os.path.join(os.path.dirname(__file__), "..", "data", "elections", "by_elections")

BY_ELECTIONS = [
    "2000 Lunas by-election", "2000 Sanggang by-election", "2000 Telok Kemang by-election",
    "2001 Likas by-election", "2002 Anak Bukit by-election", "2002 Indera Kayangan by-election",
    "2002 Ketari by-election", "2002 Pendang by-election", "2004 Ba'kelalan by-election",
    "2004 Kuala Berang by-election", "2005 Pengkalan Pasir by-election",
    "2007 Batu Talam by-election", "2007 Ijok by-election", "2007 Machap by-election",
    "2008 Permatang Pauh by-election", "2009 Bagan Pinang by-election", "2009 Batang Air by-election",
    "2009 Bukit Gantang by-election", "2009 Bukit Selambau by-election",
    "2009 Kuala Terengganu by-election", "2009 Manek Urai by-election", "2009 Penanti by-election",
    "2009 Permatang Pasir by-election", "2010 Batu Sapi by-election", "2010 Galas by-election",
    "2010 Hulu Selangor by-election", "2010 Sibu by-election", "2011 Kerdau by-election",
    "2011 Merlimau by-election", "2011 Tenang by-election", "2013 Kuala Besut by-election",
    "2013 Sungai Limau by-election", "2014 Balingian by-election", "2014 Bukit Gelugor by-election",
    "2014 Kajang by-election", "2014 Pengkalan Kubor by-election", "2014 Telok Intan by-election",
    "2015 Chempaka by-election", "2015 Permatang Pauh by-election", "2015 Rompin by-election",
    "2016 Kuala Kangsar by-election", "2016 Sungai Besar by-election", "2017 Tanjong Datu by-election",
    "2018 Balakong by-election", "2018 Port Dickson by-election", "2018 Seri Setia by-election",
    "2018 Sungai Kandis by-election", "2019 Cameron Highlands by-election",
    "2019 Rantau by-election", "2019 Sandakan by-election", "2019 Semenyih by-election",
    "2019 Tanjung Piai by-election", "2020 Chini by-election", "2020 Kimanis by-election",
    "2020 Slim by-election", "2022 Bugaya by-election", "2022 Padang Serai by-election",
    "2023 Jepak by-election", "2023 Kemaman by-election", "2023 Kuala Terengganu by-election",
    "2023 Pelangai by-election", "2023 Pulai by-election", "2023 Simpang Jeram by-election",
    "2024 Kuala Kubu Baharu by-election", "2024 Mahkota by-election", "2024 Nenggiri by-election",
    "2024 Sungai Bakap by-election", "2025 Ayer Kuning by-election",
    "2026 Kinabatangan by-election", "2026 Lamag by-election",
]

def slug(t):
    return t.replace("'", "").replace("–", "-").replace("(", "").replace(")", "").replace(",", "").replace(" ", "_")

os.makedirs(BASE, exist_ok=True)
total = len(BY_ELECTIONS)

for i, title in enumerate(BY_ELECTIONS, 1):
    encoded = title.replace(" ", "_")
    print(f"[{i}/{total}] {title}")
    url = f"https://en.wikipedia.org/w/index.php?title={encoded}&action=raw"
    try:
        resp = requests.get(url, timeout=15, headers=HEADERS)
        if resp.status_code == 200:
            name = slug(title)
            path = os.path.join(BASE, f"{name}.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n*Source: https://en.wikipedia.org/wiki/{encoded}*\n\n---\n\n{resp.text}")
            print(f"  OK ({len(resp.text)} chars)")
        else:
            print(f"  FAIL {resp.status_code}")
    except Exception as e:
        print(f"  ERROR: {e}")
    time.sleep(0.3)

print(f"\nDone! {total} by-elections")
