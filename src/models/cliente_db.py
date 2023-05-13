from sqlalchemy import Column, String, UUID
from src.database.dbconfig import Base
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = 'dados_cliente'
    __table_args__ = {'schema': 'principal'}

    id = Column(UUID, primary_key=True)
    cpf = Column(String, unique=True)
    nome_cliente = Column(String)
    endereco = Column(String)
    contato = Column(String)
    contato_2 = Column(String)
    email = Column(String)

    recibos = relationship('Recibo', back_populates='cliente', cascade='all, delete-orphan')



