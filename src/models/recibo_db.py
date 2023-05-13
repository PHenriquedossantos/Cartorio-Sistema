from sqlalchemy import Column, String, UUID, ForeignKey, DateTime, Text
from sqlalchemy.sql import func
from src.database.dbconfig import Base
from sqlalchemy.orm import relationship


class Recibo(Base):
    __tablename__ = 'receipt'
    __table_args__ = {'schema': 'principal'}

    id = Column(UUID, primary_key=True)
    client_id = Column(UUID, ForeignKey('principal.dados_cliente.id'), nullable=False)
    representative_name = Column(String, nullable=False)
    user_id = Column(UUID, ForeignKey('principal.users.id'))
    date = Column(DateTime, server_default=func.now())
    resume = Column(Text)
    client = relationship('Cliente', back_populates='recibos', cascade='all')
    user = relationship('User', back_populates='recibos', cascade='all')

    def to_dict(self):
        return {
            "id": self.id,
            "representative_name": self.representative_name,
            "date": self.date,
            "resume": self.resume
        }