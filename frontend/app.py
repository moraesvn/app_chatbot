import sys
import os
from pathlib import Path

# Caminho absoluto do projeto e do backend
project_root = Path(__file__).resolve().parent.parent
backend_path = project_root / "backend"

# Garante que o backend esteja no sys.path
backend_path_resolved = str(backend_path.resolve())
if backend_path_resolved not in sys.path:
    sys.path.insert(0, backend_path_resolved)

import streamlit as st
from dotenv import load_dotenv

# Carregar variáveis de ambiente
env_path = project_root / ".env"
load_dotenv(env_path)

# Import do agente
from app.agents.marketplace_agent import create_marketplace_agent


# Configuração da página
st.set_page_config(
    page_title="Agente Marketplace - Teste",
    page_icon="🤖",
    layout="wide",
)

# Título
st.title("🤖 Agente de Atendimento Marketplace")
st.markdown("Interface para testar o agente durante o desenvolvimento")

# Inicializar o agente (usando cache do Streamlit)
@st.cache_resource
def get_agent():
    """Cria e retorna o agente (cacheado pelo Streamlit)."""
    try:
        agent = create_marketplace_agent()
        return agent, None
    except Exception as e:
        return None, str(e)

# Verificar se a API key está configurada
api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key.startswith("sk-proj-XXXX"):
    st.error("⚠️ OPENAI_API_KEY não configurada no arquivo .env")
    st.info("Configure a chave no arquivo .env na raiz do projeto")
    st.stop()

# Obter o agente
agent, error = get_agent()

if error:
    st.error(f"❌ Erro ao criar agente: {error}")
    st.stop()

# Sidebar com informações
with st.sidebar:
    st.header("ℹ️ Informações")
    st.markdown("""
    **Como usar:**
    1. Digite sua pergunta no campo abaixo
    2. Clique em "Enviar" ou pressione Enter
    3. Aguarde a resposta do agente
    
    **Nota:** Esta interface faz chamadas diretas ao agente Agno,
    sem passar pelo backend FastAPI.
    """)
    
    st.divider()
    
    st.subheader("📊 Status")
    st.success("✅ Agente carregado")
    st.info(f"🔑 API Key: {api_key[:10]}...{api_key[-4:]}")

# Área principal de chat
st.subheader("💬 Chat com o Agente")

# Inicializar histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar histórico de mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada
if prompt := st.chat_input("Digite sua pergunta aqui..."):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Mostrar mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Mostrar mensagem do agente (com placeholder)
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                # Fazer chamada ao agente
                import asyncio
                response = asyncio.run(agent.arun(prompt))
                
                # Exibir resposta
                st.markdown(response.content)
                
                # Adicionar resposta ao histórico
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response.content
                })
            except Exception as e:
                error_msg = f"❌ Erro ao processar: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })

# Botão para limpar histórico
if st.session_state.messages:
    st.divider()
    if st.button("🗑️ Limpar Histórico"):
        st.session_state.messages = []
        st.rerun()
