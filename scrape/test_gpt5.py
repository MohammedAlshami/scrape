"""Test why GPT-5-nano returns empty with system prompts."""
import requests, os

ROOT = os.path.dirname(os.path.abspath(__file__))
key = os.environ.get("OPENROUTER_API_KEY")
if not key:
    with open(os.path.join(ROOT, "..", ".env")) as f:
        key = f.read().strip().split("=", 1)[1].strip()

headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

tests = [
    ("system prompt", {
        "model": "openai/gpt-5-nano",
        "messages": [
            {"role": "system", "content": "You are an analyst."},
            {"role": "user", "content": "Say hello in 5 words."}
        ],
        "max_tokens": 50,
    }),
    ("no system", {
        "model": "openai/gpt-5-nano",
        "messages": [
            {"role": "user", "content": "Say hello in 5 words."}
        ],
        "max_tokens": 50,
    }),
    ("long user no system", {
        "model": "openai/gpt-5-nano",
        "messages": [
            {"role": "user", "content": "Hello. " * 2000 + "Reply: Hello"}
        ],
        "max_tokens": 50,
    }),
    ("gpt-4o-mini system+long", {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are an analyst."},
            {"role": "user", "content": "Hello. " * 2000 + "What do you think?"}
        ],
        "max_tokens": 100,
    }),
]

for label, body in tests:
    try:
        resp = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            json=body, headers=headers, timeout=60,
        )
        data = resp.json()
        content = data.get("choices", [{}])[0].get("message", {}).get("content")
        print(f"{label}: status={resp.status_code}, content_len={len(content) if content else 0}")
    except Exception as e:
        print(f"{label}: ERROR {e}")
