"""Check for embedding models on OpenRouter."""
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
    if any(x in mid.lower() for x in ["embed", "ada", "text-embedding", "3-small", "3-large"]):
        pricing = m.get("pricing", {})
        print(f"{mid}")
        print(f"  prompt: {pricing.get('prompt', '?')}/token")
