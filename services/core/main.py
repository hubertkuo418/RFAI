from fastapi import FastAPI

app = FastAPI(
    title="ResearchForge AI Lab"
)

@app.get("/")
def root():

    return {
        "status": "running",
        "project": "ResearchForge AI Lab"
    }