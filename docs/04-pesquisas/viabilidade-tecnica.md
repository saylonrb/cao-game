# Viabilidade técnica — Caô!

**Pesquisa:** 16/11/2026

**Status:** pesquisa concluída; stack aprovada em 16/11/2026. Hospedagem remota continua sem escolha ou contratação.

**Base:** [requisitos da primeira versão](../01-requisitos/requisitos.md).

## Problema e critérios

O Caô! precisa sincronizar partidas privadas de até dez pessoas, preservar cartas ocultas e contas entre visitas, aceitar reconexão em um minuto e funcionar em celular e computador. O lançamento inicial será para poucos grupos de amigos, com preferência por **R$ 0 enquanto possível**. O responsável pelo produto conhece mais Python e Java; TypeScript é uma oportunidade de aprendizado.

Critérios de comparação: aderência às regras e ao tempo real; proteção de mãos e contas; capacidade de recuperar uma partida após queda do processo; custo inicial e risco de ultrapassar cotas; esforço de aprendizado; facilidade de teste, implantação e manutenção. Um plano gratuito serve para um piloto apenas se suas limitações forem aceitas explicitamente.

## Conceito: HTTP e comunicação em tempo real

**HTTP** atende bem ações pontuais, como cadastro, login e consulta de estatísticas: o navegador faz uma requisição e recebe uma resposta. **WebSocket** mantém uma conexão bidirecional pela qual cliente e servidor podem enviar mensagens sem que o navegador pergunte repetidamente se houve novidade. Uma partida pode usar HTTP para ações pontuais e comunicação persistente para jogadas, turnos e votos. A [MDN descreve o WebSocket como sessão bidirecional](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).

Socket.IO é uma camada de eventos que pode usar WebSocket e também outros transportes; oferece salas, confirmação de eventos e reconexão. Ele **não substitui as regras do jogo nem garante sozinho que uma partida sobreviva ao reinício do servidor**. As [garantias de entrega](https://socket.io/docs/v4/delivery-guarantees/) exigem cuidados adicionais para eventos perdidos. A versão Python precisa ser compatível com a versão JavaScript do cliente, conforme a [matriz oficial de compatibilidade](https://python-socketio.readthedocs.io/en/stable/intro.html).

## Interface

| Opção | Adequação ao Caô! | Custo e limite técnico |
| --- | --- | --- |
| **React + Vite + TypeScript** | Boa para uma interface de jogo interativa; Vite gera arquivos estáticos publicáveis; TypeScript descreve cartas e eventos no cliente. | Roteamento e gestão de estado precisam ser escolhidos quando necessários; haverá aprendizagem de TypeScript. |
| **SvelteKit** | Componentes e aplicação integrados em um framework; também permite renderização no cliente. | Introduz Svelte e SvelteKit ao mesmo tempo, sem vantagem clara para a primeira versão privada. |
| **Next.js** | Framework React completo, com renderização no servidor e outras opções de entrega. | Essas capacidades acrescentam conceitos e decisões de implantação que o lobby e a mesa privada não exigem agora. |

**Recomendação provisória:** React + Vite + TypeScript. A documentação oficial confirma o [modelo de componentes com TypeScript](https://react.dev/learn/typescript), o [modelo de tipos do TypeScript](https://www.typescriptlang.org/docs/handbook/intro) e o [modelo de projeto e build do Vite](https://vite.dev/guide/). [SvelteKit](https://svelte.dev/docs/kit/introduction) e [Next.js](https://nextjs.org/docs/app/getting-started/deploying) permanecem alternativas. A escolha deriva do predomínio de interação no navegador; não houve benchmark das três opções.

TypeScript é JavaScript com verificação estática de tipos durante o desenvolvimento; o navegador executa o JavaScript gerado. Os tipos ajudam a detectar erros no código, mas **mensagens recebidas pela rede ainda precisam de validação em execução no servidor**.

## Servidor e motor de regras

| Opção | Pontos fortes para este projeto | Trabalho adicional e trade-off |
| --- | --- | --- |
| **Python + FastAPI + python-socketio** | Aproveita a experiência do responsável pelo produto. FastAPI atende HTTP; python-socketio oferece eventos e salas e pode ser executado junto de uma aplicação FastAPI. | Contratos entre TypeScript e Python precisam ser validados dos dois lados. Regras, estado, reconexão e persistência da partida continuam sendo responsabilidade do Caô!. |
| **Java + Spring Boot + WebSocket/STOMP** | Usa Java conhecido pelo responsável; Spring oferece suporte oficial a mensagens WebSocket. | STOMP e Spring introduzem mais conceitos de configuração. Não oferece, por si, as regras e a recuperação de partida. Uso de recursos no plano gratuito precisaria ser medido. |
| **TypeScript + Fastify + Socket.IO** | Mesma linguagem na interface e no servidor, com possibilidade de compartilhar tipos; Fastify oferece validação por esquema. | Exige aprender TypeScript nos dois lados ao mesmo tempo; o motor de regras e a persistência seguem como trabalho do projeto. |
| **TypeScript + Colyseus** | Framework especializado em salas, sincronização e reconexão; inclui mecanismos para filtrar a visão por cliente. | Impõe convenções próprias de estado e sala; contas, regras específicas e recuperação após falha do processo ainda precisam de desenho. |

**Recomendação provisória:** Python + FastAPI + python-socketio para a primeira versão. O [FastAPI suporta WebSocket](https://fastapi.tiangolo.com/advanced/websockets/); o [python-socketio documenta salas e integração ASGI/FastAPI](https://python-socketio.readthedocs.io/en/stable/server.html). A alternativa Java é tecnicamente viável segundo o [guia WebSocket do Spring](https://spring.io/guides/gs/messaging-stomp-websocket/), e a alternativa TypeScript é sustentada pelos guias de [Fastify](https://fastify.dev/docs/latest/Reference/Validation-and-Serialization/) e [Socket.IO](https://socket.io/docs/v4/how-it-works). O [Colyseus documenta reconexão de salas](https://docs.colyseus.io/room/reconnection). A preferência por Python é uma **inferência de adequação ao aprendizado e ao escopo**, não uma afirmação de desempenho superior.

O motor de regras deve ser testável independentemente da interface e da conexão, qualquer que seja a linguagem escolhida. A separação concreta e os contratos serão definidos na etapa de arquitetura.

**Memória e processamento são critérios diferentes.** A [Render informa 512 MB de RAM no plano gratuito](https://render.com/docs/compute-plans) e [alerta que aplicações JVM em Docker podem precisar de mais memória](https://render.com/docs/troubleshooting-deploys). Isso indica risco de hospedagem para uma implementação Java específica, não uma regra de que Java sempre consome mais recursos que Python. Por outro lado, a [JVM HotSpot compila e otimiza código durante a execução](https://docs.oracle.com/en/java/javase/25/vm/java-hotspot-virtual-machine-performance-enhancements.html), dando a Java uma vantagem potencial em processamento contínuo. O Caô! ainda não tem medições: com até três salas de dez pessoas, a preferência por Python é uma hipótese de produtividade e adequação ao piloto, sujeita a testes de memória, CPU e latência.

## Persistência e autenticação

| Opção | Avaliação |
| --- | --- |
| **PostgreSQL** | Candidato principal para contas, sessões, estatísticas e registros ou instantâneos de partidas. Transações permitem atualizar dados relacionados como uma unidade. Exige um serviço de banco e plano de backup. |
| **SQLite** | Muito simples para desenvolvimento local ou um único processo com disco persistente. Seu modo WAL permite leituras simultâneas, mas só um escritor por vez; um serviço gratuito com disco efêmero perde o arquivo em reinícios. |
| **Redis ou armazenamento apenas em memória** | Útil como cache ou coordenação futura, mas insuficiente sozinho para contas e estatísticas persistentes. Introduzir Redis desde o início acrescentaria outro serviço. |

**Recomendação provisória:** PostgreSQL, sem Redis inicialmente. O [guia de transações do PostgreSQL](https://www.postgresql.org/docs/current/tutorial-transactions.html) e a [orientação de uso do SQLite](https://www.sqlite.org/whentouse.html) sustentam a comparação. Um instantâneo da partida após jogadas aceitas é hipótese a testar na arquitetura: o transporte de tempo real não garante recuperação após reinício.

Para apelido e senha sem e-mail, um serviço de autenticação gerenciado pode não encaixar diretamente: o [Supabase Auth usa e-mail ou telefone para senha](https://supabase.com/docs/guides/auth/passwords), e o [plugin de apelido do Better Auth estende o autenticador de e-mail e senha](https://better-auth.com/docs/plugins/username). A hipótese mais aderente é manter contas na aplicação, com biblioteca consolidada para hash de senhas e sessões revogáveis. A [documentação do FastAPI mostra `pwdlib` com Argon2](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/). A implementação deverá seguir a [orientação OWASP para senhas](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) e [sessões](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html): não armazenar senha em texto puro, proteger cookie de sessão e limitar tentativas de login. Isto não autoriza criar criptografia ou fluxo de autenticação próprios sem revisão.

## Hospedagem e custo

Valores e limites consultados em **16/11/2026**. Estão sujeitos a mudança; nenhum serviço foi criado.

| Caminho | Custo inicial informado | Adequação e risco |
| --- | --- | --- |
| **Desenvolvimento local** | Sem cobrança de provedor. | Melhor para aprender e verificar regras; amigos fora da rede local ainda não conseguem jogar normalmente. |
| **Render Free para servidor e site estático + Neon Free para PostgreSQL** | Planos gratuitos conforme documentação consultada. | Candidato a piloto remoto com Python. O serviço web gratuito do Render dorme após 15 minutos sem tráfego e pode levar cerca de um minuto para acordar; pode reiniciar e tem disco efêmero. Neon Free informa 1 GB e 100 CU-h por projeto ao mês. É preciso testar se a experiência e a reconexão de um minuto continuam aceitáveis. |
| **Cloudflare Workers Free + Durable Objects + D1** | Sem cobrança fixa dentro das cotas gratuitas. | Durable Objects permitem coordenar uma sala com WebSockets e hibernação; D1 guarda dados. Há suporte a Python, inclusive em Durable Objects, mas esta alternativa exige arquitetura própria da plataforma e prova de viabilidade das bibliotecas necessárias e da autenticação por senha sob o limite gratuito de CPU. Exceder cotas gratuitas faz operações falharem. |
| **Railway Hobby com servidor e PostgreSQL** | Mínimo de US$ 5/mês de uso informado; excedente cobrado por consumo. | Suporta WebSockets e banco na mesma plataforma; não atende à preferência de R$ 0. Banco, backup e custos de uso precisam ser configurados e acompanhados. Só considerar mediante autorização de despesa. |

Fontes: [Render Free](https://render.com/docs/free), [Render WebSockets](https://render.com/docs/websocket), [Neon preços](https://neon.com/pricing), [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects/platform/pricing/), [Cloudflare D1](https://developers.cloudflare.com/d1/platform/pricing/), [Cloudflare Workers limites](https://developers.cloudflare.com/workers/platform/limits/), [Cloudflare Python Workers](https://developers.cloudflare.com/workers/languages/python/), [Cloudflare Durable Objects em Python](https://developers.cloudflare.com/changelog/post/2025-05-14-python-worker-durable-object/), [Railway preços](https://railway.com/pricing), [Railway WebSockets](https://docs.railway.com/networking/public-networking/specs-and-limits) e [Railway PostgreSQL](https://docs.railway.com/databases/postgresql).

**Recomendação provisória para o piloto:** desenvolver localmente e, quando for autorizado um teste remoto, avaliar Render Free com Neon Free. Essa combinação preserva Python e o custo inicial zero, mas **não está validada para uma partida pública confiável**. Cloudflare merece um experimento curto se o despertar do servidor gratuito prejudicar as partidas; seu suporte a Python não significa que a mesma aplicação FastAPI + python-socketio possa ser transferida sem adaptações. Não há escolha de hospedagem para produção neste momento.

## Operação mínima para o piloto

Antes de convidar amigos, definir como acompanhar erros de conexão e jogadas rejeitadas, medir reinícios e tempo de resposta e guardar cópia recuperável das contas e vitórias. O disco do [Render Free é efêmero](https://render.com/docs/free), e o plano [Neon Free tem limites próprios](https://neon.com/pricing); a escolha do mecanismo de backup e sua frequência ainda dependem da arquitetura. Logs não devem incluir senhas, tokens de sessão ou cartas ocultas de outros jogadores.

## Verificações antes de confirmar a stack

1. Testar um cliente TypeScript com servidor Python, inclusive reconexão, confirmação e duplicação de ações; verificar compatibilidade de versões do protocolo.
2. Forçar reinício do servidor e verificar se a partida e as mãos podem ser reconstruídas sem expor cartas e sem violar o prazo de um minuto.
3. Medir três salas de dez pessoas, atualização de jogadas e uso de recursos no plano candidato.
4. Testar cadastro, login, limitação de tentativas, expiração de sessão e acesso às mãos por jogadores e espectadores.
5. Verificar telas de cerca de 360 px e 1280 px e comparar o layout do Figma com os fluxos de requisitos.

Essas verificações são propostas; **nenhum protótipo, teste de carga, instalação ou implantação foi executado**. A stack e os serviços dependem da revisão do responsável pelo produto. A arquitetura e o planejamento de implementação pertencem às etapas posteriores.
