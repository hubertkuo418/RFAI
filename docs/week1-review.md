# Week 1 Review

Review date: 2026-06-08

Status: Complete for Week 1 project scope. The repository can route a user task
through FastAPI, the core router, a workspace decision, and a placeholder agent
response.

## Week 1 Goal

```text
User Input
    ↓
FastAPI / PilotDeck-facing Core
    ↓
Router
    ↓
Workspace
    ↓
Agent
    ↓
Response
```

## Completion Checklist

### Repository

- [x] GitHub Repo 建立
- [x] README 完成
- [x] License 完成
- [x] `.gitignore` 完成
- [x] 基礎目錄完成：`docs/`, `apps/`, `services/`, `workspaces/`, `configs/`, `docker/`, `scripts/`

### Environment

- [x] `requirements.txt` 建立
- [x] Conda env `researchforge` 建立
- [x] `researchforge` uses Python 3.12.13
- [x] Python dependencies 可安裝
- [x] Git 可用
- [x] Node.js 22 可用
- [x] Docker CLI 可用
- [x] VSCode 專案設定存在

Python environment note: normal development uses the conda environment
`researchforge` at `/home/hubert/miniconda3/envs/researchforge`, verified with
Python 3.12.13. The shell may still default to the `base` environment unless
`conda activate researchforge` is run.

### PilotDeck

- [x] PilotDeck CLI 可用
- [x] `pilotdeck/` 專案設定目錄建立
- [x] `pilotdeck/config.yaml` 建立
- [x] `configs/pilotdeck.config.yaml` 建立
- [x] Workspace metadata 建立

### Workspace Metadata

- [x] `workspaces/research/workspace.json`
- [x] `workspaces/course/workspace.json`
- [x] `workspaces/hardware/workspace.json`
- [x] Agent metadata 名稱統一為短名稱：`paper`, `research`, `writing`, `course`, `knowledge`, `hardware`, `experiment`

### Core

- [x] Router 建立：`services/core/router.py`
- [x] Router MVP 測試建立：`services/core/test_router.py`
- [x] Agent registry 建立：`services/core/agent_registry.py`
- [x] Placeholder agents 建立：`services/agents/`
- [x] `research` workspace routes to `paper_agent`
- [x] `course` workspace routes to `course_agent`
- [x] `hardware` workspace routes to `hardware_agent`

### FastAPI Backend

- [x] FastAPI app 建立：`services/core/main.py`
- [x] `GET /` returns running status
- [x] `GET /health` returns healthy status
- [x] `POST /task` routes task and returns placeholder agent response

### Docker

- [x] Root `Dockerfile` 建立
- [x] `docker-compose.yml` 建立
- [x] Docker Compose config 可解析
- [ ] Docker build 本機驗證
- [ ] Docker compose up 本機驗證

Docker local validation note: Docker is installed, but the current user cannot
access `/var/run/docker.sock` in this shell. Add the user to the `docker` group
or run from a Docker-enabled shell, then verify with:

```bash
docker compose build
docker compose up
```

### CI/CD

- [x] GitHub Actions workflow 建立：`.github/workflows/ci.yml`
- [x] CI installs Python 3.12 dependencies
- [x] CI runs compile, router smoke test, and API smoke test

### Documentation

- [x] `docs/architecture.md`
- [x] `docs/roadmap.md`
- [x] `docs/environment.md`
- [x] `docs/week1-review.md`

## Fixes Applied During Review

- Added `pilotdeck/` project config structure.
- Added GitHub Actions CI smoke workflow.
- Updated Router to expose `route(task)` for the Day 4 MVP shape.
- Kept Day 4 route outputs as `paper_agent`, `course_agent`, and `hardware_agent`.
- Added registry aliases so route outputs can resolve to short-name workspace agents.
- Updated FastAPI imports to package-safe imports from `services.core.*`.
- Updated `/task` endpoint to return a placeholder agent response.
- Updated Dockerfile to launch `services.core.main:app` from the repository root.
- Updated environment smoke-test documentation.

## Verification Run

```bash
python -m compileall services
python -m services.core.test_router
python -c "from fastapi.testclient import TestClient; from services.core.main import app; c=TestClient(app); assert c.get('/').json()['status'] == 'running'; assert c.get('/health').json()['status'] == 'healthy'; r=c.post('/task', json={'workspace':'research','query':'Transformer quantization paper'}).json(); assert r['agent'] == 'paper_agent'; assert r['status'] == 'routed'; assert 'Paper Agent' in r['response']; print('api ok')"
docker compose config
```

The Python checks were also verified through the project conda environment:

```bash
conda run -n researchforge python -m compileall services
conda run -n researchforge python -m services.core.test_router
conda run -n researchforge python -c "from fastapi.testclient import TestClient; from services.core.main import app; c=TestClient(app); assert c.get('/').json()['status'] == 'running'; assert c.get('/health').json()['status'] == 'healthy'; r=c.post('/task', json={'workspace':'research','query':'Transformer quantization paper'}).json(); assert r['agent'] == 'paper_agent'; assert r['status'] == 'routed'; assert 'Paper Agent' in r['response']; print('api ok')"
```

Result:

- [x] Python modules compile
- [x] Router smoke test passes and returns `paper_agent`
- [x] API smoke test passes
- [x] Conda env `researchforge` smoke tests pass
- [x] Workspace JSON files are valid
- [x] Workspace agents resolve through registry
- [x] Docker Compose config parses
- [ ] Docker daemon build/run blocked by local socket permission

## Week 1 Deliverables

- [x] Repo Scaffold
- [x] PilotDeck Workspace
- [x] Core Router MVP
- [x] FastAPI Backend
- [x] Docker Environment files
- [x] CI/CD smoke workflow
- [x] Documentation

## Week 2 Readiness

- [x] 可以進入 Week 2
- [ ] 需要補強

Remaining operational item: re-run Docker build and compose-up after Docker
socket permission is fixed for the current shell.
