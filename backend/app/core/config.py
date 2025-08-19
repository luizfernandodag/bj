from pydantic import BaseModel
import os

class Settings(BaseModel):
    app_env: str = os.getenv("APP_ENV", "dev")
    database_url: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5433/best_job")
    redis_url: str = os.getenv("REDIS_URL", "redis://redis:6379/0")
    secret_key: str = os.getenv("SECRET_KEY", "postgres")

settings = Settings()
