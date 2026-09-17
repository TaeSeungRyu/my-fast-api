from fastapi import HTTPException


users = [
    {"id": 1, "name": "kim", "age": 30},
    {"id": 2, "name": "lee", "age": 25},
]


def get_users():
    return users


def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


def create_user(name: str, age: int):

    new_user = {
        "id": len(users) + 1,
        "name": name,
        "age": age
    }

    users.append(new_user)

    return new_user