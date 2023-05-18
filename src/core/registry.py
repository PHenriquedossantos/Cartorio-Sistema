from src.models.registry import Registry
from src.models.registry_db import Registry as RegistryDB
from src.database.dbconfig import session


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
