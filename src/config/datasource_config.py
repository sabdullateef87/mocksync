import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, select, create_engine
# from src.models.model import User, Project, Collection, API

load_dotenv();

DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')


def build_database_connection_string():
    url = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'
    return url

    
SQLALCHEMY_DATABASE_URL = build_database_connection_string()
connect_args = {"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

async def create_db_and_table():
    print("creating sql tables")
    SQLModel.metadata.create_all(engine)
    
async def get_session():
    with Session(engine) as session:
        yield session
        
SessionDep = Annotated[Session, Depends(get_session)]