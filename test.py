from services.core.workspace_loader import load_workspace

workspace = load_workspace("hardware")

print(workspace["agents"])