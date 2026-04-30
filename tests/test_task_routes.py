"""
Testes de integração para rotas /tasks usando TestClient.
"""
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.task_routes import router
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import PriorityAdvisor
from app.services.task_service import TaskService

@pytest.fixture
def app_with_isolated_repo():
    app = FastAPI()
    # Isola dependências para cada teste
    repo = TaskRepository()
    advisor = PriorityAdvisor()
    service = TaskService(repo, advisor)
    # Monkeypatch as dependências do router
    router.dependency_overrides = {}
    app.include_router(router)
    # Injeta dependências isoladas
    app.dependency_overrides = {
        TaskRepository: lambda: repo,
        PriorityAdvisor: lambda: advisor,
        TaskService: lambda: service,
    }
    return app

@pytest.fixture
def client(app_with_isolated_repo):
    return TestClient(app_with_isolated_repo)

def test_create_task(client):
    resp = client.post("/tasks/", json={"title": "Nova", "description": "desc", "completed": False})
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == "Nova"
    assert data["completed"] is False

def test_list_tasks(client):
    client.post("/tasks/", json={"title": "T1", "description": "desc", "completed": False})
    resp = client.get("/tasks/")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_update_task(client):
    post = client.post("/tasks/", json={"title": "T2", "description": "desc", "completed": False})
    tid = post.json()["id"]
    resp = client.put(f"/tasks/{tid}", json={"title": "Atualizada", "completed": True})
    assert resp.status_code == 200
    assert resp.json()["title"] == "Atualizada"
    assert resp.json()["completed"] is True

def test_delete_task(client):
    post = client.post("/tasks/", json={"title": "T3", "description": "desc", "completed": False})
    tid = post.json()["id"]
    resp = client.delete(f"/tasks/{tid}")
    assert resp.status_code == 204

def test_get_task_404(client):
    resp = client.get("/tasks/9999")
    assert resp.status_code == 404

def test_update_task_404(client):
    resp = client.put("/tasks/9999", json={"title": "X"})
    assert resp.status_code == 404

def test_delete_task_404(client):
    resp = client.delete("/tasks/9999")
    assert resp.status_code == 404
