# Estado atual — Caô!

**Atualizado em:** 16/11/2026

**Etapa:** 6 — desenvolvimento incremental; plano aprovado e base local I0 em andamento.

## Marco concluído

Visão do produto, requisitos, stack, arquitetura e plano de execução aprovados. ADR-0001 aceito. API e interface iniciais criadas; não há contas, salas ou partidas. A base foi publicada no repositório público `saylonrb/cao-game`, com `main` e `staging` no mesmo commit inicial. O CI da interface passou; o job Python falhou antes de iniciar por referência inválida à action `setup-uv@v9`. Correção preparada em `fix/ci-setup-uv`.

## Trabalho atual

I0 criou a API FastAPI + Socket.IO com rota `/health`, interface React/Vite/TypeScript de apresentação, lockfiles, Compose para PostgreSQL, testes de verificação e workflow de CI. Dependências locais instaladas e verificações de código executadas; `docker compose config` passou, mas o banco não pôde ser iniciado porque o daemon Docker não estava disponível. O CI ainda não rodou no GitHub, pois não há repositório remoto. Render Free + Neon Free continuam apenas candidatos ao piloto.

## Decisões recentes

- Salas privadas por código ou link têm até dez pessoas no total. Só o responsável atual inicia; após um minuto de desconexão, a função passa ao jogador conectado há mais tempo.
- O jogo usa contas por apelido e senha, estatísticas persistentes e um baralho inicial de 108 cartas. As regras de cartas, denúncia, reconexão, espectadores, vitória e nova partida estão detalhadas em [requisitos.md](../01-requisitos/requisitos.md).
- A primeira versão funciona em celular e computador, com um cenário e poucos avatares. O lançamento é para grupos pequenos de amigos; há um layout parcialmente pronto no Figma ainda não consultado.
- A validação inicial inclui telas de cerca de 360 px e 1280 px e três salas simultâneas de dez pessoas. Recuperação de senha e expulsão ficam para depois da primeira versão.
- O responsável conhece mais Python e Java e prefere custo inicial de R$ 0 enquanto possível. Java e TypeScript no servidor foram comparados; a preferência provisória por Python aproveita sua familiaridade.
- O responsável aprovou Python e a stack recomendada. A decisão e seus limites constam em [DECISOES.md](DECISOES.md).
- O responsável aprovou a etapa 4, o ADR-0001 e o plano da etapa 5.
- O responsável aprovou o plano da etapa 5 e pediu testes unitários das funcionalidades e CI/CD. O workflow verifica código e testes em PRs e guarda o build da interface em `main`; deploy exige decisão posterior.

## Próxima tarefa

Publicar e validar a correção do CI por PR para `staging`; o responsável autorizou commits, push de branches e abertura de PRs neste repositório em 16/11/2026. Concluir I0 verificando PostgreSQL quando o daemon Docker estiver disponível; depois iniciar I1 (contas e lobby) com testes unitários e de integração. Antes de qualquer piloto remoto, validar reinícios, reconexão, cotas, backup e segurança.

## Referências

- [Visão do produto](../00-visao/visao-produto.md)
- [Pendências](PENDENCIAS.md)
- [Especificação de requisitos](../01-requisitos/requisitos.md)
- [Pesquisa de viabilidade técnica](../04-pesquisas/viabilidade-tecnica.md)
- [Decisões aprovadas](DECISOES.md)
- [Arquitetura aprovada](../02-arquitetura/visao-arquitetural.md)
- [Roadmap proposto](../03-planejamento/roadmap.md)
- [Backlog inicial](../03-planejamento/backlog.md)
