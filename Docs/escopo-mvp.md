# Escopo do MVP - Micro-API de Tarefas

## 1. Objetivo
Definir o escopo do MVP de uma micro-API para gestao de tarefas voltada ao uso de equipe interna, com foco em entrega rapida, simplicidade operacional e validacao do fluxo principal de trabalho.

O MVP deve permitir cadastro, consulta e atualizacao de tarefas, incluindo priorizacao basica para apoiar a organizacao do backlog operacional da equipe.

## 2. Requisitos Funcionais
### RF-01 - Criar tarefa
A API deve permitir criar uma tarefa com, no minimo, os seguintes campos:
- titulo (obrigatorio)
- descricao (opcional)
- prioridade (baixa, media, alta)
- status inicial (pendente)
- data/hora de criacao

### RF-02 - Listar tarefas
A API deve permitir listar tarefas com suporte a:
- paginacao basica
- filtro por status
- filtro por prioridade
- ordenacao por data de criacao e prioridade

### RF-03 - Consultar tarefa por identificador
A API deve permitir consultar os dados de uma tarefa especifica por ID unico.

### RF-04 - Atualizar tarefa
A API deve permitir atualizar campos editaveis da tarefa, incluindo:
- titulo
- descricao
- prioridade
- status (pendente, em_progresso, concluida)

### RF-05 - Remover tarefa
A API deve permitir remover uma tarefa por ID.

### RF-06 - Endpoint de health check
A API deve expor endpoint de verificacao de saude para monitoramento basico do servico.

### RF-07 - Priorizacao assistida (MVP)
A API deve disponibilizar mecanismo inicial de priorizacao assistida, baseado em regras deterministicas (score por urgencia/impacto/esforco), sem dependencia obrigatoria de servicos externos de IA nesta fase.

## 3. Requisitos Nao Funcionais
### RNF-01 - Desempenho
- Tempo medio de resposta inferior a 300 ms para operacoes de leitura em ambiente interno padrao.
- Suporte inicial a uso concorrente de baixa escala (equipe interna).

### RNF-02 - Confiabilidade
- Estrutura de tratamento de erros com codigos HTTP consistentes.
- Validacao de payload de entrada e saida.

### RNF-03 - Observabilidade
- Endpoint de health check ativo.
- Logs basicos por requisicao com informacoes de erro e status.

### RNF-04 - Manutenibilidade
- Codigo com tipagem, organizacao modular e padrao de nomenclatura consistente.
- Documentacao minima de execucao local e endpoints principais.

### RNF-05 - Seguranca (escopo MVP interno)
- Uso restrito a rede/ambiente interno.
- Nao expor segredos em codigo-fonte.
- Preparacao para incluir autenticacao/autorizacao em release posterior.

### RNF-06 - Portabilidade
- Execucao local via ambiente virtual Python 3.11+.
- Dependencias declaradas em arquivo de requisitos.

## 4. Fora de Escopo (MVP)
- Interface web para usuarios finais.
- Autenticacao e autorizacao completas (RBAC, SSO, OAuth2).
- Integracao com provedores externos de IA generativa.
- Persistencia com banco distribuito e estrategia avancada de escalabilidade.
- SLA formal de alta disponibilidade.
- Auditoria completa e trilha de conformidade.
- Notificacoes em tempo real (email, chat, webhook).
- Multi-tenant e controle avancado por organizacao.

## 5. Criterios de Aceite do MVP
- CRUD de tarefas operacional com validacao de dados.
- Endpoint de health check funcional.
- Priorizacao assistida basica operacional por regras internas.
- Documentacao inicial disponivel para execucao local.
- Testes minimos cobrindo rotas criticas (health check e fluxos principais de tarefa).
