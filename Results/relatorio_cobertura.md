# Relatório de Cobertura de Testes (pytest + coverage)

**Data:** 29/04/2026

## Resumo Geral
- **Cobertura total:** 83%
- **Testes executados:** 17 (todos passaram)

## Cobertura por arquivo

| Arquivo                                 | Stmts | Miss | Cobertura | Linhas não cobertas |
|-----------------------------------------|-------|------|-----------|---------------------|
| app/api/task_routes.py                  | 33    | 1    | 97%       | 30                  |
| app/main.py                             | 12    | 12   | 0%        | 1-21                |
| app/models/task.py                      | 21    | 0    | 100%      | -                   |
| app/repositories/task_repository.py     | 34    | 0    | 100%      | -                   |
| app/services/priority_advisor.py        | 36    | 13   | 64%       | 21-22, 37-60        |
| app/services/task_service.py            | 18    | 0    | 100%      | -                   |
| **TOTAL**                              | 154   | 26   | 83%       |                     |

## Pontos de atenção
- **app/main.py:** Não possui testes cobrindo o health check (`/health`) e inicialização do app.
- **app/services/priority_advisor.py:** Linhas não cobertas incluem chamadas à LLM/OpenAI e fallback de exceção.
- **app/api/task_routes.py:** Apenas 1 linha não coberta (provavelmente tratamento de erro ou fluxo alternativo).

## Recomendações
- Adicionar testes para o endpoint `/health` em `main.py`.
- Simular falhas e sucesso na integração com LLM/OpenAI para cobrir todos os fluxos do `PriorityAdvisor`.
- Garantir cobertura de todos os fluxos de erro nas rotas.

## Conclusão
A cobertura está excelente para o MVP, cobrindo toda a lógica de domínio e rotas principais. Pequenos ajustes podem levar a cobertura próxima de 100%.
