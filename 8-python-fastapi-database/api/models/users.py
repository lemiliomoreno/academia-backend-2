from pydantic import BaseModel


class CreateUser(BaseModel):
    email: str
    password: str
    name: str
