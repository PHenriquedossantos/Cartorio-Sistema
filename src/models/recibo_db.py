from sqlalchemy import Column, String, UUID, ForeignKey, DateTime, Text
from src.database.dbconfig import Base
from sqlalchemy.orm import relationship

class Recibo(Base):
    __tablename__ = 'recibos'
    __table_args__ = {'schema': 'principal'}

    id = Column(UUID, primary_key=True)
    #atendimento_id = Column(UUID, ForeignKey(''))
    #servicos = relationship()
    nome_apresentante = Column(String)
    data = Column(DateTime)
    atendente_id = Column(UUID, ForeignKey('users.id'))
    resumo = Column(Text)
    cliente_id = Column(UUID, ForeignKey('dados_cliente.id'), nullable=False)

    cliente = relationship('Cliente', back_populates='recibos', cascade='all')
    atendente = relationship('User', back_populates='recibos', cascade='all')
    
    

    def to_dict(self):
        return {
            "id": self.id,
            "atendimento_id": self.atendimento_id,
            "servicos": self.servicos,
            "dados_cliente": self.dados_cliente
        }