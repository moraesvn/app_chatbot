"""
Agente Agno básico para testar chamadas à API OpenAI.
"""
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.os import AgentOS

from app.config import settings


def create_marketplace_agent() -> Agent:
    """
    Cria um agente simples para testar a API OpenAI.
    
    Returns:
        Agent: Agente configurado para atendimento básico
    """
    agent = Agent(
        name=settings.agno_agent_name,
        model=OpenAIChat(
            id=settings.agno_model,
            api_key=settings.openai_api_key,
        ),
        markdown=True,
        description=(
            "Agente de atendimento para marketplace. "
            "Responde perguntas de clientes de forma clara e objetiva."
        ),
    )
    
    return agent


def create_agent_os() -> AgentOS:
    """
    Cria o AgentOS com o agente marketplace.
    
    Returns:
        AgentOS: Runtime configurado para servir o agente
    """
    agent = create_marketplace_agent()
    agent_os = AgentOS(agents=[agent])
    return agent_os
