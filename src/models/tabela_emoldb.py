from sqlalchemy import Column, String, Integer, Float
from src.database.dbconfig import Base


class TabelaEmol(Base):
    __tablename__ = 'tabela_emol'
    __table_args__ = {'schema': 'principal'}

    codigo_ato = Column(String, primary_key=True)
    descricao_ato = Column(String)
    tabela = Column(String)
    item = Column(String, primary_key=True)
    documento = Column(String)
    quantidade = Column(Integer)
    desconto = Column(Float)
    valor = Column(Float)
    custas = Column(Float)
    fermoju = Column(Float)
    selo = Column(Float)
    faadep = Column(Float)
    frmp = Column(Float)
    outros = Column(Float)
    iss = Column(Float)
    total = Column(Float)
    data = Column(String)
    livro = Column(Integer)
    folha = Column(Integer)
    ordem = Column(Integer)

