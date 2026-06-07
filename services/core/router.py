from typing import Dict

ROUTES = {
    "research": "paper_agent",
    "course": "course_agent",
    "hardware": "hardware_agent"
}

def route(task: Dict):

    workspace = task.get("workspace")

    return ROUTES.get(
        workspace,
        "unknown_agent"
    )