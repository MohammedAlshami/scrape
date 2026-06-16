"""Find working max_tokens for gpt-5-nano."""
import requests, os

ROOT = os.path.dirname(os.path.abspath(__file__))
key = os.environ.get("OPENROUTER_API_KEY")
if not key:
    with open(os.path.join(ROOT, "..", ".env")) as f:
        key = f.read().strip().split("=", 1)[1].strip()

for max_tok in [2000, 500, 100]:
    body = {
        "model": "openai/gpt-5-nano",
        "messages": [{"role": "user", "content": "Say hello in 5 words"}],
        "max_tokens": max_tok,
    }
    resp = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        json=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        timeout=30,
    )
    data = resp.json()
    content = data.get("choices", [{}])[0].get("message", {}).get("content")
    finish = data.get("choices", [{}])[0].get("finish_reason")
    usage = data.get("usage", {})
    reas = usage.get("completion_tokens_details", {}).get("reasoning_tokens", 0)
    comp = usage.get("completion_tokens", 0)
    has = "YES" if content else "NO"
    print(f"max_tokens={max_tok}: finish={finish}, reasoning={reas}, completion={comp}, has_content={has}")
    if content:
        print(f"  content={repr(content[:100])}")
