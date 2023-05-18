from src.models.client_db import Client as ClientDB
from src.models.client import Client
from src.database.dbconfig import session


class ClientCore:
    def create_client(self, client: Client):
        with session:
            new_client = ClientDB(**client.dict())
            session.add(new_client)
            session.commit()
            return new_client

    def list_clients(self):
        with session:
            clients = session.query(ClientDB).all()
            return clients

    def delete_client(self, id: str):
        with session:
            client = session.query(ClientDB).filter(ClientDB.id == id).first()
            if not client:
                return False
            session.delete(client)
            session.commit()
