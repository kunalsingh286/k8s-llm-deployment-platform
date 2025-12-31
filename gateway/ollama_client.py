import os
import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "tinyllama")


def generate_text(prompt: str) -> str:
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )
    response.raise_for_status()
    return response.json()["response"]
