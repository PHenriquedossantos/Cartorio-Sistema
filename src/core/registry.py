from src.models.registry import Registry
from src.errors.user_not_found_exception import UserNotFoundException
from src.models.registry_db import Registry as RegistryDB
from src.database.dbconfig import session
from src.models.update_registry import UpdateRegistry


class RegistryCore:
    def create_registry(self, registry: Registry):
        with session:
            new_registry = RegistryDB(**registry.dict())
            session.add(new_registry)
            session.commit()
            return new_registry

    def list_registries(self):
        with session:
            registries = session.query(RegistryDB).all()
            return registries

    def delete_registry(self, id: str):
        with session:
            registry = session.query(RegistryDB).filter(RegistryDB.id == id).first()
            if not registry:
                return False
            session.delete(registry)
            session.commit()
            return True


    def update_registry(self, id: str, update_registry: UpdateRegistry) -> RegistryDB:
        with session:
            user = session.query(RegistryDB).filter(RegistryDB.id == id).first()

            if not user:
                raise UserNotFoundException

            for key, value in update_registry.dict().items():
                if value:
                    setattr(user, f"{key}", value)

            session.commit()

            return user