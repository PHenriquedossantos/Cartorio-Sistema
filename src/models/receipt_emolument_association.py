from sqlalchemy import Column, UUID, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from src.database.dbconfig import Base


class ReceiptEmolumentAssociation(Base):
    __tablename__ = "receipt_emolument"
    __table_args__ = {"schema": "principal"}

    receipt_id = Column(UUID, ForeignKey("principal.receipt.id"), primary_key=True)
    emolument_id = Column(
        String, ForeignKey("principal.emolument.codigo"), primary_key=True
    )
    qtd = Column(Integer)

    emolument = relationship("Emolument", back_populates="receipts")
    receipt = relationship("Receipt", back_populates="emoluments")
