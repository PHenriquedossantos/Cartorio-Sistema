from fastapi import APIRouter, status, Response
from src.models.client import Client
from src.core.client import ClientCore
from src.models.update_client import UpdateClient

from src.errors.user_not_found_exception import UserNotFoundException
from src.static.messages import NOT_FOUND, INTERNAL_ERROR

api_router = APIRouter(prefix="/client")


@api_router.get("", status_code=status.HTTP_200_OK)
def list_clients():
    client_core = ClientCore()
    clients = client_core.list_clients()
    return clients


@api_router.post("", status_code=status.HTTP_201_CREATED)
async def add_client(client: Client):
    client_core = ClientCore()
    client_core.create_client(client)
    return True

@api_router.put("/{id}")
def update_user(id: str, client: UpdateClient, response: Response):
    client_core = ClientCore()
    try:
        return client_core.update_client(id, client)
    except UserNotFoundException:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": NOT_FOUND.format("Client")}
    except Exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": INTERNAL_ERROR}