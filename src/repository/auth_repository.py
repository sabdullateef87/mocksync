from fastapi import Depends
from src.models.user_model import User
from src.config.datasource_config import SessionDep
from src.models.request.user_requests import CreateUser
from src.util.jwt_util import *
from sqlmodel import select

class AuthRepository:
    def __init__(self, session: SessionDep):
        self.session = session
        
    def register_user(self, user: CreateUser) -> User:
        
        new_user = User (
            username=user.username,
            email=user.email,
            hashed_password= get_password_hash(user.password),
            subscription="BASIC"
        )
        try:
            self.session.add(new_user)
            self.session.commit()
            self.session.refresh(new_user)
            return new_user
        except Exception as ex:
            raise ex
    
    def get_user_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()