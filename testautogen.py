import httpx, os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("OPENROUTER_API_KEY")
print("Key loaded:", repr(key))  # Should NOT be None or empty

r = httpx.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    json={"model": "mistralai/mistral-small-3.2-24b-instruct", "messages": [{"role": "user", "content": "Hello"}]}
)
print(r.status_code, r.json())