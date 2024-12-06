from fastapi import Depends
from src.models.model import User
from src.config.datasource_config import SessionDep
from src.models.request.user_requests import CreateUser


class UserRepository:
    
    def __init__(self, session: SessionDep):
        self.session = session
        
    def create_user(self, user : User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        
        print(user)
        return user
