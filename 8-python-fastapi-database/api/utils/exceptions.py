from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


class DuplicateRecord(Exception):
    def __init__(self, detail):
        self.detail = detail


class Unauthorized(Exception):
    def __init__(self, detail):
        self.detail = detail


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "type": "bad_request",
            "title": "Bad Request",
            "detail": "The payload is not valid.",
            "status": 400,
        },
    )


async def duplicate_record_exception_handler(request: Request, exc: DuplicateRecord):
    return JSONResponse(
        status_code=409,
        content={
            "type": "duplicate_record",
            "title": "Duplicate Record",
            "detail": exc.detail,
            "status": 409,
        },
    )


async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "type": "internal_server_error",
            "title": "Internal Server Error",
            "detail": "There was an error processing your request.",
            "status": 500,
        },
    )


async def unauthorized_handler(request: Request, exc: Unauthorized):
    return JSONResponse(
        status_code=401,
        content={
            "type": "unauthorized",
            "title": "Unauthorized",
            "detail": exc.detail,
            "status": 401,
        },
    )
