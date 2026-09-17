from fastapi import APIRouter
from pydantic import BaseModel

from app.services import user_service


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


class User(BaseModel):
    name: str
    age: int


@router.get("")
def get_users():
    return user_service.get_users()


@router.get("/{user_id}")
def get_user(user_id: int):
    return user_service.get_user(user_id)


@router.post("")
def create_user(user: User):
    return user_service.create_user(
        user.name,
        user.age
    )