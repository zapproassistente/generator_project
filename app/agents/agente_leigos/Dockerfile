# Dockerfile — Agente Leigos ZapPRO (FastAPI)

FROM python:3.11-slim

WORKDIR /agent

# Copia requirements e instala dependências
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia código e prompt
COPY . .

# Expõe a porta padrão
EXPOSE 8080

# Comando padrão do container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
