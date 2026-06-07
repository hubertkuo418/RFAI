# PilotDeck

Project-level PilotDeck settings for ResearchForge AI Lab.

Start PilotDeck with the repository config:

```bash
pilotdeck start --config pilotdeck/config.yaml
```

Workspace metadata remains under `workspaces/` so PilotDeck, the FastAPI core,
and future LangGraph flows can share the same source of truth.
