import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()  

MODEL_REGISTRY = {
    "gpt-5": "openai/gpt-5",
    "gpt-5-mini": "openai/gpt-5-mini",
    "gpt-5-nano": "openai/gpt-5-nano",
    "gpt-4o": "openai/gpt-4o-2024-05-13",
    "gpt-4o-mini": "openai/gpt-4o-mini",
    "gpt-3.5": "openai/gpt-3.5-turbo",
    "o1": "openai/o1",
    "o1-pro": "openai/o1-pro",
    "o3": "openai/o3",
    "o3-mini": "openai/o3-mini",
    "o3-pro": "openai/o3-pro",
    "o4-mini": "openai/o4-mini",
    "claude-haiku": "anthropic/claude-3.5-haiku",
    "deepseek-chat": "deepseek/deepseek-chat",
    "deepseek-coder": "deepseek/deepseek-coder",
    "deepseek-math": "deepseek/deepseek-math"
}

BASE_URL = "https://api.us-east-1.langdb.ai/f667eeb6-7eb2-46b6-b342-89aa70f38b9d/v1/chat/completions"
HEADERS = {
    "authorization": f"Bearer {os.getenv('LANGDB_API_KEY')}",
    "Content-Type": "application/json"
}

def query_neural(prompt, model_key="gpt-4o-mini"):
    model_id = MODEL_REGISTRY.get(model_key)
    if not model_id:
        return f"[ERROR] Unknown model key: {model_key}"

    payload = json.dumps({
        "model": model_id,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    })

    try:
        response = requests.post(BASE_URL, headers=HEADERS, data=payload)
        data = response.json()
        if "choices" not in data:
            return f"[ERROR] 'choices' missing in response: {data}"
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[ERROR] {str(e)}"
