from fastapi import APIRouter, Depends
from src.models.request.user_requests import CreateUser
from src.config.datasource_config import SessionDep
from src.service.user_service import UserService
from src.exception.exception import BadRequestException
router = APIRouter()

@router.post("/user")
async def create_user(
    user: CreateUser, user_service: UserService = Depends()):
    
    try:
    
        new_user = user_service.create_user(user)
        return {"message": "User created successfully"}
    except Exception as e:
        print("exception type" , type (e))
        raise e
    