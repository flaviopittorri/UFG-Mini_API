from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime



from app.api.task_routes import router as task_router

app = FastAPI(title="Task Prioritization API")
app.include_router(task_router)


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", timestamp=datetime.now(timezone.utc))
