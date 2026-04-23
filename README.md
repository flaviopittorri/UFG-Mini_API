# Micro-API de Gestao de Tarefas com Priorizacao Assistida por IA

## Objetivo
Este projeto e um MVP de micro-API para gestao de tarefas com priorizacao assistida por IA.

O foco inicial e:
- cadastrar e acompanhar tarefas;
- classificar tarefas por prioridade;
- sugerir ordem de execucao com apoio de IA.

A proposta e validar rapidamente o fluxo principal de produto com uma base tecnica simples, escalavel e facil de evoluir.

## Stack
- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic
- Pytest (testes)
- Ruff (lint)
- Git (versionamento)

## Como Rodar Localmente
### 1. Pre-requisitos
- Python 3.11 ou superior
- Git instalado

### 2. Clonar o repositorio
```bash
git clone <url-do-repositorio>
cd Laboratorio-Projeto
```

### 3. Criar e ativar o ambiente virtual
Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instalar dependencias
Dependencias principais:
```bash
pip install fastapi uvicorn[standard] pydantic
```

Dependencias de desenvolvimento (opcional):
```bash
pip install pytest ruff
```

### 5. Estrutura inicial sugerida
```text
.
|-- app/
|   |-- main.py
|   |-- api/
|   |-- services/
|   `-- models/
|-- tests/
|-- .gitignore
`-- README.md
```

### 6. Executar a API
Com um arquivo `app/main.py` contendo uma instancia `FastAPI`:
```bash
uvicorn app.main:app --reload
```

Endpoints locais:
- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Roadmap de Releases
### R0 - Setup tecnico
- [ ] Inicializar repositorio e padroes de projeto
- [ ] Configurar ambiente local, lint e testes basicos
- [ ] Criar endpoint de health check

### R1 - CRUD de tarefas
- [ ] Criar tarefa
- [ ] Listar tarefas
- [ ] Atualizar status e prioridade
- [ ] Remover tarefa

### R2 - Priorizacao assistida por IA (MVP)
- [ ] Criar endpoint de sugestao de prioridade
- [ ] Implementar regras iniciais de score (impacto, urgencia, esforco)
- [ ] Adicionar fallback deterministico sem dependencia externa

### R3 - Qualidade e observabilidade
- [ ] Atingir cobertura minima de testes
- [ ] Implementar logs estruturados
- [ ] Validar erros e contratos

### R4 - Preparacao para producao
- [ ] Containerizar aplicacao
- [ ] Configurar variaveis de ambiente por perfil
- [ ] Criar pipeline CI com testes e lint

## Status
Projeto em fase inicial de MVP.
