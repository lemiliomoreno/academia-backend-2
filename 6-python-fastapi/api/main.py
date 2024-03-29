import os

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Boolean, Column, Integer, String
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# load environment variables

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOSTNAME = os.getenv("POSTGRES_HOSTNAME")

# db tables

engine = create_engine(
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:5432/{POSTGRES_DB}"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


Base.metadata.create_all(bind=engine)


# models


class CreateUser(BaseModel):
    email: str
    hashed_password: str
    is_active: bool


app = FastAPI()


@app.get("/ping")
def ping():
    return {"ping": "pong1"}


@app.post("/users")
def create_user(user: CreateUser):
    db_user = User(
        email=user.email, hashed_password=user.hashed_password, is_active=user.is_active
    )

    with Session(engine) as session:
        session.add(db_user)
        session.commit()

    print(db_user)
    return {"ping": user}


@app.get("/users")
def get_users():
    with Session(engine) as session:
        users = session.query(User).all()

    emails = []

    for user in users:
        emails.append(user.email)

    return {"users": emails}
