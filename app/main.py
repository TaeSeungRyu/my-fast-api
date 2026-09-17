from fastapi import FastAPI
from app.routers.device import router as device_router
from app.routers.user_router import router as user_router
from app.exception_handler import PlcException, plc_exception_handler
import os

ENV = os.getenv("ENV", "local")

is_prod = ENV == "production"

app = FastAPI(
    docs_url=None if is_prod else "/docs",
    redoc_url=None if is_prod else "/redoc",
    openapi_url=None if is_prod else "/openapi.json",
)

# 전역 Exception 등록
app.add_exception_handler(
    PlcException,
    plc_exception_handler,
)

# router 등록
app.include_router(device_router)
app.include_router(user_router)