from fastapi import APIRouter, Response, status
from src.models.registry import Registry
from src.core.registry import RegistryCore
from src.models.update_registry import UpdateRegistry
from src.static.messages import DELETE_SUCESS

from src.errors.user_not_found_exception import UserNotFoundException
from src.static.messages import NOT_FOUND, INTERNAL_ERROR

api_router = APIRouter(prefix="/registry")


@api_router.get("", status_code=status.HTTP_200_OK)
def list_registries():
    registry_core = RegistryCore()
    registries = registry_core.list_registries()
    return registries

@api_router.post("", status_code=status.HTTP_201_CREATED)
async def add_registry(registry: Registry):
    registry_core = RegistryCore()
    registry_core.create_registry(registry)
    return True

@api_router.put("/{id}")
def update_registry(id: str, registry: UpdateRegistry, response: Response):
    user_registry = RegistryCore()
    try:
        return user_registry.update_registry(id, registry)
    except UserNotFoundException:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": NOT_FOUND.format("Registry")}
    except Exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": INTERNAL_ERROR}

@api_router.delete("/{id}")
def delete_registry(id: str, response: Response):
    registry_core = RegistryCore()
    if not registry_core.delete_registry(id):
        response.status_code = status.HTTP_404_NOT_FOUND
    return DELETE_SUCESS.format("Cartório")



