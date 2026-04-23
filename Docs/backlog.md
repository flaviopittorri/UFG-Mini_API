# Backlog Minimo - MVP Micro-API de Tarefas

## Release 1 - Core

- [ ] **RF-01 - Criar tarefa**
  - Criterios de aceite:
  - `POST /tasks` cria tarefa com `titulo` obrigatorio.
  - Retorna `201` com ID unico e dados persistidos.
  - Valida erro `400/422` para payload invalido.

- [ ] **RF-02 - Listar tarefas**
  - Criterios de aceite:
  - `GET /tasks` retorna lista paginada.
  - Suporta filtro por `status` e `prioridade`.
  - Retorna `200` com schema consistente.

- [ ] **RF-03 - Consultar tarefa por ID**
  - Criterios de aceite:
  - `GET /tasks/{id}` retorna tarefa existente.
  - Retorna `404` quando ID nao encontrado.

- [ ] **RF-04 - Atualizar tarefa**
  - Criterios de aceite:
  - `PUT/PATCH /tasks/{id}` atualiza campos permitidos.
  - Mantem validacoes de dominio (`status`, `prioridade`).
  - Retorna `200` com objeto atualizado.

- [ ] **RF-05 - Remover tarefa**
  - Criterios de aceite:
  - `DELETE /tasks/{id}` remove tarefa existente.
  - Retorna `204` sem corpo.
  - Retorna `404` para recurso inexistente.

- [ ] **RT-01 - Health check operacional**
  - Criterios de aceite:
  - `GET /health` retorna `200`.
  - Payload contem `status: ok` e `timestamp` UTC.

## Release 2 - Qualidade

- [ ] **RT-02 - Suite minima de testes automatizados**
  - Criterios de aceite:
  - Testes de contrato das rotas core implementados.
  - Cobertura minima de 70% nos modulos de API.
  - Pipeline falha em caso de regressao.

- [ ] **RT-03 - Padrao de qualidade de codigo**
  - Criterios de aceite:
  - Ruff executa sem erros no CI.
  - Projeto com tipagem valida nos endpoints principais.

- [ ] **RT-04 - Tratamento padrao de erros**
  - Criterios de aceite:
  - Erros de validacao seguem formato unico.
  - Erros de negocio retornam codigo HTTP coerente.
  - Logs registram falhas com contexto minimo.

- [ ] **RT-05 - Documentacao tecnica minima**
  - Criterios de aceite:
  - README atualizado com setup e execucao.
  - Documentacao de escopo e backlog disponiveis em `docs/`.

## Release 3 - Final

- [ ] **RF-06 - Priorizacao assistida (MVP)**
  - Criterios de aceite:
  - Endpoint de priorizacao retorna score e ordem sugerida.
  - Regras consideram urgencia, impacto e esforco.
  - Fallback deterministico sem dependencia externa.

- [ ] **RT-06 - Observabilidade minima de producao**
  - Criterios de aceite:
  - Logs estruturados por requisicao habilitados.
  - Identificador de correlacao presente nas respostas/logs.

- [ ] **RT-07 - Empacotamento e execucao padronizada**
  - Criterios de aceite:
  - Dependencias fixadas em `requirements.txt`.
  - Aplicacao inicia via comando unico documentado.
  - Ambiente local reproduzivel com `.venv`.

- [ ] **RT-08 - Prontidao para entrega interna**
  - Criterios de aceite:
  - Checklist de aceite funcional concluido.
  - Historico de versao e tag de release gerados.
  - Sem erros criticos abertos no backlog.
