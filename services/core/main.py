from fastapi import FastAPI
from services.api.v1.routes import router

app = FastAPI(
    title="ResearchForge AI Lab",
    version="0.1.0"
)

app.include_router(
    router,
    prefix="/api/v1"
)

@app.get("/")
def root():
    return {
        "project": "ResearchForge AI Lab",
        "status": "running"
    }