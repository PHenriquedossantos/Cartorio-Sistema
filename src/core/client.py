from src.models.client_db import Client as ClientDB
from src.models.client import Client
from src.database.dbconfig import session
from src.errors.user_not_found_exception import UserNotFoundException
from src.models.update_client import UpdateClient

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

    def update_client(self, id: str, update_user: UpdateClient) -> ClientDB:
        with session:
            user = session.query(ClientDB).filter(ClientDB.id == id).first()

            if not user:
                raise UserNotFoundException

            for key, value in update_user.dict().items():
                if value:
                    setattr(user, f"{key}", value)

            session.commit()

            return user