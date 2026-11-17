# Caô!

Caô! é um projeto de jogo de cartas original para partidas privadas entre amigos no navegador. O projeto também serve como prática de Engenharia de Software, com descoberta de produto, requisitos verificáveis, decisões fundamentadas e desenvolvimento incremental.

**Situação:** Etapa 6 — base local em desenvolvimento. Ainda não há contas, salas ou partidas implementadas.

## Processo

1. Descoberta e visão do produto.
2. Engenharia de requisitos.
3. Viabilidade e pesquisa tecnológica.
4. Projeto e arquitetura.
5. Planejamento dos incrementos.
6. Desenvolvimento e testes.
7. Implantação, operação e evolução.

A passagem entre etapas depende de revisão e aprovação do responsável pelo produto. Publicação e outras ações externas exigem autorização específica.

## Ponto de retomada

- [Visão do produto](docs/00-visao/visao-produto.md)
- [Estado atual](docs/memoria/ESTADO_ATUAL.md)
- [Pendências](docs/memoria/PENDENCIAS.md)
- [Requisitos aprovados](docs/01-requisitos/requisitos.md)
- [Pesquisa de viabilidade técnica](docs/04-pesquisas/viabilidade-tecnica.md)
- [Decisões aprovadas](docs/memoria/DECISOES.md)
- [Arquitetura aprovada](docs/02-arquitetura/visao-arquitetural.md)
- [Roadmap proposto](docs/03-planejamento/roadmap.md)
- [Backlog inicial](docs/03-planejamento/backlog.md)

## Executar a base local

Pré-requisitos: Python 3.13 ou superior, [uv](https://docs.astral.sh/uv/), Node.js 24, npm e Docker com Compose. O banco ainda não é acessado pela API; o arquivo Compose prepara o PostgreSQL para o próximo incremento. Nesta sessão o daemon Docker não estava disponível, então a inicialização do banco continua sem verificação prática.

1. `docker compose up -d postgres`
2. Em `backend/`: `uv sync` e `uv run uvicorn cao_backend.app:app --reload --host 127.0.0.1 --port 8000`
3. Em `frontend/`: `npm ci` e `npm run dev`

A interface fica em `http://127.0.0.1:5173`. A rota de saúde da API fica em `http://127.0.0.1:8000/health`.

Verificações: em `backend/`, `uv run ruff check .` e `uv run pytest`; em `frontend/`, `npm run lint`, `npm test` e `npm run build`. O [workflow de CI](.github/workflows/ci.yml) repete essas verificações em PRs para `staging` e `main`. Um push em `main` guarda o build da interface como artefato; nenhum deploy está configurado.

Documentos adicionais serão criados quando houver conteúdo real a registrar.
