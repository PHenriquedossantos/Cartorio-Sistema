from fastapi import FastAPI

from src.models.user import User
from src.core.user import UserCore

app = FastAPI()

users: list[User] = []

@app.post('/user')
def create_user(user: User):
    user_core = UserCore()
    new_user = user_core.create_user(user)
    return new_user

@app.delete('/user/{id}')
def delete_user(id: str):
    user_core = UserCore()
    if user_core.delete_user(id):

        return True
    return False

@app.get('/user')
def list_users():
    user_core = UserCore()
    users = user_core.list_users()
    return users