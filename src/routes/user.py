from fastapi import APIRouter
from src.models.user import User
from src.core.user import UserCore

api_router = APIRouter(prefix='/user')

@api_router.post('')
def create_user(user: User):
    user_core = UserCore()
    new_user = user_core.create_user(user)
    return new_user

@api_router.delete('/{id}')
def delete_user(id: str):
    user_core = UserCore()
    if user_core.delete_user(id):

        return True
    return False

@api_router.get('')
def list_users():
    user_core = UserCore()
    users = user_core.list_users()
    return users
