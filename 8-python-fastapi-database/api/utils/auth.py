import os

from fastapi import Header
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.database import User
from utils.database import get_db
from utils.exceptions import Unauthorized


POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOSTNAME = os.getenv("POSTGRES_HOSTNAME")


def authenticate(token: str = Header(...)):
    engine = create_engine(
        f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:5432/{POSTGRES_DB}"
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db = SessionLocal()

    token = db.query(User).filter(User.token == token).first()

    if token is None:
        raise Unauthorized("Invalid authentication token.")
