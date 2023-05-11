from fastapi import APIRouter
from src.models.cliente import Cliente 
from src.core.cliente import ClienteCore

api_router = APIRouter(prefix='/cliente')

@api_router.post('', status_code=201)
async def adicionar_cliente(cliente: Cliente):
    cliente_core = ClienteCore()
    cliente_core.create_cliente(cliente)
    return True