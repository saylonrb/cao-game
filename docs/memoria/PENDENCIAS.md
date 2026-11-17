# Pendências — Caô!

**Ponto de controle atual:** Etapa 6 autorizada; I0 parcialmente verificado. Hospedagem remota ainda não foi escolhida.

## Decisões e provas pendentes

1. Iniciar PostgreSQL local e verificar conexão/migrações quando o daemon Docker estiver disponível; `docker compose config` já passou.
2. Implementar I1 (contas e lobby) com testes unitários e de integração; o CI remoto já passou após a correção por PRs #1 e #2.
3. Definir navegadores suportados e metas de resposta após medição; detalhar sessão, backup e monitoramento antes do piloto remoto.
4. Avaliar Render Free + Neon Free e alternativas apenas quando houver necessidade de piloto remoto; não criar serviços ou aceitar despesas sem autorização.
5. Na implementação, provar reconexão, recuperação após reinício, cotas de hospedagem, proteção de contas e mãos ocultas; consultar o layout parcialmente pronto no Figma quando o projeto da interface começar.

## Para detalhamento posterior

- Definir nomes e aparência das cartas, conjunto inicial de avatares e cenário.
- Planejar recuperação de senha, histórico detalhado de partidas, expulsão de participantes e novas opções visuais como possibilidades futuras, fora da primeira versão.
- Avaliar proteção contra abuso de convites e de criação de salas durante o projeto de segurança.

Os requisitos e critérios de aceitação da primeira versão estão em [requisitos.md](../01-requisitos/requisitos.md).
