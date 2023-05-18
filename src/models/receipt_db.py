from sqlalchemy import Column, String, UUID, ForeignKey, DateTime, Text
from sqlalchemy.sql import func
from src.database.dbconfig import Base
from sqlalchemy.orm import relationship
from src.models.receipt_emolument_association import ReceiptEmolumentAssociation
from src.models.emolument_db import Emolument


class Receipt(Base):
    __tablename__ = "receipt"
    __table_args__ = {"schema": "principal"}

    id = Column(UUID, primary_key=True)
    client_id = Column(UUID, ForeignKey("principal.client.id"), nullable=False)
    representative_name = Column(String, nullable=False)
    user_id = Column(UUID, ForeignKey("principal.user.id"))
    date = Column(DateTime, server_default=func.now())
    resume = Column(Text)

    client = relationship("Client", back_populates="receipts", cascade="all")
    user = relationship("User", back_populates="receipts", cascade="all")
    emoluments = relationship(
        "ReceiptEmolumentAssociation", back_populates="receipt", cascade="all"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "representative_name": self.representative_name,
            "date": self.date,
            "resume": self.resume,
        }
