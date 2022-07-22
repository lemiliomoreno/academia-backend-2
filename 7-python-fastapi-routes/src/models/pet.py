from pydantic import BaseModel


class CreatePet(BaseModel):
    animal: str
    name: str
