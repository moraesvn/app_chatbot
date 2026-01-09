"""
Arquivo principal para inicializar o AgentOS.
"""
from agno.os import AgentOS

from app.agents.marketplace_agent import create_agent_os

# Criar o AgentOS
agent_os = create_agent_os()

# Obter a aplicação FastAPI
app = agent_os.get_app()


if __name__ == "__main__":
    # Executar o AgentOS
    agent_os.serve(
        app="app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
