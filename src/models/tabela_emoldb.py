from sqlalchemy import Column, String, Integer, Float
from src.database.dbconfig import Base


class TabelaEmol(Base):
    __tablename__ = 'tabela_emol'
    __table_args__ = {'schema': 'principal'}

    codigo = Column(String, primary_key=True)
    descricao = Column(String)
    tipo_servico = Column(String, nullable=False)
    tipo_selo = Column(String)
    emolumentos = Column(String, primary_key=True)
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




