from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4


class TaskRequest(BaseModel):
    workspace: str
    query: str


class TaskResponse(BaseModel):
    task_id: str
    workspace: str
    agent: str
    query: str
    status: str
    created_at: datetime