# Development Environment

This project uses the `researchforge` conda environment for Python development.

## Python

Required Python version:

```powershell
Python 3.12
```

Current verified conda environment:

```bash
conda run -n researchforge python --version
```

Verified:

```text
Python 3.12.13
```

## Activate Environment

Activate the project environment before development:

```bash
conda activate researchforge
```

If the shell has not activated the env, run commands through conda:

```bash
conda run -n researchforge python -m services.core.test_router
```

## Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## Smoke Tests

Router:

```bash
python -m services.core.test
```

Expected:

```text
paper_agent
```

FastAPI app import and endpoints:

```bash
python -c "from fastapi.testclient import TestClient; from services.core.main import app; c=TestClient(app); print(c.get('/').json()); print(c.get('/health').json()); print(c.post('/task', json={'workspace':'research','query':'Transformer quantization paper'}).json())"
```

Expected:

```text
{'status': 'running'}
{'service': 'ResearchForge Core', 'status': 'healthy'}
...
```

## Tool Checks

```powershell
node --version
git --version
docker --version
```

Docker must be available on `PATH` before the Week 1 Day 6 Docker tasks.
