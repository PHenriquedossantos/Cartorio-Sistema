from fastapi import APIRouter
from src.models.recibo import Recibo
from src.core.recibo import ReciboCore

api_router = APIRouter(prefix='/recibo')

@api_router.post('', status_code=201)
def adicionar_recibo(recibo: Recibo):
    recibo_core = ReciboCore()
    recibo_core.create_recibo(recibo)
    return {"message": "Recibo criado com sucesso!"}

@api_router.get('')
def listar_recibos():
    recibo_core = ReciboCore()
    recibos = recibo_core.listar_recibos()
    return [recibo.to_dict() for recibo in recibos]

@api_router.delete('/{id}')
def delete_recibo(id: str):
    recibo_core = ReciboCore()
    recibo = recibo_core.delete_recibo(id)
    if recibo:
        return {"message": "Recibo deletado com sucesso!"}
    else:
        return {"message": "Recibo não encontrado!"}