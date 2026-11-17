# Backlog inicial — Caô!

**Status:** aprovado pelo responsável pelo produto em 16/11/2026. Ordem, marcos e gates estão no [roadmap](roadmap.md). Itens são resultados verificáveis, não uma lista fechada de arquivos ou bibliotecas.

| Prioridade | Item | Dependência | Critério objetivo |
| --- | --- | --- | --- |
| P0 | Ambiente local e migrações reproduzíveis | — | Frontend, backend e PostgreSQL iniciam sem credenciais versionadas; migração inicial aplica e reverte em banco de teste. |
| P0 | Cadastro, login, sessão e perfil | Ambiente | Apelido único, senha protegida, logout e totais consultáveis; sessão ausente/inválida é recusada. |
| P0 | Criar/entrar/sair de sala e configurar lobby | Contas | Convite funciona, 10 pessoas é limite total, responsável inicia com 2+ jogadores, sala encerra segundo RF-23. |
| P0 | Motor puro: baralho, turnos e compra comum | Ambiente | Baralho de 108, primeira carta numérica, sorteio de primeiro turno e compra RF-04 reproduzíveis nos testes. |
| P0 | Motor puro: efeitos, pilhas e cor | Motor básico | Casos `+2`/`+4`, opção `+2` sobre `+4`, bloqueio e inversão com dois jogadores passam. |
| P0 | Motor puro: anúncio, denúncia e conclusão | Efeitos | Primeira denúncia válida aplica uma carta; pilha termina antes do vencedor; ranking por cartas com empate. |
| P0 | Integrar comandos, persistência e projeções | Lobby + motor | Ação confirmada após commit; duplicação não reaplica; jogador recebe só a própria mão. |
| P0 | Mesa jogável em celular e computador | Integração | Dois jogadores concluem partida local; controles essenciais acessíveis em 360 px e 1280 px. |
| P0 | Reconexão, saída e sucessão | Integração | Antes/depois de 60 s preserva ou devolve mão corretamente; reinício não reinicia prazo; sala mantém responsável válido. |
| P0 | Espectadores e votação de nova partida | Integração + reconexão | Espectador seleciona no máximo uma mão autorizada; entrada/saída zera votos; só responsável inicia com unanimidade. |
| P0 | Totais, resultado e fluxo completo | Partida integrada | Uma conclusão normal soma partidas/vitória uma vez; encerramento sem vencedor não soma; ranking e nova partida visíveis. |
| P0 | Segurança e recuperação do piloto | Fluxo completo | Testes de acesso às mãos e sessões, reinício antes/depois do commit e restauração de backup passam. |
| P1 | Ajuste visual com Figma e acessibilidade | Mesa funcional | Layout final validado em toque/teclado e com sinais além da cor. |
| P1 | Medição e decisão de hospedagem | Fluxo completo | Três salas de dez com CPU, RAM, latência e cotas registrados; provedor e custo aprovados antes de publicar. |

**Prioridade:** P0 é indispensável à primeira versão local ou à segurança do piloto; P1 melhora a apresentação e fundamenta a publicação. O ajuste visual é necessário antes de convidar amigos, embora possa avançar junto dos últimos itens P0. Recuperação de senha, expulsão, histórico detalhado e novos cenários ficam fora da primeira versão, conforme os requisitos.

Cada item só é marcado concluído com critério demonstrado e referência aos testes ou à verificação manual realizada. Quando uma regra descoberta na implementação alterar requisitos, voltar à revisão do produto antes de codificá-la como regra definitiva.
