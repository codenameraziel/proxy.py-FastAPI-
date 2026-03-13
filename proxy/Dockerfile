FROM python:3.10-slim

WORKDIR /app

# Instalar dependências
RUN pip install --no-cache-dir fastapi uvicorn requests

COPY proxy.py /app/proxy.py

EXPOSE 8000

CMD ["uvicorn", "proxy:app", "--host", "0.0.0.0", "--port", "8000"]
