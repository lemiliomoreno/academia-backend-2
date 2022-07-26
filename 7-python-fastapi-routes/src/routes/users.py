from fastapi import APIRouter

from utils.environment import get_db_credentials


router = APIRouter(tags=["users"], prefix="/users")


@router.get("")
async def get_all_users():
    return {"users": ["user1", "user2"]}


@router.post("")
async def create_user():
    credentials = get_db_credentials()
    return {
        "msg": "user created",
        "db_user": credentials["db_user"],
        "db_host": credentials["db_host"],
    }


@router.get("/{id}")
async def get_user(id: int):
    return {"user": [f"user{id}"]}
