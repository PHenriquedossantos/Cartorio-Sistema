from src.models.receipt import Receipt
from src.models.receipt_db import Receipt as ReceiptDB
from src.errors.user_not_found_exception import UserNotFoundException
from src.models.emolument_db import Emolument
from src.models.update_receipt import UpdateReceipt
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
        
    def update_receipt(self, id: str, update_receipt: UpdateReceipt) -> ReceiptDB:
        with session:
            receipt = session.query(ReceiptDB).filter(ReceiptDB.id == id).first()

            if not receipt:
                raise UserNotFoundException
            
            updated_receipt_dict = update_receipt.dict()

            for key, value in updated_receipt_dict.items():
                if key == 'emoluments' and value:
                    updated_emoluments = updated_receipt_dict.get('emoluments')
                    emoluments_ids =  [key for key, _ in updated_emoluments.items()]
                    emoluments_db = session.query(Emolument).filter(Emolument.codigo.in_(emoluments_ids))

                    associations = []
                    for emolument in emoluments_db:
                        associations.append(
                            ReceiptEmolumentAssociation(
                                receipt=receipt,
                                emolument=emolument,
                                qtd=updated_emoluments[emolument.codigo],
                            )
                        )
                
                    updated_emoluments = updated_receipt_dict.get('emoluments')
                    for emolument in receipt.emoluments:
                        session.delete(emolument)
                    receipt.emoluments = associations

                if value and key != 'emoluments':
                    setattr(receipt, f"{key}", value)

            session.commit()

            return receipt
        
   
