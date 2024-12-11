from fastapi import APIRouter, Depends
from src.models.request.user_requests import CreateUser
from src.config.datasource_config import SessionDep
from src.service.user_service import UserService

router = APIRouter()

@router.post("/user")
async def create_user(
    user: CreateUser, user_service: UserService = Depends()):
    
    new_user = user_service.create_user(user)
    return {"message": "User created successfully"}
    