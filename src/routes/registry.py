from fastapi import APIRouter, Response, status
from src.models.registry import Registry 
from src.core.registry import RegistryCore
from src.static.messages import DELETE_SUCESS

api_router = APIRouter(prefix='/registry')

@api_router.post('', status_code=status.HTTP_201_CREATED)
async def add_registry(registry: Registry):
    registry_core = RegistryCore()
    registry_core.create_registry(registry)
    return True


@api_router.get('', status_code=status.HTTP_200_OK)
def list_registries():
    registry_core = RegistryCore()
    registries = registry_core.list_registries()
    return registries

@api_router.delete('/{id}')
def delete_registry(id: str, response: Response):
    registry_core = RegistryCore()
    if not registry_core.delete_registry(id):
        response.status_code = status.HTTP_404_NOT_FOUND
    return DELETE_SUCESS.format('Cartório')