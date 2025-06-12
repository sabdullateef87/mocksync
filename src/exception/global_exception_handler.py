from http import HTTPStatus
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import Union
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from src.exception.exception import BaseCustomException

async def global_exception_handler(request: Request, exc: Union[Exception, BaseCustomException]):
    """
    Global exception handler for unhandled exceptions
    Handles both standard exceptions and custom exceptions
    """
    
    if isinstance(exc, BaseCustomException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "statusCode" : exc.status_code,
                "message": exc.message,
                "details": exc.details
            }
        )
    if isinstance(exc, IntegrityError):
        print(exc._message)
        return JSONResponse(
            status_code=HTTPStatus.CONFLICT,
            content={
                "statusCode" : HTTPStatus.CONFLICT,
                "message": "A duplicate scenarios encountered, kindly check the request.",
                # "details": exc._message
            }
        )
                
    
    # Fallback for unexpected exceptions
    return JSONResponse(
        status_code=500,
        content={
            "error": "Unexpected Error",
            "message": str(exc)
        }
    )

async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """
    Handler for HTTP-specific exceptions
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "HTTP Error",
            "message": exc.detail
        }
    )

def setup_exception_handlers(app):
    """
    Utility function to add exception handlers to a FastAPI app
    """
    app.add_exception_handler(Exception, global_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(BaseCustomException, global_exception_handler)