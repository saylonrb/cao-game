# Pendências — Caô!

**Ponto de controle atual:** Etapa 6 autorizada; I0 parcialmente verificado. Hospedagem remota ainda não foi escolhida.

## Decisões e provas pendentes

1. Publicar o primeiro commit no repositório público `saylonrb/cao-game`, criar `staging` e verificar o CI remoto; commits, push de branches e PRs foram autorizados pelo responsável em 16/11/2026.
2. Iniciar PostgreSQL local e verificar conexão/migrações quando o daemon Docker estiver disponível; `docker compose config` já passou.
3. Implementar I1 (contas e lobby) com testes unitários e de integração; confirmar execução real do CI após a publicação da base.
4. Definir navegadores suportados e metas de resposta após medição; detalhar sessão, backup e monitoramento antes do piloto remoto.
5. Avaliar Render Free + Neon Free e alternativas apenas quando houver necessidade de piloto remoto; não criar serviços ou aceitar despesas sem autorização.
6. Na implementação, provar reconexão, recuperação após reinício, cotas de hospedagem, proteção de contas e mãos ocultas; consultar o layout parcialmente pronto no Figma quando o projeto da interface começar.

## Para detalhamento posterior

- Definir nomes e aparência das cartas, conjunto inicial de avatares e cenário.
- Planejar recuperação de senha, histórico detalhado de partidas, expulsão de participantes e novas opções visuais como possibilidades futuras, fora da primeira versão.
- Avaliar proteção contra abuso de convites e de criação de salas durante o projeto de segurança.

Os requisitos e critérios de aceitação da primeira versão estão em [requisitos.md](../01-requisitos/requisitos.md).
