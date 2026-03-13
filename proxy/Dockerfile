# Dockerfile para o proxy FastAPI
FROM python:3.11-slim

# Instala dependências basicas
RUN pip install --no-cache-dir fastapi uvicorn requests

# Copia o codigo do proxy para dentro do container
WORKDIR /app
COPY proxy.py /app/proxy.py

# Define a variavel de ambiente para o Ollama
ENV OLLAMA_URL=http://ollama:11434/api/chat

# Comando para rodar o servidor FastAPI
CMD ["uvicorn", "proxy:app", "--host", "0.0.0.0", "--port", "8000"]
