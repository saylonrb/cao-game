# Estado atual — Caô!

**Atualizado em:** 16/11/2026

**Etapa:** 6 — desenvolvimento incremental; plano aprovado e base local I0 em andamento.

## Marco concluído

Visão do produto, requisitos, stack, arquitetura e plano de execução aprovados. ADR-0001 aceito. API e interface iniciais criadas; não há contas, salas ou partidas. A base foi publicada no repositório público `saylonrb/cao-game`, com `main` e `staging`. O primeiro CI revelou uma referência inválida à action `setup-uv`; a correção foi integrada por PRs #1 e #2. Os jobs Python e TypeScript passaram no CI final de `main`.

## Trabalho atual

I0 criou a API FastAPI + Socket.IO com rota `/health`, interface React/Vite/TypeScript de apresentação, lockfiles, Compose para PostgreSQL, testes de verificação e workflow de CI. Dependências locais instaladas e verificações de código executadas; `docker compose config` passou, mas o banco não pôde ser iniciado porque o daemon Docker não estava disponível. O CI executou no GitHub e passou após a correção. Render Free + Neon Free continuam apenas candidatos ao piloto.

## Decisões recentes

- Salas privadas por código ou link têm até dez pessoas no total. Só o responsável atual inicia; após um minuto de desconexão, a função passa ao jogador conectado há mais tempo.
- O jogo usa contas por apelido e senha, estatísticas persistentes e um baralho inicial de 108 cartas. As regras de cartas, denúncia, reconexão, espectadores, vitória e nova partida estão detalhadas em [requisitos.md](../01-requisitos/requisitos.md).
- A primeira versão funciona em celular e computador, com um cenário e poucos avatares. O lançamento é para grupos pequenos de amigos; há um layout parcialmente pronto no Figma ainda não consultado.
- A validação inicial inclui telas de cerca de 360 px e 1280 px e três salas simultâneas de dez pessoas. Recuperação de senha e expulsão ficam para depois da primeira versão.
- O responsável conhece mais Python e Java e prefere custo inicial de R$ 0 enquanto possível. A stack aprovada consta em [DECISOES.md](DECISOES.md).
- O responsável aprovou a etapa 4, o ADR-0001 e o plano da etapa 5.
- O responsável aprovou o plano da etapa 5 e pediu testes unitários das funcionalidades e CI/CD. O workflow verifica código e testes em PRs e guarda o build da interface em `main`; deploy exige decisão posterior.

## Próxima tarefa

Concluir I0 verificando PostgreSQL quando o daemon Docker estiver disponível; depois iniciar I1 (contas e lobby) com testes unitários e de integração. O responsável autorizou commits, push de branches e abertura de PRs neste repositório em 16/11/2026. Antes de qualquer piloto remoto, validar reinícios, reconexão, cotas, backup e segurança.

## Referências

- [Visão do produto](../00-visao/visao-produto.md)
- [Pendências](PENDENCIAS.md)
- [Especificação de requisitos](../01-requisitos/requisitos.md)
- [Pesquisa de viabilidade técnica](../04-pesquisas/viabilidade-tecnica.md)
- [Decisões aprovadas](DECISOES.md)
- [Arquitetura aprovada](../02-arquitetura/visao-arquitetural.md)
- [Roadmap aprovado](../03-planejamento/roadmap.md)
- [Backlog inicial](../03-planejamento/backlog.md)
