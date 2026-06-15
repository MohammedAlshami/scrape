import json, sys, os
sys.path.insert(0, ".")

API_KEY = os.environ.get("OPENROUTER_API_KEY") or open(".env").read().strip().split("=", 1)[1].strip()
OR_URL = "https://openrouter.ai/api/v1/chat/completions"

import requests


def extract_election_trigger(text: str, election_label: str) -> dict:
    prompt = f"""You are a Malaysian political historian. Analyze the following text about {election_label} and extract structured data about what triggered this election.

Return ONLY a JSON object:
{{
  "election": "{election_label}",
  "dissolution_date": "YYYY-MM-DD or approximate",
  "election_date": "YYYY-MM-DD",
  "prime_minister": "PM name at time",
  "government_type": "majority|coalition|minority|unity|caretaker",
  "term_status": "early|on_schedule|end_of_term",
  "months_since_last_election": number,
  "trigger_events": [
    {{
      "event": "short description",
      "date": "YYYY-MM or approximate",
      "type": "confidence_vote|coalition_break|defection|budget_fail|scandal|crisis|natural_term|other"
    }}
  ],
  "primary_trigger": "1-sentence summary of the main reason the election was called",
  "political_context": "brief description of political situation"
}}

Base your analysis ONLY on the text provided. Return ONLY valid JSON."""

    r = requests.post(OR_URL, json={
        "model": "openai/gpt-5-nano",
        "reasoning": {"effort": "high"},
        "messages": [
            {"role": "system", "content": "You are a Malaysian political historian. Return only valid JSON."},
            {"role": "user", "content": f"{prompt}\n\nTEXT:\n{text[:6000]}"},
        ],
    }, headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, timeout=60)

    if r.status_code != 200:
        return {"election": election_label, "error": f"API error: {r.status_code}"}

    content = r.json()["choices"][0]["message"]["content"]
    json_start = content.find("{")
    json_end = content.rfind("}") + 1
    if json_start >= 0 and json_end > json_start:
        try:
            return json.loads(content[json_start:json_end])
        except json.JSONDecodeError:
            return {"election": election_label, "error": "JSON parse error"}
    return {"election": election_label, "error": "No JSON found"}


def analyze_all_elections() -> list[dict]:
    from tools.wikipedia_rag import WikipediaRAG
    rag = WikipediaRAG()

    elections = [
        ("2004 Malaysian general election", "GE11 (2004)"),
        ("2008 Malaysian general election", "GE12 (2008)"),
        ("2013 Malaysian general election", "GE13 (2013)"),
        ("2018 Malaysian general election", "GE14 (2018)"),
        ("2022 Malaysian general election", "GE15 (2022)"),
    ]

    results = []
    for page, label in elections:
        result = rag.index_page(page)
        print(f"  {page}: {result}")
        if result:
            text = " ".join(rag._indexed_pages.get(page, []))[:6000]
            if text:
                analysis = extract_election_trigger(text, label)
                results.append(analysis)
                print(f"    -> dissolution={analysis.get('dissolution_date','?')}, "
                      f"trigger={analysis.get('primary_trigger','?')[:60]}")

    return results


def analyze_current_situation(election_patterns: list[dict]) -> dict:
    patterns_json = json.dumps(election_patterns, indent=2)

    prompt = f"""You are a Malaysian political analyst. Analyze these past election trigger patterns and predict GE16.

Past elections:
{patterns_json}

Current situation (use your training data):
- Current PM: Anwar Ibrahim (since Nov 2022)
- Government: PH + BN + others (unity government)
- Last election: GE15 on 19 Nov 2022
- Latest possible dissolution: Nov 2027 (constitutional limit)
- Today: {os.environ.get("CURRENT_DATE", "June 2026")}

Study the patterns above. When do Malaysian elections typically get called?
- Is it early, on schedule, or at the last minute?
- What types of events trigger a dissolution?
- What's the typical lead time from dissolution to election day?

Return ONLY a JSON object:
{{
  "prediction": {{
    "probability": float 0-1,
    "dissolution_month": "MMM YYYY",
    "election_month": "MMM YYYY",
    "window_3month": "start_month-end_month YYYY",
    "reasoning": "2-3 sentence analysis based on patterns",
    "trigger_to_watch": "what specific event would trigger GE16"
  }},
  "pattern_insights": ["insight 1", "insight 2", "insight 3"]
}}

Return ONLY valid JSON."""

    r = requests.post(OR_URL, json={
        "model": "openai/gpt-5-nano",
        "reasoning": {"effort": "high"},
        "messages": [
            {"role": "system", "content": "You are a Malaysian political analyst. Return only valid JSON."},
            {"role": "user", "content": prompt},
        ],
    }, headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, timeout=60)

    if r.status_code != 200:
        return {"prediction": {"error": f"API error: {r.status_code}"}}

    content = r.json()["choices"][0]["message"]["content"]
    json_start = content.find("{")
    json_end = content.rfind("}") + 1
    if json_start >= 0 and json_end > json_start:
        try:
            return json.loads(content[json_start:json_end])
        except json.JSONDecodeError:
            return {"prediction": {"error": "JSON parse error"}}
    return {"prediction": {"error": "No JSON found"}}
