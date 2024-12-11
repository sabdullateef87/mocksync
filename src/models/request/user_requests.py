from pydantic import BaseModel

class CreateUser(BaseModel):
    username : str | None = None
    email : str
    password : str
    