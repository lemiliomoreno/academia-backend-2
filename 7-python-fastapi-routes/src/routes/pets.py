from fastapi import APIRouter

from models.pet import CreatePet


router = APIRouter(
    tags=["pets"],
    prefix="/pets"
)


@router.get("")
async def get_all_pets():
    return {"pets": ["pet1", "pet2"]}

@router.post("")
async def create_pet(pet: CreatePet):
    return {"msg": "pet created", "animal": pet.animal, "name": pet.name}
