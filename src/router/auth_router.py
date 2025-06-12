from fastapi import APIRouter, Depends
from src.models.request.user_requests import CreateUser
from src.config.datasource_config import SessionDep
from src.models.response.api_response import Response
from src.service.user_service import UserService
from src.service.auth_service import AuthService
from src.exception.exception import BadRequestException
router = APIRouter()

@router.post("/auth")
async def create_user(user: CreateUser, auth_service: AuthService = Depends()):
    try:
        data = auth_service.register_user(user)
        return Response(success=True, data=data)
    except Exception as e:
        print("exception type" , type (e))
        raise e