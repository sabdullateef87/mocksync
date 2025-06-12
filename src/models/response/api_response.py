from typing import Generic, Optional, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel
from fastapi import FastAPI

# Generic Type for data
T = TypeVar("T")

# API Response Class
class Response(GenericModel, Generic[T]):
    success: bool
    message: Optional[str] = "Operation successful"
    data: Optional[T] = None
