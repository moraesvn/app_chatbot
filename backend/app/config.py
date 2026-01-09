"""
Configurações da aplicação usando Pydantic Settings.
"""
import os
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configurações da aplicação."""
    
    # OpenAI (obrigatório)
    openai_api_key: str
    
    # Agno Agent (opcionais com valores padrão)
    agno_agent_name: str = "Marketplace Support Agent"
    agno_model: str = "gpt-4o-mini"
    
    class Config:
        # Buscar .env na raiz do projeto (2 níveis acima de backend/app)
        env_file = Path(__file__).parent.parent.parent / ".env"
        env_file_encoding = "utf-8"


# Instância global das configurações
settings = Settings()
