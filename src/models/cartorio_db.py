from sqlalchemy import Column, String, UUID
from src.database.dbconfig import Base

class Cartorio(Base):
    __tablename__ = 'registry'
    __table_args__ = {'schema': 'principal'}

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    cnj = Column(String, unique=True, nullable=False)
    cnpj = Column(String, unique=True)
    notary = Column(String, nullable=False)
    notary_sub = Column(String, nullable=False)
    address = Column(String, nullable=False)
    clerk = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    phone_2 = Column(String)
    mail = Column(String)


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.nome_fantasia,
            "cnpj": self.cnpj,
            "notary": self.notary,
            "notary_sub": self.notary_sub,
            "address": self.address,
            "clerk": self.clerk,
            "cnj": self.cnj,
            "mail": self.mail,
            "phone": self.phone,
            "phone_2": self.phone_2
        }