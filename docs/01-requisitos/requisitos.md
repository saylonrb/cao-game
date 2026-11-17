# Requisitos da primeira versão — Caô!

**Etapa:** 2 — engenharia de requisitos

**Atualizado em:** 16/11/2026

**Status:** Etapa 2 aprovada pelo responsável pelo produto em 16/11/2026. Nenhuma tecnologia ou arquitetura foi selecionada.

Este documento distingue decisões confirmadas na descoberta, propostas de detalhamento e questões abertas. IDs permitem relacionar critérios, implementação e testes futuros.

## Requisitos confirmados

| ID | Requisito | Critério de aceitação inicial |
| --- | --- | --- |
| RF-01 | Uma pessoa pode criar uma sala privada e compartilhar código ou link de convite. | Amigos entram diretamente como jogadores pelo código ou link enquanto a sala está no lobby e há vaga; a sala comporta no máximo dez pessoas no total, somando jogadores e espectadores, sem lotação definida na criação. Se estiver cheia, a entrada é recusada com mensagem clara até surgir vaga. |
| RF-02 | Apenas o responsável atual pela sala inicia uma partida. Inicialmente, ele é o criador; a função pode ser transferida após desconexão. | Uma tentativa de início por outro participante é rejeitada; o responsável consegue iniciar com ao menos dois jogadores. |
| RF-03 | Participantes podem escolher nome e avatar no lobby. | O nome e o avatar escolhidos são visíveis aos demais na sala. |
| RF-04 | Cada jogador inicia com sete cartas. No turno normal, só pode comprar se não tiver carta jogável e compra no máximo uma vez. Se a carta comprada for jogável, pode jogá-la imediatamente; caso contrário, a vez passa. | A distribuição e cada ação válida alteram o estado da partida de forma consistente para os participantes; tentativas de compra com jogada disponível ou de segunda compra no mesmo turno são rejeitadas. |
| RF-05 | O baralho inclui cartas numéricas, bloqueio, inversão, compra de duas, escolha de cor e compra de quatro. | Os efeitos de cada tipo serão especificados e verificados em cenários próprios. |
| RF-06 | Ao ficar com duas cartas, o jogador deve anunciar a última carta antes de jogar a penúltima. | O jogo confirma que o anúncio foi registrado antes de permitir a jogada. Se não anunciar antes da jogada, não pode corrigir depois. A primeira denúncia válida de outro jogador, após essa jogada e antes da próxima jogada dele, aplica compra de uma carta uma única vez. Espectadores não podem denunciar. |
| RF-07 | Uma pessoa vence ao ficar sem cartas depois da resolução de todos os efeitos pendentes. | Se a última carta gerar uma pilha de compra, os jogadores podem responder e a pilha é resolvida antes do resultado. Entre as pessoas que continuarem com a mão vazia, vence a que zerou a mão primeiro. Se a penalidade voltar a ela e precisar comprar, outra pessoa com a mão vazia pode vencer. Os demais são classificados pela quantidade restante; quantidades iguais compartilham a mesma posição. |
| RF-08 | Quem não participa da partida em andamento pode assistir e solicitar participação na próxima. | A pessoa que entra durante a partida ocupa uma das dez vagas totais como espectadora, sem receber cartas nem realizar jogadas; pode pedir para integrar a próxima partida. |
| RF-09 | Uma nova partida requer concordância dos participantes que vão jogar e ação do responsável pela sala. | O responsável só consegue iniciar depois de todos os futuros jogadores sinalizarem concordância; há entre 2 e 10 jogadores. A entrada ou saída de alguém durante a votação reinicia os sinais. Sem resposta, a votação fica aguardando, sem início automático; o responsável pode cancelá-la. |
| RF-10 | Totais de partidas concluídas e vitórias persistem entre visitas e aparecem no lobby. | Após sair e entrar novamente, o jogador vê os mesmos totais; quem sai antes do resultado não recebe partida jogada. Partida encerrada sem vencedor não altera totais de ninguém. |

## Regras detalhadas

- **RF-11 — Conta (confirmado):** cadastro e login por apelido único e senha, para reservar o apelido e associar estatísticas ao mesmo jogador. Recuperação de senha fica para versão posterior; a perda de acesso nesta versão está registrada em RF-17.
- **RF-12 — Empilhamento (confirmado):** permitir `+2` sobre `+2`, `+4` sobre `+2` e `+4` sobre `+4`. Uma opção escolhida pelo criador no lobby também permite `+2` sobre `+4`. A opção fica fixa durante a partida. Cada carta adiciona seu valor à penalidade; quem não jogar uma carta de compra permitida pela configuração compra o total acumulado e perde a vez. Durante a pilha, a cor não limita as respostas; depois, vale a cor da última carta jogada ou a cor escolhida pelo jogador que lançou o último `+4`. Se a pilha começou com a última carta de um jogador, ela é resolvida antes do resultado da partida.
- **RF-13 — Visual inicial:** um cenário e um conjunto pequeno de avatares, com expansão posterior.
- **RF-14 — Uso do `+4` (confirmado):** a carta pode ser jogada em qualquer turno do seu dono, mesmo que ele tenha outra carta jogável; não há restrição baseada na cor anterior nem desafio por uso indevido.
- **RF-15 — Visibilidade para espectadores (confirmado):** o criador escolhe, na criação da sala, se espectadores podem ver as cartas dos jogadores. A configuração é exibida a todos antes da partida. Se estiver ativa, o espectador pode escolher uma mão por vez para ver; se estiver inativa, vê apenas as quantidades de cartas. O criador pode mudar a configuração entre partidas.
- **RF-16 — Sucessão do criador (confirmado):** após a desconexão do responsável pela sala, há um minuto para reconexão. Se ele não voltar, o controle passa ao jogador conectado há mais tempo. Se voltar depois, assiste à partida atual como espectador e pode participar da seguinte como jogador comum. Reconexão e destino das cartas seguem RF-18.
- **RF-17 — Conta sem recuperação na primeira versão (confirmado):** quem perder a senha não recupera a conta nesta versão e precisará criar outra com apelido diferente; os totais anteriores continuam associados à conta inacessível.
- **RF-18 — Reconexão e saída (confirmado):** qualquer jogador desconectado tem um minuto para voltar e retomar a mesma mão e posição. Se for sua vez, a partida aguarda esse prazo. Se o prazo expirar, ele sai da partida e poderá retornar como espectador. A saída voluntária ocorre imediatamente. Em ambos os casos, suas cartas retornam ao monte de compra sem serem reveladas e são embaralhadas. Se as saídas deixarem apenas um jogador ativo, a partida termina sem vencedor.
- **RF-19 — Correspondência e efeitos básicos (confirmado):** no turno comum, uma carta combina por cor, número ou símbolo. Cartas de escolha de cor e `+4` independem da carta da mesa. Bloqueio pula o próximo jogador; inversão muda o sentido. Com dois jogadores, a inversão dá outra vez a quem a jogou.
- **RF-20 — Início e reposição do monte (confirmado):** a primeira carta virada na mesa deve ser numérica; cartas de efeito sorteadas nesse momento retornam ao baralho e uma nova carta é sorteada. Se o monte de compra acabar, as cartas já jogadas são embaralhadas para formar outro monte, preservando a carta mais recente na mesa.
- **RF-21 — Primeiro turno (confirmado):** o primeiro jogador é sorteado em cada partida.
- **RF-22 — Disponibilidade de compra (confirmado):** toda compra exigida deve ser cumprida integralmente. Primeiro, reembaralham-se os descartes disponíveis, preservando a carta da mesa. Se ainda faltarem cartas, acrescenta-se e embaralha-se um novo conjunto de cartas até haver quantidade suficiente.
- **RF-23 — Encerramento da sala (confirmado):** quando a última pessoa sai ou quando só restam espectadores, a sala é encerrada e seus ocupantes são informados. O código e o link deixam de permitir entrada. A troca de responsável não altera código ou link. Expulsão de participantes fica fora da primeira versão.
- **RF-24 — Baralho inicial (confirmado):** 108 cartas: para cada uma das quatro cores, um `0`, duas cópias de cada número de `1` a `9`, duas de bloqueio, duas de inversão e duas de `+2`; mais quatro cartas de escolha de cor e quatro `+4`. Novos conjuntos acrescentados em RF-22 usam essa composição.
- **RF-25 — Ações concorrentes (confirmado):** o jogo avalia as ações recebidas em uma ordem única, aceita apenas a primeira denúncia válida para cada falta e impede que ações repetidas apliquem efeitos extras. O jogador recebe confirmação de que seu anúncio foi registrado antes de poder jogar a penúltima carta.

## Requisitos de qualidade

| ID | Necessidade | Verificação proposta |
| --- | --- | --- |
| RNF-01 | A primeira versão deve funcionar bem em computadores e celulares. | Verificar cadastro, lobby, partida e resultado em telas de aproximadamente 360 px e 1280 px de largura, sem controles essenciais inacessíveis ou rolagem horizontal inesperada. |
| RNF-02 | O lançamento inicial atende grupos pequenos de amigos. | Verificar três salas simultâneas com até dez pessoas cada, sem misturar ações ou cartas entre salas. Metas de tempo de resposta serão calibradas em teste controlado antes de produção. |
| RNF-03 | Contas, sessões e cartas ocultas devem ser protegidas. | Verificar armazenamento seguro de senhas, acesso autorizado às mãos, proteção de sessão e rejeição de ações inválidas. A tecnologia será definida depois da etapa de viabilidade. |
| RNF-04 | Cores devem ser distinguíveis sem depender apenas da cor visual. | Verificar símbolos ou rótulos nas cartas e controles, inclusive em telas pequenas. |

## Cenários de aceitação prioritários

1. **Sala e vagas:** dado um convite válido, uma pessoa entra diretamente no lobby enquanto há vaga; com dez pessoas presentes, outra tentativa recebe aviso de sala cheia e não cria o 11º ocupante.
2. **Compra comum:** dado um turno com carta jogável, a compra é rejeitada; sem carta jogável, compra-se uma carta, que pode ser jogada se servir. Se não servir, o turno passa.
3. **Pilha configurável:** com a opção padrão, `+2` responde a `+2` e `+4` responde a `+2` ou `+4`; com a opção adicional, `+2` também responde a `+4`. Quem não responde compra a soma inteira e perde a vez.
4. **Anúncio da última carta:** dado um jogador que não anunciou antes de jogar sua penúltima carta, a primeira denúncia válida feita por outro jogador antes da próxima jogada dele impõe uma compra de uma carta; denúncias posteriores não duplicam a penalidade.
5. **Resultado após pilha:** dado um jogador que zera a mão com `+2`, se outra pessoa responder e a pilha voltar ao primeiro, o resultado espera a resolução. Entre os que permanecerem sem cartas, vence quem esvaziou a mão primeiro; se o primeiro precisar comprar, vence o próximo que permaneceu com a mão vazia. Empate de quantidade entre os demais compartilha posição.
6. **Reconexão:** dado um jogador desconectado, retorno dentro de um minuto restaura a mesma mão e posição. Se o prazo expirar, suas cartas voltam ao monte sem exposição e ele pode voltar como espectador; se restar só um jogador ativo, a partida termina sem vencedor.
7. **Espectador e nova partida:** uma entrada durante a partida ocupa vaga de espectador. Se autorizado na configuração, pode escolher uma mão por vez para ver. Na partida seguinte, entra como jogador após pedir participação, haver vaga e concordar; mudança do grupo reinicia os joinhas.
8. **Conta e totais:** após concluir uma partida com vencedor, os jogadores que permaneceram até o resultado veem o total de partidas incrementado e o vencedor vê uma vitória adicional ao voltar ao lobby. Saídas antecipadas e partidas sem vencedor não alteram esses totais.

## Limites e detalhes posteriores

- Recuperação de conta, expulsão de participantes, histórico detalhado de partidas e ampliação de avatares ou cenários ficam fora da primeira versão.
- Nomes e aparência final das cartas, lista de avatares e cenário serão detalhados no projeto de interface com apoio do layout existente no Figma.
- Compatibilidade específica de navegadores, metas de latência, implantação e tecnologias serão pesquisadas nas etapas seguintes; RNF-01 a RNF-04 permanecem como necessidades do produto.

## Revisão de cobertura da Etapa 2

- **Fluxo principal coberto:** cadastro, sala, entrada, lobby, início, jogadas, compra, vitória, ranking e nova partida.
- **Regras principais:** os casos que alteram entrada na sala, vez, compra, vitória e estatísticas estão especificados; detalhes de interface e mensagens ficam para o projeto.
- **Qualidade:** alvos de tela e concorrência estão registrados; navegadores e metas de latência serão definidos com evidência técnica antes do lançamento.
- **Critérios de conclusão da etapa:** requisitos prioritários sem ambiguidades que mudem o resultado do jogo, cenários de aceitação verificáveis, limites da primeira versão e pendências futuras explicitamente separados; revisão e aprovação pelo responsável pelo produto.

## Referências para comparação

Consultadas em 16/11/2026. São referências de pesquisa, **não** regras automaticamente adotadas pelo Caô!:

- [Instruções do UNO clássico, Mattel](https://service.mattel.com/instruction_sheets/UNO%20Basic%20IS.pdf): descrevem a compra e perda da vez após `+2` e `+4`, sem empilhamento na regra principal.
- [Instruções do UNO Show ’Em No Mercy, Mattel](https://service.mattel.com/instruction_sheets/HVW18-Eng.pdf): variante oficial com empilhamento de cartas de compra de valor igual ou maior.
