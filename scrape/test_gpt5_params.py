"""Test gpt-5-nano with different params."""
import requests, os

ROOT = os.path.dirname(os.path.abspath(__file__))
key = os.environ.get("OPENROUTER_API_KEY")
if not key:
    with open(os.path.join(ROOT, "..", ".env")) as f:
        key = f.read().strip().split("=", 1)[1].strip()

headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

# Try gpt-5-nano with various params
body = {
    "model": "openai/gpt-5-nano",
    "messages": [{"role": "user", "content": "Say hello in 3 words"}],
    "max_tokens": 50,
}

resp = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    json=body, headers=headers, timeout=30,
)
data = resp.json()
content = data.get("choices", [{}])[0].get("message", {}).get("content")
finish = data.get("choices", [{}])[0].get("finish_reason")
print(f"gpt-5-nano: status={resp.status_code}, finish={finish}")
print(f"  content={repr(content)}")
print(f"  usage={data.get('usage')}")

# Try reasoning parameter
body2 = {
    "model": "openai/gpt-5-nano",
    "messages": [{"role": "user", "content": "Say hello in 3 words"}],
    "max_tokens": 50,
    "reasoning": {"effort": "low"},
}
resp2 = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    json=body2, headers=headers, timeout=30,
)
data2 = resp2.json()
content2 = data2.get("choices", [{}])[0].get("message", {}).get("content")
print(f"\ngpt-5-nano+reasoning: status={resp2.status_code}")
print(f"  content={repr(content2)}")

# Also try with extra body param "include_reasoning": true
body3 = {**body, "include_reasoning": True}
resp3 = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    json=body3, headers=headers, timeout=30,
)
data3 = resp3.json()
content3 = data3.get("choices", [{}])[0].get("message", {}).get("content")
print(f"\ngpt-5-nano+include_reasoning: status={resp3.status_code}")
print(f"  content={repr(content3)}")
