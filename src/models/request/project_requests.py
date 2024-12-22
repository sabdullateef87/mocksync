from pydantic import BaseModel
from typing import Optional


class CreateProject(BaseModel):
    name: str
    description: Optional[str] = None


class UpdateProject(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
