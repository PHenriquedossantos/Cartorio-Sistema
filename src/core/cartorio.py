from src.models.cartorio import Cartorio
from src.models.cartorio_db import Cartorio as CartorioDB
from src.database.dbconfig import session

class CartorioCore():
    def create_cartorio(self, cartorio: Cartorio):
        with session:
            new_cartorio = CartorioDB(**cartorio.dict())
            session.add(new_cartorio)
            session.commit()
            return new_cartorio
        
    def listar_cartorio(self):
        with session:
            cartorios = session.query(CartorioDB).all()
            return cartorios
        
    def delete_cartorio(self, id: str):
        with session:
            cartorio = session.query(CartorioDB).filter(CartorioDB.id == id).first()
            if not cartorio:
                return False
            session.delete(cartorio)
            session.commit()
            return True