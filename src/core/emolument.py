from src.database.dbconfig import session
from src.models.emolument_db import Emolument as EmolumentDB
from src.models.emolument import Emolument


class EmolumentCore:
    def create_emolument(self, emolument: Emolument):
        with session:
            new_emolument = EmolumentDB(**emolument.dict())
            session.add(new_emolument)
            session.commit()
            return new_emolument

    def list_emoluments(self):
        with session:
            emoluments = session.query(EmolumentDB).all()
            return emoluments
