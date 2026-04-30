"""
Advisor de prioridade com heurística local e LLM opcional.
"""
import os
import requests
from typing import Optional
from app.models.task import TaskCreate

class PriorityAdvisor:
    """Sugere prioridade usando heurística local ou LLM se disponível."""
    def __init__(self, timeout: float = 3.0):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.timeout = timeout

    def suggest_priority(self, data: TaskCreate) -> str:
        """Sugere prioridade para a tarefa."""
        if not self.api_key:
            return self._local_heuristic(data)
        try:
            llm_priority = self._llm_suggest(data)
            if llm_priority:
                return llm_priority
        except Exception:
            pass  # Falha segura
        return self._local_heuristic(data)

    def _local_heuristic(self, data: TaskCreate) -> str:
        """Heurística local simples para prioridade."""
        if data.due_date:
            return "alta"
        if data.description and ("importante" in data.description.lower()):
            return "alta"
        return "normal"

    def _llm_suggest(self, data: TaskCreate) -> Optional[str]:
        """Sugere prioridade via LLM (OpenAI)."""
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        prompt = (
            "Classifique a prioridade da tarefa como 'alta', 'normal' ou 'baixa'. "
            f"Título: {data.title}\nDescrição: {data.description or ''}\n"
            f"Data limite: {data.due_date or 'nenhuma'}\n"
            "Responda apenas com a palavra da prioridade."
        )
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1,
            "temperature": 0
        }
        resp = requests.post(url, headers=headers, json=payload, timeout=self.timeout)
        resp.raise_for_status()
        result = resp.json()
        content = result["choices"][0]["message"]["content"].strip().lower()
        if content in {"alta", "normal", "baixa"}:
            return content
        return None
