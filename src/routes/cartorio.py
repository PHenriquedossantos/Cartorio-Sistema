from fastapi import APIRouter
from src.models.cartorio import Cartorio 
from src.core.cartorio import CartorioCore

api_router = APIRouter(prefix='/cartorio')

@api_router.post('', status_code=201)
async def adicionar_cartorio(cartorio: Cartorio):
    cartorio_core = CartorioCore()
    cartorio_core.create_cartorio(cartorio)
    return True


@api_router.get('')
def listar_cartorios():
    cartorio_core = CartorioCore()
    cartorios = cartorio_core.listar_cartorio()
    return cartorios

@api_router.delete('/{id}')
def delete_cartorio(id: str):
    cartorio_core = CartorioCore()
    cartorio = cartorio_core.delete_cartorio(id)
    return cartorio