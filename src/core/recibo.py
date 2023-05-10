from src.models.recibo import Recibo
from src.models.recibo_db import Recibo as ReciboDB
from src.database.dbconfig import session

class ReciboCore():
    def create_recibo(self, recibo: Recibo):
        with session:
            new_recibo = ReciboDB(**recibo.dict())
            session.add(new_recibo)
            session.commit()
            return new_recibo

    def listar_recibos(self):
        with session:
            recibos = session.query(ReciboDB).all()
            return recibos

    def delete_recibo(self, id: str):
        with session:
            recibo = session.query(ReciboDB).filter(ReciboDB.id == id).first()
            if not recibo:
                return False
            session.delete(recibo)
            session.commit()
            return True
