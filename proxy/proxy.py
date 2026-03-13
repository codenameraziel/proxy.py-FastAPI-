from fastapi import FastAPI, Request
import requests

app = FastAPI()

OLLAMA_URL = "http://ollama:11434/api/chat"

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    body = await request.json()
    model = body.get("model", "mistral")
    messages = body.get("messages", [])

    # Adaptar formato para Ollama
    ollama_payload = {
        "model": model,
        "messages": messages
    }

    resp = requests.post(OLLAMA_URL, json=ollama_payload)
    data = resp.json()

    # Adaptar resposta para formato OpenAI
    return {
        "id": "chatcmpl-ollama",
        "object": "chat.completion",
        "choices": [
            {
                "index": 0,
                "message": data["message"],
                "finish_reason": "stop"
            }
        ]
    }
