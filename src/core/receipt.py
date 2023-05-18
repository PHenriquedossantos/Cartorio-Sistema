from src.models.receipt import Receipt
from src.models.receipt_db import Receipt as ReceiptDB
from src.models.emolument_db import Emolument
from src.models.receipt_emolument_association import ReceiptEmolumentAssociation
from src.database.dbconfig import session


class ReceiptCore:
    def create_receipt(self, receipt: Receipt):
        with session:
            receipt_dto = receipt.dict()
            emoluments = receipt_dto.pop("emoluments")
            emoluments_ids = [key for key, _ in emoluments.items()]
            emoluments_db = session.query(Emolument).filter(
                Emolument.codigo.in_(emoluments_ids)
            )

            new_receipt = ReceiptDB(**receipt_dto)

            associations = []
            for emolument in emoluments_db:
                associations.append(
                    ReceiptEmolumentAssociation(
                        receipt=new_receipt,
                        emolument=emolument,
                        qtd=emoluments[emolument.codigo],
                    )
                )

            new_receipt.emoluments = associations
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
