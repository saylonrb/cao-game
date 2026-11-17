# ADR-0001 — Estado autoritativo e recuperação da partida

**Data:** 16/11/2026

**Status:** aceita pelo responsável pelo produto em 16/11/2026.

## Contexto

Jogadas simultâneas, anúncios, denúncias, compra acumulada e reconexões exigem uma ordem única de decisões. A sala deve preservar mãos e resultado após reinício do servidor sem expor cartas de outros jogadores.

## Alternativas avaliadas

1. **Estado apenas na memória do servidor:** simples em funcionamento normal, mas perde a partida em reinício.
2. **Registro de cada evento e reconstrução por replay:** oferece histórico detalhado, mas acrescenta versões de eventos, replay e migrações para uma primeira versão que não mostra histórico.
3. **Instantâneo transacional por ação aceita:** mantém o estado atual versionado e recuperável, com custo de uma escrita por mudança e sem histórico completo de jogadas.

## Decisão

Usar servidor autoritativo com uma fila ou trava por sala em processo único. Após validar uma ação, salvar o novo estado da partida em JSONB no PostgreSQL, junto com versão, recibo do comando e demais alterações necessárias em uma transação. Confirmar ao cliente somente depois do commit. Enviar a cada pessoa uma projeção autorizada do estado; nunca transmitir o instantâneo bruto.

## Justificativa

O volume inicial previsto é de três salas de dez pessoas. O instantâneo dá um caminho direto para recuperar a partida, e a versão/recibo permitem rejeitar ações antigas e impedir duplicação após perda de confirmação. A complexidade de replay não se justifica sem necessidade de histórico detalhado nesta versão.

## Consequências e validação

- Cada mudança aceita grava no banco; medir latência e tamanho do estado com três salas de dez pessoas.
- Os dados de mãos e baralho precisam de regras rígidas de acesso e exclusão de logs.
- Um processo adicional não pode compartilhar as mesmas filas locais; escala horizontal requer novo desenho.
- Testar reinício antes e depois do commit, repetição de comando e reconexão com projeções corretas.
- Se o banco não estiver disponível, a ação não é aceita; o cliente recebe erro recuperável e sincroniza depois.

Fluxos e componentes estão na [visão arquitetural](../visao-arquitetural.md).
