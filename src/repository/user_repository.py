from fastapi import Depends
from src.config.datasource_config import SessionDep
from src.models.request.user_requests import CreateUser
from src.models.user_model import User


class UserRepository:
    def __init__(self, session: SessionDep):
        self.session = session
        
    def create_user(self, user : User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        
        return user
