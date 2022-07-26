from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from crud import users
from models.users import CreateUser
from utils.database import SessionLocal


router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

@router.get("")
def get_users(db: Session = Depends(get_db)):
    db_users = users.get_all_users(db)
    return JSONResponse(
        content=[{"email": db_user.email, "password": db_user.password} for db_user in db_users],
        status_code=200
    )


@router.post("")
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user_created = users.create_user(db, user)
    return JSONResponse(
        content={
            "email": user_created.email,
            "password": user_created.password,
        },
        status_code=201
    )
