"""
Serviço de tarefas com sugestão de prioridade.
"""
from typing import List, Optional
from app.models.task import TaskCreate, TaskUpdate, TaskOut
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import PriorityAdvisor

class TaskService:
    """Camada de serviço para tarefas."""
    def __init__(self, repository: TaskRepository, advisor: PriorityAdvisor):
        self._repo = repository
        self._advisor = advisor

    def create_task(self, data: TaskCreate) -> TaskOut:
        """Cria tarefa, sugerindo prioridade se aplicável."""
        # Exemplo: prioridade pode ser adicionada ao TaskOut futuramente
        # priority = self._advisor.suggest_priority(data)
        return self._repo.create(data)

    def list_tasks(self) -> List[TaskOut]:
        """Lista todas as tarefas."""
        return self._repo.list()

    def get_task(self, task_id: int) -> Optional[TaskOut]:
        """Obtém uma tarefa pelo ID."""
        return self._repo.get_by_id(task_id)

    def update_task(self, task_id: int, data: TaskUpdate) -> Optional[TaskOut]:
        """Atualiza uma tarefa."""
        return self._repo.update(task_id, data)

    def delete_task(self, task_id: int) -> bool:
        """Remove uma tarefa."""
        return self._repo.delete(task_id)
