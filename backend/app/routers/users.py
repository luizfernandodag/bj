from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])    
@router.get("/")
def list_user():
    return [{"id":1, "name":"Luiz"}]

@router.post("/")
def create_user(user:dict):
    return {"id":2, **user}