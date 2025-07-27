# Dockerfile — Painel GPT ZapPRO (FastAPI)

FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Variáveis para evitar prompts no build
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependências
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar o projeto
COPY ./app ./app

# Comando padrão
CMD ["uvicorn", "app.core.main:app", "--host", "0.0.0.0", "--port", "8000"]
