# Execução Inicial da API de Tarefas

## 1. Criação de tarefas

### Requisição
```
POST /tasks/
{
  "title": "Primeira tarefa",
  "description": "Descrição teste",
  "completed": false
}
```
Resposta:
```
201 Created
{
  "id": 1,
  "title": "Primeira tarefa",
  "description": "Descri��o teste",
  "due_date": null,
  "completed": false,
  "created_at": "...",
  "updated_at": "..."
}
```

### Requisição
```
POST /tasks/
{
  "title": "Segunda tarefa",
  "description": "Outra descrição",
  "completed": false
}
```
Resposta:
```
201 Created
{
  "id": 2,
  "title": "Segunda tarefa",
  "description": "Outra descri��o",
  "due_date": null,
  "completed": false,
  "created_at": "...",
  "updated_at": "..."
}
```

## 2. Listagem de tarefas

### Requisição
```
GET /tasks/
```
Resposta:
```
200 OK
[
  {
    "id": 1,
    "title": "Primeira tarefa",
    "description": "Descri��o teste",
    "due_date": null,
    "completed": false,
    "created_at": "...",
    "updated_at": "..."
  },
  {
    "id": 2,
    "title": "Segunda tarefa",
    "description": "Outra descri��o",
    "due_date": null,
    "completed": false,
    "created_at": "...",
    "updated_at": "..."
  }
]
```

Esses exemplos mostram a API funcionando: criação e listagem de tarefas via HTTP.
