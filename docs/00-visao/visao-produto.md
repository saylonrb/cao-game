# Visão do produto — Caô!

**Status:** visão inicial aprovada para orientar a engenharia de requisitos em 16/11/2026. Detalhes de regras e implementação ainda estão em aberto.

## Propósito e público

Oferecer a amigos uma partida online de cartas por turnos, acessível pelo navegador, com o clima imprevisível e divertido de jogos de descarte, mas com identidade visual e regras próprias.

## Experiência desejada

1. Uma pessoa cria uma sala privada e convida amigos por código ou link.
2. Os participantes entram no lobby, escolhem nome e avatar e veem seus totais de partidas e vitórias.
3. Com pelo menos dois jogadores presentes, somente o responsável atual pela sala pode iniciar a partida. Inicialmente ele é o criador; a sala aceita até dez pessoas no total, incluindo espectadores, sem exigir número de vagas definido na criação.
4. Cada pessoa começa com sete cartas. Durante a partida, joga ou compra cartas e aplica os efeitos do baralho que serão especificados.
5. Ao ficar com duas cartas, a pessoa deve anunciar sua última carta antes de jogar a penúltima. Se não anunciar, qualquer outra pessoa pode denunciá-la depois dessa jogada e antes da próxima jogada dela. Uma denúncia válida obriga a compra de uma carta.
6. Vence quem estiver sem cartas após a resolução dos efeitos pendentes. Os demais são classificados pela quantidade de cartas que restou em suas mãos.
7. No fim, o grupo pode encerrar ou iniciar outra partida. Uma nova partida depende do sinal de concordância de todos os futuros jogadores e da ação do responsável pela sala; a entrada ou saída de alguém reinicia a votação.

## Limites iniciais

- Primeira versão visual com um cenário e um conjunto pequeno de avatares, funcionando bem em computadores e celulares.
- Cadastro e login por apelido e senha reservam nomes e preservam totais entre visitas. A primeira versão não terá recuperação de senha.
- Guardar totais de partidas e vitórias; não há necessidade inicial de histórico detalhado de partidas.
- Salas privadas e participação remota em tempo real fazem parte da visão.
- Pessoas que entram durante uma partida podem assistir e pedir participação na próxima. O criador escolhe se espectadores poderão ver uma mão por vez; essa configuração é visível a todos antes da partida e pode mudar entre partidas. Se o criador não se reconectar em um minuto, o jogador conectado há mais tempo assume o controle da sala.
- O conjunto exato de cartas, efeitos, exceções e critérios de aceitação ainda será definido.
- O lançamento inicial é para grupos pequenos de amigos. Há um layout parcialmente pronto no Figma a consultar quando a interface for detalhada.

## Critério de sucesso inicial

Um grupo de amigos consegue criar uma sala, entrar, jogar uma partida completa segundo regras acordadas, identificar o vencedor e começar outra partida mediante concordância do grupo.
