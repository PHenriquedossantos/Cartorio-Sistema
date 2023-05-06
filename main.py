from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.database.dbconfig import session
from src.models.user import User
from src.models.cartorio import Cartorio
from src.core.user import UserCore
from src.core.cartorio import CartorioCore



app = FastAPI()

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


@app.post('/cartorio', status_code=200)
async def adicionar_cartorio(cartorio: Cartorio):
    cartorio_core = CartorioCore()
    cartorio_core.create_cartorio(cartorio)
    return True


@app.get('/cartorio')
def listar_cartorios():
    cartorio_core = CartorioCore()
    cartorios = cartorio_core.listar_cartorio()
    return cartorios

@app.delete('/cartorio/{id}')
def delete_cartorio(id: str):
    cartorio_core = CartorioCore()
    cartorio = cartorio_core.delete_cartorio(id)
    return cartorio