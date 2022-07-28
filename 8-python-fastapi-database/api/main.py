from fastapi import FastAPI

from routes import users


app = FastAPI()

app.include_router(users.router)


@app.get("/ping", tags=["ping"])
async def ping():
    return {"ping": "pong"}
