from fastapi import APIRouter, status
from src.models.client import Client
from src.core.client import ClientCore

api_router = APIRouter(prefix='/client')

@api_router.get('', status_code=status.HTTP_200_OK)
def list_clients():
    client_core = ClientCore()
    clients = client_core.list_clients()
    return clients

@api_router.post('', status_code=status.HTTP_201_CREATED)
async def add_client(client: Client):
    client_core = ClientCore()
    client_core.create_client(client)
    return True