import requests

GROQ_API_KEY = "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"
GROQ_MODEL_ID = "llama-3.1-8b-instant"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": GROQ_MODEL_ID,
    "messages": [{"role": "user", "content": "Hello, can you summarize the stock market today?"}]
}

response = requests.post(
    "https://api.groq.com/v1/chat/completions",
    json=data,
    headers=headers
)

print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())
