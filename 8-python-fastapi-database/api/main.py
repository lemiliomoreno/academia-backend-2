from fastapi import FastAPI

from routes import users
from models.users import Base
from utils.database import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)


@app.get("/ping", tags=["ping"])
async def ping():
    return {"ping": "pong"}
