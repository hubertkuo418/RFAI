from datetime import datetime
from uuid import uuid4

from fastapi import FastAPI

from services.core.agent_registry import get_agent
from services.core.models import TaskRequest
from services.core.router import route

app = FastAPI(
    title="ResearchForge AI Lab",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "status": "running"
    }


@app.post("/task")
def create_task(task: TaskRequest):
    agent = route(task.model_dump())
    response = None

    if agent is not None:
        response = get_agent(agent).run(task.query)

    return {
        "task_id": str(uuid4()),
        "workspace": task.workspace,
        "agent": agent,
        "query": task.query,
        "response": response,
        "status": "routed",
        "created_at": datetime.utcnow()
    }


@app.get("/health")
def health():
    return {
        "service": "ResearchForge Core",
        "status": "healthy"
    }
