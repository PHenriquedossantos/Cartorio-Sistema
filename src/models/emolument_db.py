from sqlalchemy import Column, String, Integer, Float
from src.database.dbconfig import Base


class Emolument(Base):
    __tablename__ = 'emoluments'
    __table_args__ = {'schema': 'principal'}

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




