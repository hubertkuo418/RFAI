from fastapi import FastAPI
from datetime import datetime
from uuid import uuid4

from models import TaskRequest
from router import route_task

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

    agent = route_task(task.workspace)

    return {
        "task_id": str(uuid4()),
        "workspace": task.workspace,
        "agent": agent,
        "query": task.query,
        "status": "routed",
        "created_at": datetime.utcnow()
    }
    
    
@app.get("/health")
def health():
    return {
        "service":"ResearchForge Core",
        "status":"healthy"
    }