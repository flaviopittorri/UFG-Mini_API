# Checklist de Revisão da API de Tarefas

## 1. Pontos de acoplamento altos
- [ ] Instâncias de `TaskRepository`, `PriorityAdvisor` e `TaskService` são criadas diretamente em `task_routes.py` (dificulta testes e injeção de dependências).
- [ ] `TaskService` depende diretamente de `PriorityAdvisor`, mas não utiliza a sugestão de prioridade no fluxo (comentado).
- [ ] `TaskRepository` está acoplado ao modelo `TaskOut`, dificultando troca futura por outro backend.

## 2. Onde faltam validações
- [ ] Falta validação de existência de título único ou regras de negócio além do min/max length.
- [ ] Falta validação de datas (ex: `due_date` no passado).
- [ ] Falta validação de `completed` em `TaskUpdate` para evitar valores inválidos.
- [ ] Falta tratamento de erros para entradas inválidas no repository (ex: update/delete de IDs inexistentes só retornam None).
- [ ] Falta validação de prioridade (caso seja adicionada ao modelo futuramente).

## 3. 5 testes a priorizar na próxima release
- [ ] Criar tarefa com dados válidos (happy path).
- [ ] Atualizar tarefa inexistente (deve retornar 404).
- [ ] Deletar tarefa existente e garantir remoção.
- [ ] Criar tarefa com `due_date` inválida (passado).
- [ ] Listar tarefas e garantir retorno consistente após operações de CRUD.
