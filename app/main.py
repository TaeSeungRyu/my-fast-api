from fastapi import FastAPI
from pydantic import BaseModel
from app.exception_handler import PlcException, plc_exception_handler

app = FastAPI(title="FastAPI Practice")

# 전역 Exception 등록
app.add_exception_handler(
    PlcException,
    plc_exception_handler,
)



class PlcCommand(BaseModel):
    device_id: int
    running: bool


@app.get("/")
def root():
    return {"message": "Hello FastAPI!"}


@app.get("/plc/status")
def get_plc_status():
    # 실제 PLC 대신 연습용 고정 데이터
    return {
        "connected": True,
        "temperature": 68.2,
        "speed": 1500,
    }


@app.get("/plc/{device_id}")
def get_plc(device_id: int):

    print("device_id",device_id)

    if device_id <= 0:
        raise PlcException(
            "잘못된 PLC 번호입니다.",
            400,
        )
    
    if device_id == 999:
        raise PlcException(
            "PLC 연결 실패",
            503,
        )
    return {"device_id": device_id, "status": "RUNNING"}


@app.post("/plc/command")
def send_command(command: PlcCommand):
    return {
        "message": "Command received",
        "device_id": command.device_id,
        "running": command.running,
    }


@app.get("/plc")
def get_plcs(status: str = "ALL"):
    return {
        "status": status,
        "devices": [
            {"device_id": 1, "name": "PLC-A"},
            {"device_id": 2, "name": "PLC-B"},
        ],
    }