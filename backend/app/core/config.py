from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "SkillForge API"
    VERSION: str = "0.1.0"


settings = Settings()