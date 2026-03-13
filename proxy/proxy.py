from fastapi import FastAPI, Request
import requests

app = FastAPI()

# URL interna do Ollama (nome do serviço no docker-compose)
OLLAMA_URL = "http://ollama:11434/api/chat"

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    body = await request.json()
    model = body.get("model", "mistral")
    messages = body.get("messages", [])

    # Payload para Ollama
    ollama_payload = {
        "model": model,
        "messages": messages,
        "stream": False,   # força resposta única em JSON
        "options": {
            "num_predict": 128   # limita saída a ~128 tokens
        }
    }

    # Timeout aumentado para evitar abortar cedo
    resp = requests.post(OLLAMA_URL, json=ollama_payload, timeout=120)
    data = resp.json()

    # Extrair texto da resposta
    content = data.get("message", {}).get("content", "")

    # Adaptar para formato OpenAI
    return {
        "id": "chatcmpl-ollama",
        "object": "chat.completion",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": content
                },
                "finish_reason": "stop"
            }
        ]
    }
