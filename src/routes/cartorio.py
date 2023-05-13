from fastapi import APIRouter, Response, status
from src.models.cartorio import Cartorio 
from src.core.cartorio import CartorioCore
from src.static.messages import DELETE_SUCESS

api_router = APIRouter(prefix='/cartorio')

@api_router.post('', status_code=status.HTTP_201_CREATED)
async def adicionar_cartorio(cartorio: Cartorio):
    cartorio_core = CartorioCore()
    cartorio_core.create_cartorio(cartorio)
    return True


@api_router.get('', status_code=status.HTTP_200_OK)
def listar_cartorios():
    cartorio_core = CartorioCore()
    cartorios = cartorio_core.listar_cartorio()
    return cartorios

@api_router.delete('/{id}')
def delete_cartorio(id: str, response: Response):
    cartorio_core = CartorioCore()
    if not cartorio_core.delete_cartorio(id):
        response.status_code = status.HTTP_404_NOT_FOUND
    return DELETE_SUCESS.format('Cartório')