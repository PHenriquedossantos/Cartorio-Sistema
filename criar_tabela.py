from src.database.dbconfig import Base, engine
from src.models.emolument_db import Emolument


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
