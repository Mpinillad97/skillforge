from fastapi import FastAPI

app = FastAPI(
    title="SkillForge API",
    description="Backend API for the SkillForge platform.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "SkillForge",
        "version": "0.1.0",
        "status": "running",
    }