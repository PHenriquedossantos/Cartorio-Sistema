from src.models.cliente_db import Cliente as ClienteDB
from src.models.cliente import Cliente
from src.database.dbconfig import session


class ClienteCore:
    def create_cliente(self, cliente: Cliente):
        with session:
            new_cliente = ClienteDB(**cliente.dict())
            session.add(new_cliente)
            session.commit()
            return new_cliente

    def listar_clientes(self):
        with session:
            clientes = session.query(ClienteDB).all()
            return clientes

    def delete_cliente(self, id: str):
        with session:
            cliente = session.query(ClienteDB).filter(ClienteDB.id == id).first()
            if not cliente:
                return False
            session.delete(cliente)
            session.commit()
