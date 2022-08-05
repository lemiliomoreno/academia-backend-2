from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from models.database import User
from models.login import Login
from utils.database import get_db
from utils.exceptions import Unauthorized


router = APIRouter(prefix="", tags=["login"])


@router.post("/login")
async def login(user: Login, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user is None or db_user.password != user.password:
        raise Unauthorized("Bad credentials.")

    return JSONResponse(
        content={"token": db_user.token},
        status_code=200,
    )
