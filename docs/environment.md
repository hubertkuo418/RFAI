# Development Environment

This project uses the `researchforge` conda environment for Python development.

## Python

Required Python version:

```powershell
Python 3.12
```

Current verified environment:

```powershell
C:\Users\huber\anaconda3\envs\researchforge\python.exe --version
```

Expected:

```text
Python 3.12.x
```

## Activate Environment

If `conda` is available in the shell:

```powershell
conda activate researchforge
```

If `conda` is not on `PATH`, use the Anaconda Prompt or run Python directly:

```powershell
C:\Users\huber\anaconda3\envs\researchforge\python.exe
```

## Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

## Smoke Tests

Router:

```powershell
python -m services.core.test
```

Expected:

```text
paper
```

FastAPI app import and endpoints:

```powershell
python -c "from fastapi.testclient import TestClient; from services.core.main import app; c=TestClient(app); print(c.get('/').json()); print(c.get('/api/v1/health').json())"
```

Expected:

```text
{'project': 'ResearchForge AI Lab'}
{'status': 'ok'}
```

## Tool Checks

```powershell
node --version
git --version
docker --version
```

Docker must be available on `PATH` before the Week 1 Day 6 Docker tasks.
