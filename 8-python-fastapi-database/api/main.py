from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from routes import users
from utils.exceptions import DuplicateRecord, validation_exception_handler, duplicate_record_exception_handler, exception_handler


app = FastAPI()

app.include_router(users.router)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(DuplicateRecord, duplicate_record_exception_handler)
app.add_exception_handler(Exception, exception_handler)


@app.get("/ping", tags=["ping"])
async def ping():
    return {"ping": "pong"}
