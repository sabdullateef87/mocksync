from typing import Collection, Optional
from sqlmodel import Field, Relationship, SQLModel

from src.models.user_model import User


class Project(SQLModel, table=True):
    __tablename__ = "project"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    description: Optional[str] = None
    
    user_id: int = Field(foreign_key="users.id")
    user: User | None = Relationship(back_populates="project")
    
# Foreign key and relationship
    user_id: int = Field(foreign_key="users.id", nullable=False)
    user: "User" = Relationship(back_populates="projects")