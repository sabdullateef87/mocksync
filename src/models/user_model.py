import datetime
from typing import Collection, List, Optional

from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str = Field(nullable=False)
    is_active: bool = Field(default=True)
    is_verified: bool = Field(default=False)
    is_superuser: bool = Field(default=False)
    failed_login_attempts: int = Field(default=0)
    subscription:str = Field(nullable=False)

    # One-to-many relationship
    projects: List["Project"] = Relationship(back_populates="user")
    

    
# class Collection(SQLModel, table=True):
#     __tablename__ = "collection"
    
#     id: int = Field(default=None, primary_key=True)
#     name: str = Field(default=None, nullable=False)

#     project_id: int = Field(foreign_key="project.id")
#     project: Project | None = Relationship(back_populates="project")
    
#     apis: List["API"] = Relationship(back_populates="collection")
    
# class API(SQLModel, table=True):
#     __tablename__ = "apis"

#     id: int = Field(default=None, primary_key=True)
#     name: str = Field(default=None, nullable=False)
#     endpoint: str = Field(default=None, nullable=False)
#     method: str = Field(default=None, nullable=False)
#     collection_id: int = Field(foreign_key="collection.id")

#     # Relationship field
#     collection: "Collection" = Relationship(back_populates="apis")