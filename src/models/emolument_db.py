from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from src.database.dbconfig import Base
from src.models.receipt_emolument_association import ReceiptEmolumentAssociation


class Emolument(Base):
    __tablename__ = "emolument"
    __table_args__ = {"schema": "principal"}

    codigo = Column(String, primary_key=True)
    descricao = Column(String)
    tipo_servico = Column(String)
    tipo_selo = Column(String)
    emolumentos = Column(String)
    fermoju = Column(String)
    valor_selo = Column(Float)
    subtotal = Column(Float)
    faadep = Column(Float)
    frmmp = Column(Float)
    total = Column(Float)
    limite = Column(Float)
    limete_excedente = Column(Float)
    valor_por_excedente = Column(Float)
    parcela_excedente = Column(Float)

    receipts = relationship(
        "ReceiptEmolumentAssociation", back_populates="emolument", cascade="all"
    )
