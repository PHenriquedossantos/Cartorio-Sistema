from src.models.receipt import Receipt
from src.models.receipt_db import Receipt as ReceiptDB
from src.database.dbconfig import session

class ReceiptCore():
    def create_receipt(self, receipt: Receipt):
        with session:
            new_receipt = ReceiptDB(**receipt.dict())
            session.add(new_receipt)
            session.commit()
            return new_receipt

    def list_receipts(self):
        with session:
            receipts = session.query(ReceiptDB).all()
            return receipts

    def delete_receipt(self, id: str):
        with session:
            receipt = session.query(ReceiptDB).filter(ReceiptDB.id == id).first()
            if not receipt:
                return False
            session.delete(receipt)
            session.commit()
            return True
