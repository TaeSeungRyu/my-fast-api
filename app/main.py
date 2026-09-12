from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Practice")


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

    if device_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="device_id는 1 이상이어야 합니다."
        )

    if device_id == 999:
        raise HTTPException(
            status_code=404,
            detail="PLC를 찾을 수 없습니다."
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