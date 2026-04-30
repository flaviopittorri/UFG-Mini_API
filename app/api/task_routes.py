"""
Rotas de tarefas para FastAPI.
"""
from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.task import TaskCreate, TaskUpdate, TaskOut
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import PriorityAdvisor
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])

repo = TaskRepository()
advisor = PriorityAdvisor()
service = TaskService(repo, advisor)

@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate) -> TaskOut:
    return service.create_task(task)

@router.get("/", response_model=List[TaskOut])
def list_tasks() -> List[TaskOut]:
    return service.list_tasks()

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int) -> TaskOut:
    task = service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task_update: TaskUpdate) -> TaskOut:
    updated = service.update_task(task_id, task_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return updated

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    deleted = service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
