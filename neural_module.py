import os
import requests
import json

def query_neural(prompt):
    url = "https://api.us-east-1.langdb.ai/f667eeb6-7eb2-46b6-b342-89aa70f38b9d/v1/chat/completions"

    payload = json.dumps({
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    })

    headers = {
        "authorization": "Bearer langdb_ajltSjNKTU1SODI0ck9iRlhtaEJIMThXYndicVg5",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[ERROR] {str(e)}"