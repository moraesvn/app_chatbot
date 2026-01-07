# Agente de IA - Atendimento Marketplace

Sistema de atendimento pré e pós-venda para marketplace utilizando agente de IA com RAG (Retrieval-Augmented Generation).

## 🎯 Objetivo

1. Colaborador cola a pergunta do cliente do marketplace na interface web
2. Agente IA treinado com dados da empresa consulta informações e gera resposta
3. Resposta é exibida na interface para revisão
4. Colaborador copia e cola a resposta no marketplace

## 🏗️ Arquitetura

### Backend
- **FastAPI** - API REST
- **Agno** - Framework para agentes de IA com RAG
- **PostgreSQL + pgvector** - Banco de dados com suporte a busca vetorial
- **OpenAI** - LLM e embeddings

### Frontend
- **Streamlit** - Interface web (a implementar)

## 📁 Estrutura do Projeto

```
app_chatbot/
├── backend/
│   └── app/
│       ├── agents/      # Agentes Agno
│       ├── api/         # Rotas FastAPI
│       ├── models/      # Modelos SQLAlchemy
│       ├── schemas/     # Schemas Pydantic
│       ├── services/    # Lógica de negócio
│       └── database/    # Configuração do banco
├── data/
│   └── knowledge_base/  # Base de conhecimento
└── frontend/            # Streamlit (a implementar)
```

## 🚀 Como Começar

### Pré-requisitos
- Python 3.12+
- Docker e Docker Compose
- Conta OpenAI com API key

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/moraesvn/app_chatbot.git
cd app_chatbot
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o .env com suas credenciais
```

5. Inicie o PostgreSQL com Docker:
```bash
docker-compose up -d
```

## 📝 Status do Projeto

- [x] Estrutura de pastas
- [x] Configuração inicial (requirements.txt, docker-compose.yml)
- [ ] Configuração do banco de dados
- [ ] Integração com Agno
- [ ] Implementação do RAG
- [ ] API FastAPI
- [ ] Interface Streamlit

## 🔧 Desenvolvimento

Este projeto segue desenvolvimento incremental por etapas pequenas.

## 📄 Licença

[Definir licença]

