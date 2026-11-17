# Decisões aprovadas — Caô!

## D-001 — Stack da primeira versão

**Data:** 16/11/2026

**Status:** aprovada pelo responsável pelo produto.

**Contexto:** jogo privado em navegador, até dez pessoas por sala, desenvolvimento com orçamento inicial de R$ 0 e responsável com maior familiaridade em Python e Java.

**Alternativas estudadas:** Python + FastAPI + python-socketio; Java + Spring WebSocket/STOMP; TypeScript + Fastify/Socket.IO; Colyseus. Interface com React + Vite + TypeScript, SvelteKit ou Next.js. Persistência com PostgreSQL ou SQLite. Comparação e fontes em [viabilidade-tecnica.md](../04-pesquisas/viabilidade-tecnica.md).

**Decisão:** React + Vite + TypeScript para a interface; Python + FastAPI + python-socketio para o servidor; PostgreSQL para dados persistentes.

**Motivo:** Python aproveita a experiência do responsável e oferece um caminho documentado para HTTP e comunicação em tempo real. TypeScript ajuda a manter os modelos da interface claros. PostgreSQL oferece transações para contas, estatísticas e estado persistente.

**Consequências:** validar mensagens de rede em execução, manter contratos entre Python e TypeScript, testar reconexão e persistência de partidas. A escolha de provedor e plano de hospedagem continua aberta; Render Free + Neon Free é candidato, não serviço aprovado. A arquitetura ainda definirá bibliotecas auxiliares e a forma concreta de recuperação.
