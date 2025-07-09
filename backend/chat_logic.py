import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",  # Use your OpenRouter key here
    "Content-Type": "application/json"
}

def query_huggingface(prompt: str) -> str:
    payload = {
        "model": "gryphe/mythomax-l2-13b",
        "messages": [
            {"role": "system", "content": "You are Aura, a concise, helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        print("Status code:", response.status_code)
        print("Response text:", response.text)

        response.raise_for_status()
        result = response.json()

        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error querying OpenRouter:", e)
        return "Hmm... I'm having trouble thinking right now."
