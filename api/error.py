from typing import Callable, Any

from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse


class KawaiiException(Exception):
    pass


class InvalidToken(KawaiiException):
    pass


class ServerError(KawaiiException):
    pass


def create_exception_handler(
    status_code: int, details: Any
) -> Callable[[Request, Exception], JSONResponse]:

    async def except_handler(request: Request, exception: KawaiiException):
        return JSONResponse(content=details, status_code=status_code)

    return except_handler


def register_handler(app: FastAPI):
    app.add_exception_handler(
        InvalidToken,
        create_exception_handler(
            status_code=status.HTTP_400_BAD_REQUEST,
            details={
                "message": "User with email already exists.",
                "error_code": "invalid_token",
            },
        ),
    )

    @app.exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR)
    async def intername_server_error():
        ServerError,
        create_exception_handler(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details={
                "message": "Oh hu, Something went wrong. Please try again later.",
                "error_code": "internal_server_error",
            },
        )
