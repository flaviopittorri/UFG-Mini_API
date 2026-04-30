"""
Testes para TaskService usando Pytest.
"""
import pytest
from app.models.task import TaskCreate, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import PriorityAdvisor
from app.services.task_service import TaskService

@pytest.fixture
def task_service():
    repo = TaskRepository()
    advisor = PriorityAdvisor()
    return TaskService(repo, advisor)

@pytest.fixture
def sample_task():
    return TaskCreate(title="Teste", description="Descrição", due_date=None, completed=False)

def test_create_task(task_service, sample_task):
    task = task_service.create_task(sample_task)
    assert task.id == 1
    assert task.title == "Teste"
    assert task.completed is False

def test_list_tasks(task_service, sample_task):
    task_service.create_task(sample_task)
    tasks = task_service.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Teste"

def test_update_task(task_service, sample_task):
    task = task_service.create_task(sample_task)
    update = TaskUpdate(title="Atualizado", completed=True)
    updated = task_service.update_task(task.id, update)
    assert updated is not None
    assert updated.title == "Atualizado"
    assert updated.completed is True

def test_delete_task(task_service, sample_task):
    task = task_service.create_task(sample_task)
    deleted = task_service.delete_task(task.id)
    assert deleted is True
    assert task_service.get_task(task.id) is None

def test_update_nonexistent_task(task_service):
    update = TaskUpdate(title="Inexistente")
    result = task_service.update_task(999, update)
    assert result is None

def test_delete_nonexistent_task(task_service):
    deleted = task_service.delete_task(999)
    assert deleted is False