import os



from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select

DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
DATABASE_NAME = os.environ.get('DATABASE_NAME')


def build_database_connection_string():
    return f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
    
SQLALCHEMY_DATABASE_URL = build_database_connection_string()
connect_args = {"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session
        
SessionDep = Annotated[Session, Depends(get_session)]