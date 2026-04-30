"""
Repositório em memória para tarefas.
"""
from typing import List, Optional
from threading import Lock
from datetime import datetime
from app.models.task import TaskCreate, TaskUpdate, TaskOut

class TaskRepository:
    """Repositório em memória para tarefas."""
    def __init__(self):
        self._tasks: dict[int, TaskOut] = {}
        self._next_id: int = 1
        self._lock = Lock()

    def create(self, data: TaskCreate) -> TaskOut:
        """Cria uma nova tarefa."""
        with self._lock:
            now = datetime.utcnow()
            task = TaskOut(
                id=self._next_id,
                title=data.title,
                description=data.description,
                due_date=data.due_date,
                completed=data.completed,
                created_at=now,
                updated_at=now
            )
            self._tasks[self._next_id] = task
            self._next_id += 1
            return task

    def list(self) -> List[TaskOut]:
        """Lista todas as tarefas."""
        with self._lock:
            return list(self._tasks.values())

    def get_by_id(self, task_id: int) -> Optional[TaskOut]:
        """Obtém uma tarefa pelo ID."""
        with self._lock:
            return self._tasks.get(task_id)

    def update(self, task_id: int, data: TaskUpdate) -> Optional[TaskOut]:
        """Atualiza uma tarefa existente."""
        with self._lock:
            task = self._tasks.get(task_id)
            if not task:
                return None
            updated = task.model_copy(update={
                k: v for k, v in data.model_dump(exclude_unset=True).items() if v is not None
            })
            updated.updated_at = datetime.utcnow()
            self._tasks[task_id] = updated
            return updated

    def delete(self, task_id: int) -> bool:
        """Remove uma tarefa pelo ID."""
        with self._lock:
            return self._tasks.pop(task_id, None) is not None
