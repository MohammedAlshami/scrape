"""Check OpenRouter for embedding and gpt-5-nano models."""
import requests, os

ROOT = os.path.dirname(os.path.abspath(__file__))
key = os.environ.get("OPENROUTER_API_KEY")
if not key:
    with open(os.path.join(ROOT, "..", ".env")) as f:
        key = f.read().strip().split("=", 1)[1].strip()

resp = requests.get(
    "https://openrouter.ai/api/v1/models",
    headers={"Authorization": f"Bearer {key}"},
    timeout=15,
)

for m in resp.json().get("data", []):
    mid = m["id"]
    if "embed" in mid.lower() or "gpt-5-nano" in mid.lower():
        pricing = m.get("pricing", {})
        print(f"{mid}")
        print(f"  prompt: {pricing.get('prompt', '?')}/token")
        print(f"  completion: {pricing.get('completion', '?')}/token")
        print()
