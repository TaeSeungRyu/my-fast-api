from fastapi import Request
from fastapi.responses import JSONResponse
from app.logger import logger

class PlcException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code

async def plc_exception_handler(
    request: Request,
    exc: PlcException
):
    print("request",request.body, request.headers)
    logger.exception(
        "Unhandled error: %s %s",
        request.method,
        request.url.path
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
        },
    )        