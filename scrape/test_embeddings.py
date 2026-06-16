"""Check OpenRouter embeddings endpoint and test morph model."""
import requests, os

ROOT = os.path.dirname(os.path.abspath(__file__))
key = os.environ.get("OPENROUTER_API_KEY")
if not key:
    with open(os.path.join(ROOT, "..", ".env")) as f:
        key = f.read().strip().split("=", 1)[1].strip()

headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

# Test the morph embedding model via chat completions
body = {
    "model": "morph/morph-v3-large",
    "messages": [
        {"role": "user", "content": "Generate an embedding vector for: Malaysia general election 2026 prediction Anwar Ibrahim"}
    ],
    "max_tokens": 1
}
resp = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    json=body, headers=headers, timeout=30
)
data = resp.json()
if "error" in str(data).lower():
    # Try embedding endpoint instead
    body2 = {
        "model": "morph/morph-v3-large",
        "input": "Malaysia general election 2026"
    }
    resp2 = requests.post(
        "https://openrouter.ai/api/v1/embeddings",
        json=body2, headers=headers, timeout=30
    )
    d2 = resp2.json()
    if "data" in d2:
        print(f"Embeddings endpoint WORKS! Vector dims: {len(d2['data'][0]['embedding'])}")
    else:
        print(f"Embeddings endpoint failed: {str(d2)[:200]}")
else:
    print(f"Chat endpoint returned: {str(data)[:200]}")
