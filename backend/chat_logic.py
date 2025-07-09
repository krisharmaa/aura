import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",  # Your OpenRouter key in .env
    "Content-Type": "application/json"
}

# Persistent conversation history
conversation_history = [
    {
        "role": "system",
        "content": (
            "You are Aura, a warm, supportive, and natural-sounding AI tutor. "
            "You help users learn through friendly, human-like conversations. "
            "Be expressive, kind, and adjust tone based on the user's style. "
            "Use emojis sparingly, and keep explanations concise and engaging."
        )
    }
]

def query_huggingface(prompt: str) -> str:
    # Add the user's message to the conversation
    conversation_history.append({
        "role": "user",
        "content": prompt
    })

    payload = {
        "model": "gryphe/mythomax-l2-13b",
        "messages": conversation_history
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        print("Status code:", response.status_code)
        print("Response text:", response.text)

        response.raise_for_status()
        result = response.json()

        # Get the reply from the response
        reply = result["choices"][0]["message"]["content"].strip()

        # Add assistant's reply to history
        conversation_history.append({
            "role": "assistant",
            "content": reply
        })

        return reply
    except Exception as e:
        print("Error querying OpenRouter:", e)
        return "Sorry, I couldn't respond right now. Please try again soon."
