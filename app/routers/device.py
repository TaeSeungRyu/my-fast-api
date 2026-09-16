from fastapi import APIRouter

router = APIRouter(
    prefix="/devices",
    tags=["Device"]
)


@router.get("")
def get_devices():
    return [
        {"id": 1, "name": "Device-A", "running": True},
        {"id": 2, "name": "Device-B", "running": False},
    ]


@router.get("/{device_id}")
def get_device(device_id: int):
    return {
        "id": device_id,
        "name": f"Device-{device_id}",
        "running": True
    }