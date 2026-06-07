from typing import Dict

ROUTES = {
    "research": "paper",
    "course": "course",
    "hardware": "hardware"
}

def route(task: Dict):

    workspace = task.get("workspace")

    return ROUTES.get(
        workspace,
        "unknown_agent"
    )
