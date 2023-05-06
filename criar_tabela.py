from src.database.dbconfig import Base, engine
from src.models.cartorio_db import Cartorio

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
