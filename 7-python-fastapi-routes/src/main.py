from fastapi import FastAPI

from routes import users, pets


app = FastAPI()

app.include_router(users.router)
app.include_router(pets.router)


@app.get("/ping", tags=["ping"])
async def ping():
    return {"ping": "pong"}
