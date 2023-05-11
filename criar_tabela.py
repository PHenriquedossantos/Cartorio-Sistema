from src.database.dbconfig import Base, engine
from src.models.cartorio_db import Cartorio
from src.models.user_db import User
from src.models.cliente_db import Cliente
from src.models.recibo_db import Recibo

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
