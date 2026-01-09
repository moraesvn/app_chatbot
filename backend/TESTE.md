# Como Testar o Agente

## Passo 1: Configurar variáveis de ambiente

1. Crie um arquivo `.env` na raiz do projeto (`c:\app_chatbot\.env`)
2. Adicione sua chave da OpenAI:

```
OPENAI_API_KEY=sua_chave_aqui
```

## Passo 2: Testar o agente via script

Execute o script de teste:

```bash
cd backend
python test_agent.py
```

Este script faz uma chamada simples à API OpenAI através do agente Agno.

## Passo 3: Testar via API (AgentOS)

Inicie o servidor AgentOS:

```bash
cd backend
python -m app.main
```

Ou usando uvicorn:

```bash
cd backend
uvicorn app.main:app --reload
```

O servidor estará disponível em `http://localhost:8000`

Você pode usar a interface do AgentOS UI ou fazer chamadas HTTP diretamente.

## Próximos passos

Após confirmar que o agente está funcionando, vamos adicionar:
- Banco de dados PostgreSQL
- RAG (busca vetorial)
