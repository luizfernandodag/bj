from fastapi import FastAPI
from app.core.db import healthcheck_db
from app.routers import jobs, users

app = FastAPI(title="Best Jobs API", version="0.1.0")

app.include_router(jobs.router)
app.include_router(users.router)

@app.get("/health")
def health():
    db_status = healthcheck_db()
    return {
        "status": "ok" if db_status.get("database") == "ok" else "error",
        "components": {
            "database": db_status
        }
    }
    