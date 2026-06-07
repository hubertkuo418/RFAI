from services.core.workspace_loader import list_workspaces, load_workspace


if __name__ == "__main__":
    print("All workspaces:")
    for workspace in list_workspaces():
        print("-", workspace["name"])

    print("\nResearch workspace:")
    print(load_workspace("research"))