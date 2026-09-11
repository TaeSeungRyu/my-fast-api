from fastapi import FastAPI
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
    return {"device_id": device_id, "status": "RUNNING"}


@app.post("/plc/command")
def send_command(command: PlcCommand):
    return {
        "message": "Command received",
        "device_id": command.device_id,
        "running": command.running,
    }
