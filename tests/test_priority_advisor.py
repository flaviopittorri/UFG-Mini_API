"""
Testes para PriorityAdvisor cobrindo heurística local, LLM e fallback.
"""
import pytest
from app.models.task import TaskCreate
from app.services.priority_advisor import PriorityAdvisor

@pytest.fixture
def advisor_sem_api(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "")
    return PriorityAdvisor()

@pytest.fixture
def advisor_com_api(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")
    return PriorityAdvisor()

def test_prioridade_alta_due_date(advisor_sem_api):
    task = TaskCreate(title="Tarefa", description="", due_date="2099-01-01T00:00:00", completed=False)
    assert advisor_sem_api.suggest_priority(task) == "alta"

def test_prioridade_alta_palavra_importante(advisor_sem_api):
    task = TaskCreate(title="Tarefa", description="Muito importante", due_date=None, completed=False)
    assert advisor_sem_api.suggest_priority(task) == "alta"

def test_prioridade_normal(advisor_sem_api):
    task = TaskCreate(title="Tarefa", description="Sem urgência", due_date=None, completed=False)
    assert advisor_sem_api.suggest_priority(task) == "normal"

def test_fallback_para_heuristica(monkeypatch, advisor_com_api):
    # Simula falha na chamada externa
    def fake_llm_suggest(self, data):
        raise Exception("Falha externa")
    monkeypatch.setattr(PriorityAdvisor, "_llm_suggest", fake_llm_suggest)
    task = TaskCreate(title="Tarefa", description="Sem urgência", due_date=None, completed=False)
    assert advisor_com_api.suggest_priority(task) == "normal"
