from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from models.database import User
from models.users import CreateUser
from utils.database import get_db


router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
def get_users(db: Session = Depends(get_db)):
    db_users = db.query(User).all()

    return JSONResponse(
        content=[
            {"email": db_user.email, "password": db_user.password, "name": db_user.name}
            for db_user in db_users
        ],
        status_code=200,
    )


@router.post("")
def create_user(create_user: CreateUser, db: Session = Depends(get_db)):
    user = User(
        email=create_user.email, password=create_user.password, name=create_user.name
    )

    db.add(user)
    db.commit()

    user_created = db.query(User).filter(User.email == create_user.email)[0]

    return JSONResponse(
        content={
            "email": user_created.email,
            "password": user_created.password,
            "name": user_created.name,
        },
        status_code=201,
    )
