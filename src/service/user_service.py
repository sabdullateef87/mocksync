
from fastapi import Depends
from src.models.model import User
from src.models.request.user_requests import CreateUser
from src.repository.user_repository import UserRepository
from src.util.jwt_util import get_password_hash

class UserService:
    
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo = user_repo
    
    def create_user(self, user: CreateUser):
        
        password_hash = get_password_hash(user.password)
        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=password_hash,
            subscription="GOLDEN"
        )
        
        return self.user_repo.create_user(new_user)
    