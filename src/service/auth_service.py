from fastapi import Depends
from src.repository.auth_repository import AuthRepository
from src.models.request.user_requests import CreateUser
from src.models.user_model import User
from src.exception.exception import *
from src.util.jwt_util import *

class AuthService:
    def __init__(self, auth_repo : AuthRepository = Depends()):
        self.auth_repo = auth_repo
        
    def register_user(self, create_user_dto : CreateUser):
        # TODO :  return user details with token.
        existing_user = self.auth_repo.get_user_by_email(create_user_dto.email)
        if(existing_user != None):
            raise DuplicateException("User already exist.")
        new_user = self.auth_repo.register_user(create_user_dto)
        data = { "email": new_user.email }
        return create_access_token(data)
        