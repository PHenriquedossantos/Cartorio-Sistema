from src.database.dbconfig import Base, engine
# from src.models.receipt_emolument_association import ReceiptEmolumentAssociation


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
