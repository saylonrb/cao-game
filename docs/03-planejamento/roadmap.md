# Plano de execução — Caô!

**Data:** 16/11/2026

**Status:** aprovado pelo responsável pelo produto em 16/11/2026; I0 em andamento.

**Base:** [requisitos](../01-requisitos/requisitos.md), [arquitetura aprovada](../02-arquitetura/visao-arquitetural.md), [ADR-0001](../02-arquitetura/adr/0001-estado-autoritativo.md).

## O que será a primeira versão

A primeira versão está pronta quando um grupo de amigos consegue criar contas, formar uma sala privada, jogar uma partida com **todas as regras aprovadas**, ver vencedor/ranking/estatísticas e iniciar outra partida por votação; reconexão e espectadores funcionam sem expor cartas. O primeiro protótipo jogável será uma **entrega interna**, ainda incompleta para convidar amigos. O piloto remoto só será considerado após as provas de segurança, recuperação, uso de recursos e experiência móvel.

## Sequência de incrementos

| Ordem | Entrega observável | Requisitos principais | Prova de conclusão |
| --- | --- | --- | --- |
| **I0 — Base local** | Aplicações frontend/backend iniciam localmente; PostgreSQL local, configuração segura, migrações e verificações automáticas mínimas. | RNF-03 | Ambiente reproduzível sem segredo no repositório; um comando de verificação por parte do projeto; nenhuma conta externa necessária. |
| **I1 — Contas e lobby** | Cadastro/login por apelido e senha; perfil e totais; criar/entrar em sala por código/link; nomes, avatares, vagas e configurações visíveis. | RF-01 a RF-03, RF-11, RF-13, RF-15, RF-17, RF-23 | Duas contas entram na mesma sala; 11ª pessoa é recusada; sessão inválida não acessa sala; totais persistem. |
| **I2 — Motor de regras** | Motor isolado da rede com baralho de 108 cartas, início, turnos, compra comum, cartas especiais, pilhas, anúncio/denúncia, vitória e ranking. | RF-04 a RF-07, RF-12, RF-14, RF-19 a RF-22, RF-24, RF-25 | Testes de mesa cobrem os oito cenários prioritários aplicáveis; mesma entrada e sorteio controlado produzem mesmo resultado. |
| **I3 — Primeira partida integrada** | Lobby inicia partida; mesa mostra mãos autorizadas; jogadores jogam, compram, anunciam/denunciam e recebem resultado em tempo real; estado é salvo a cada ação. | RF-02, RF-04 a RF-07, RF-12, RF-19 a RF-25; RNF-03 | Duas pessoas concluem partida local com regras completas; comandos duplicados não repetem efeitos; mão alheia não aparece no tráfego. Este é o primeiro protótipo jogável interno. |
| **I4 — Continuidade e grupo** | Reconexão de um minuto, saída, sucessão do responsável, entrada de espectadores, visibilidade opcional, pedido e votação para nova partida. | RF-08, RF-09, RF-15, RF-16, RF-18, RF-23, RF-25 | Retorno antes/depois do prazo gera papéis corretos; reinício antes/depois do commit preserva partida; mudança do grupo zera votos; três salas não se misturam. |
| **I5 — Fechamento da primeira versão** | Resultado e totais transacionais; telas responsivas; acessibilidade de cores; fluxo completo revisado com layout do Figma; mensagens de falha e nova partida. | RF-03, RF-07, RF-09, RF-10, RF-13; RNF-01 a RNF-04 | Fluxos completos em 360 px e 1280 px; ranking e totais corretos após recarregar; testes de regras, integração e segurança prioritários passam. |
| **I6 — Preparação do piloto remoto** | Medição com três salas de dez; decisão de hospedagem, backup/restore, logs seguros e procedimento de implantação/reversão. | RNF-02, RNF-03 | Cotas e desempenho medidos; recuperação do banco comprovada; custo revisado; publicação somente após autorização específica. |

**Dependências:** I0 sustenta I1 e I2; I3 precisa de I1 e I2; I4 e I5 completam o fluxo de I3; I6 depende da primeira versão local validada. Dentro de cada incremento, preferir pequenas tarefas verticais verificáveis, sem criar um grande bloco de código para só testar ao fim. A ordem de I1 e I2 pode ser parcialmente alternada sem mudar o marco de I3.

## Marcos e gates

1. **M1 — Base reproduzível:** I0 concluído; autorização separada para instalar dependências e iniciar o repositório Git local, conforme as orientações do projeto.
2. **M2 — Protótipo local jogável:** I1–I3 concluídos; apenas uso interno, com regras completas no caminho principal.
3. **M3 — Primeira versão local:** I4–I5 concluídos; critérios de RF/RNF verificados, inclusive quedas e privacidade.
4. **M4 — Piloto entre amigos:** I6 concluído; provedor, custo e publicação aprovados separadamente. O plano gratuito pode impor pausas e limites; não prometer disponibilidade contínua antes de medir.

Cada incremento segue: objetivo e critérios → alteração pequena → verificação proporcional ao risco → revisão → memória atualizada. Uma falha em regra, privacidade ou recuperação impede marcar o incremento correspondente como concluído. Metas numéricas de latência e suporte exato de navegadores serão fixados após medição e teste de interface, conforme a arquitetura aprovada.

## Fluxo de Git proposto

- **`main`** representa a versão estável aprovada. **`staging`** reúne entregas para integração e teste antes da promoção a `main`.
- Mudanças partem de `staging` em branches curtas `feat/<assunto>`, `fix/<assunto>`, `docs/<assunto>` ou `chore/<assunto>`, com nomes em minúsculas e palavras separadas por hífen. Ex.: `feat/salas-privadas`.
- Cada mudança entra por PR para `staging`, com descrição do que mudou, requisito atendido e verificações feitas. Após um marco testado, um PR de `staging` para `main` registra a promoção. Correção urgente em `main` usa `hotfix/<assunto>` e depois é incorporada a `staging`.
- Commits seguem convenção simples: `feat: ...`, `fix: ...`, `test: ...`, `docs: ...`, `refactor: ...`, `chore: ...` ou `ci: ...`, em português claro. O tipo descreve a mudança; evitar commits grandes ou mensagens como “ajustes”.
- PRs devem passar por revisão e verificações automáticas relevantes antes do merge. GitHub será configurado quando houver autorização para criar o repositório; não há commits, branches ou PRs criados nesta etapa.

## O que irá para o GitHub

Quando o repositório for autorizado, publicar código fonte, testes, migrações, arquivos de dependências travadas, configuração de exemplo sem credenciais, `README.md`, `AGENTS.md` e documentação que explica decisões e retomada do projeto, incluindo requisitos, arquitetura, plano e pesquisa técnica relevante. `AGENTS.md` é útil porque orienta futuras sessões e colaboradores; não deve conter segredos ou detalhes particulares da máquina.

Excluir `.env`, senhas, chaves, banco local, logs, caches, ambientes virtuais, builds gerados e rascunhos ou pesquisas brutas sem valor de decisão. Manter documentos existentes enquanto ajudam a reconstruir decisões; evitar arquivos vazios ou documentação repetida. O layout do Figma pode ser referenciado, mas sua publicação ou cópia dependerá do acesso e da permissão correspondente.

## Riscos e decisões reservadas

- Escolha final de provedor, backup, metas de latência e navegadores suportados após medições; sem contratação agora.
- Acesso ao layout do Figma quando I5 for desenhado, para verificar responsividade e identidade visual.
- Critérios de sessão, inatividade da sala e detalhes de migração serão fechados no incremento que os implementar, sem modificar regras de negócio silenciosamente.
- Se o teste mostrar que instantâneo por ação é pesado ou que o plano gratuito prejudica a reconexão, revisar ADR-0001 e a hospedagem antes do piloto.

**Critério para encerrar a etapa 5:** o responsável pelo produto aprova alcance da primeira versão, ordem de incrementos, marcos e fluxo de Git. A etapa 6 e instalações locais começam somente depois desse gate e das autorizações específicas aplicáveis.
