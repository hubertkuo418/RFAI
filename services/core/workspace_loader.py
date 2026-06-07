import json
from pathlib import Path


WORKSPACE_ROOT = Path("workspaces")


def load_workspace(name: str) -> dict:
    path = WORKSPACE_ROOT / name / "workspace.json"

    if not path.exists():
        raise FileNotFoundError(f"Workspace not found: {name}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def list_workspaces() -> list[dict]:
    workspaces = []

    for workspace_dir in WORKSPACE_ROOT.iterdir():
        config_path = workspace_dir / "workspace.json"

        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                workspaces.append(json.load(f))

    return workspaces