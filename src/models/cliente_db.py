from sqlalchemy import Column, String, UUID
from src.database.dbconfig import Base
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = 'client'
    __table_args__ = {'schema': 'principal'}

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    document = Column(String, unique=True)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    phone_2 = Column(String)
    mail = Column(String)

    recibos = relationship('Recibo', back_populates='cliente', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "document": self.document,
            "address": self.address,
            "phone": self.phone,
            "phone_2": self.phone_2,
            "mail": self.mail
        }



