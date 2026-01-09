# Agentes Agno

Este diretório contém os agentes Agno para o sistema de atendimento marketplace.

## Estrutura

- `marketplace_agent.py`: Agente principal para atendimento pré e pós-venda

## Como usar

O agente é inicializado através do `main.py` na raiz do backend:

```bash
cd backend
python -m app.main
```

Ou usando uvicorn diretamente:

```bash
cd backend
uvicorn app.main:app --reload
```

## Configuração

As configurações são carregadas do arquivo `.env` na raiz do projeto. Veja `.env.example` para as variáveis necessárias.
