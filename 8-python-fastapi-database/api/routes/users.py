from secrets import token_hex

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from psycopg2.errorcodes import UNIQUE_VIOLATION

from models.database import User
from models.users import CreateUser
from utils.database import get_db
from utils.exceptions import DuplicateRecord
from utils.auth import authenticate


router = APIRouter(prefix="/users", tags=["users"])


@router.get("", dependencies=[Depends(authenticate)])
async def get_users(db: Session = Depends(get_db)):
    db_users = db.query(User).all()

    return JSONResponse(
        content=jsonable_encoder(db_users),
        status_code=200,
    )


@router.post("")
async def create_user(create_user: CreateUser, db: Session = Depends(get_db)):
    user = User(
        email=create_user.email, password=create_user.password, name=create_user.name, token=token_hex(16),
    )

    db.add(user)

    try:
        db.commit()

    except IntegrityError as err:
        if err.orig.pgcode == UNIQUE_VIOLATION:
            raise DuplicateRecord(f"User {create_user.email} already exists.")

    user_created = db.query(User).filter(User.email == create_user.email)[0]

    return JSONResponse(
        content=jsonable_encoder(user_created),
        status_code=201,
    )
