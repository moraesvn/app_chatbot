# Frontend Streamlit - Interface de Teste

Interface Streamlit para testar o agente de atendimento marketplace durante o desenvolvimento.

## Características

- ✅ **Totalmente isolado do backend** - Faz chamadas diretas ao agente Agno
- ✅ **Interface simples e intuitiva** - Chat estilo conversacional
- ✅ **Histórico de conversas** - Mantém o contexto da conversa
- ✅ **Feedback visual** - Mostra status e erros claramente

## Como usar

1. Certifique-se de que o arquivo `.env` está configurado na raiz do projeto
2. Execute o Streamlit:

```bash
streamlit run frontend/app.py
```

3. A interface abrirá automaticamente no navegador (geralmente em `http://localhost:8501`)

## Estrutura

```
frontend/
└── app.py          # Interface principal Streamlit
```

## Notas

- Esta interface é apenas para **desenvolvimento e testes**
- Não passa pelo backend FastAPI - faz chamadas diretas ao agente
- O agente é cacheado pelo Streamlit para melhor performance
- O histórico de conversas é mantido na sessão do Streamlit
