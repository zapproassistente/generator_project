# app/main.py — FastAPI backend do painel ZapPRO (versão final)

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Painel ZapPRO", version="1.0")

# Configuração de rotas estáticas (CSS/JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configuração de templates (HTML)
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Painel ZapPRO"})
