from fastapi import APIRouter

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.get("/")
def list_jobs():
    return [{"id":1, "title":"Backend Engineer"}]

@router.post("/")
def create_job(job:dict):
    return {"id":2, **job}