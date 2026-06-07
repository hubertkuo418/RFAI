from typing import Mapping


ROUTES = {
    "research": "paper_agent",
    "course": "course_agent",
    "hardware": "hardware_agent",
}


def route(task: Mapping[str, str]) -> str | None:
    workspace = task.get("workspace")
    return ROUTES.get(workspace)


def route_task(workspace: str) -> str | None:
    return route({"workspace": workspace})
