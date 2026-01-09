"""
Script simples para testar o agente OpenAI.
Execute: python test_agent.py
"""
import asyncio
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Ajustar encoding para Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Carregar variáveis de ambiente da raiz do projeto
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

from app.agents.marketplace_agent import create_marketplace_agent


async def test_agent():
    """Testa o agente com uma pergunta simples."""
    print("Criando agente...")
    agent = create_marketplace_agent()
    
    print("Enviando pergunta de teste...")
    pergunta = "Olá, como posso ajudar um cliente que quer saber sobre o prazo de entrega?"
    
    print(f"\nPergunta: {pergunta}\n")
    
    resposta = await agent.arun(pergunta)
    
    print(f"Resposta do agente:\n{resposta.content}\n")
    print("Teste concluido com sucesso!")


if __name__ == "__main__":
    # Verificar se a API key está configurada
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key.startswith("sk-proj-XXXX"):
        print("ERRO: OPENAI_API_KEY nao encontrada ou nao configurada no arquivo .env")
        print("   Configure a chave no arquivo .env na raiz do projeto")
        exit(1)
    
    asyncio.run(test_agent())
