# main.py – Agente Leigos
from fastapi import FastAPI, Request
from pydantic import BaseModel
import os

app = FastAPI()

class Pergunta(BaseModel):
    mensagem: str
    usuario_id: str = "anon"

@app.post("/leigo")
async def responder(pergunta: Pergunta):
    resposta_base = gerar_resposta_leiga(pergunta.mensagem)
    return {
        "resposta": resposta_base,
        "agente": "agente_leigos"
    }

def gerar_resposta_leiga(mensagem: str) -> str:
    # Leitura do prompt base
    prompt_path = os.path.join(os.path.dirname(__file__), "prompt_leigo.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        base = f.read()
    
    # Simulação de resposta baseada na mensagem
    if "como funciona" in mensagem.lower():
        return base + "\nClaro! Eu explico do jeito mais simples possível..."
    elif "obrigado" in mensagem.lower():
        return "De nada! Qualquer dúvida, estou aqui para te ajudar. 🙌"
    else:
        return base + f"\nSobre isso que você falou, posso te orientar da seguinte forma: {mensagem}"
