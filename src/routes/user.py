from fastapi import APIRouter, Response, status
from src.models.user import User
from src.core.user import UserCore

api_router = APIRouter(prefix="/user")


@api_router.get("", status_code=status.HTTP_200_OK)
def list_users():
    user_core = UserCore()
    users = user_core.list_users()
    return users


@api_router.post("", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    user_core = UserCore()
    user_core.create_user(user)
    return user


@api_router.delete("/{id}")
def delete_user(id: str, response: Response):
    user_core = UserCore()
    if user_core.delete_user(id):
        return True
    response.status_code = status.HTTP_404_NOT_FOUND
    return False
