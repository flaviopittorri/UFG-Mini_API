# Revisao de Escopo e Backlog

## 1) O que esta grande demais para release inicial
- CRUD completo + filtros + ordenacao + paginacao no mesmo pacote pode estourar prazo.
- `PUT` e `PATCH` juntos no inicio aumenta superficie de bugs de atualizacao.
- Meta de performance (<300 ms) ja na release core pode virar gargalo prematuro.

## 2) O que esta faltando para testabilidade
- Definir estrategia de persistencia para testes (SQLite em memoria ou doubles de repositorio).
- Congelar tempo nos testes (clock injetavel) para validar `timestamp` e ordenacao.
- Padronizar fixtures/massa de dados e cenarios minimos por endpoint (sucesso, validacao, nao encontrado).
- Definir contrato de erro unico (schema de erro) para testes de regressao.
- Criterios de cobertura por camada (API, service, repository), nao so cobertura global.

## 3) Quais 3 riscos tecnicos mitigar antes da implementacao
- Acoplamento excessivo entre API/Service/Repository sem interfaces claras.
- Regra de priorizacao instavel (heuristica sem pesos/versionamento), causando comportamento inconsistente.
- Divergencia entre ambiente local e CI/producao (dependencias, banco, configuracoes), gerando "funciona na minha maquina".
