from fastapi import APIRouter, Response, status
from src.models.recibo import Recibo
from src.core.recibo import ReciboCore
from src.static.messages import DELETE_SUCESS, NOT_FOUND

api_router = APIRouter(prefix='/recibo')

@api_router.get('', status_code=status.HTTP_200_OK)
def listar_recibos():
    recibo_core = ReciboCore()
    recibos = recibo_core.listar_recibos()
    return recibos

@api_router.post('', status_code=status.HTTP_201_CREATED)
def adicionar_recibo(recibo: Recibo):
    recibo_core = ReciboCore()
    recibo_core.create_recibo(recibo)
    return recibo

@api_router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_recibo(id: str, response: Response):
    recibo_core = ReciboCore()
    recibo = recibo_core.delete_recibo(id)
    if not recibo:
        response.status_code = status.HTTP_404_NOT_FOUND
        return NOT_FOUND.format('Recibo')
    return DELETE_SUCESS.format('Recibo')