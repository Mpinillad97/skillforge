from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["Root"])
def root():
    return {
        "name": "SkillForge",
        "version": "0.1.0",
        "status": "running",
    }