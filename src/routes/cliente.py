from fastapi import APIRouter, status
from src.models.cliente import Cliente 
from src.core.cliente import ClienteCore

api_router = APIRouter(prefix='/cliente')

@api_router.get('', status_code=status.HTTP_200_OK)
def listar_clientes():
    cliete_core = ClienteCore()
    clientes = cliete_core.listar_clientes()
    return clientes

@api_router.post('', status_code=status.HTTP_201_CREATED)
async def adicionar_cliente(cliente: Cliente):
    cliente_core = ClienteCore()
    cliente_core.create_cliente(cliente)
    return True