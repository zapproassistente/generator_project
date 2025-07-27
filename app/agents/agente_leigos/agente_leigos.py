# agente_leigos.py — Agente plugável para onboarding de usuários leigos
import os

def carregar_prompt_base():
    """
    Lê o arquivo de prompt base (prompt_leigo.txt) do diretório do agente.
    """
    caminho = os.path.join(os.path.dirname(__file__), "prompt_leigo.txt")
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def responder_leigo(mensagem: str) -> str:
    """
    Gera uma resposta amigável, didática, baseada na mensagem do usuário.
    """
    prompt_base = carregar_prompt_base()
    mensagem_lower = mensagem.lower()

    if "como funciona" in mensagem_lower:
        return prompt_base + "\nClaro! Vou explicar do jeito mais simples possível..."
    elif "obrigado" in mensagem_lower:
        return "De nada! Qualquer dúvida, estou aqui para te ajudar. 🙌"
    else:
        return (
            prompt_base +
            f"\nSobre sua dúvida, posso te orientar da seguinte forma: {mensagem}"
        )

# Exemplo de uso local (para teste rápido via terminal)
if __name__ == "__main__":
    while True:
        user_input = input("Você: ")
        if user_input.strip().lower() in ["sair", "exit", "q"]:
            break
        print("Agente Leigos:", responder_leigo(user_input))
