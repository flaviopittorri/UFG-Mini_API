"""
Modelos Pydantic para operações de tarefas.
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    """Dados para criação de uma tarefa."""
    title: str = Field(..., min_length=1, max_length=100, description="Título da tarefa")
    description: Optional[str] = Field(None, max_length=500, description="Descrição detalhada")
    due_date: Optional[datetime] = Field(None, description="Data limite para conclusão")
    completed: bool = Field(default=False, description="Status de conclusão")

class TaskUpdate(BaseModel):
    """Dados para atualização parcial de uma tarefa."""
    title: Optional[str] = Field(None, min_length=1, max_length=100, description="Título da tarefa")
    description: Optional[str] = Field(None, max_length=500, description="Descrição detalhada")
    due_date: Optional[datetime] = Field(None, description="Data limite para conclusão")
    completed: Optional[bool] = Field(None, description="Status de conclusão")

class TaskOut(BaseModel):
    """Modelo de saída para uma tarefa."""
    id: int = Field(..., description="ID da tarefa")
    title: str = Field(..., description="Título da tarefa")
    description: Optional[str] = Field(None, description="Descrição detalhada")
    due_date: Optional[datetime] = Field(None, description="Data limite para conclusão")
    completed: bool = Field(..., description="Status de conclusão")
    created_at: datetime = Field(..., description="Data de criação")
    updated_at: datetime = Field(..., description="Data da última atualização")
