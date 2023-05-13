from sqlalchemy import Column, String, UUID
from src.database.dbconfig import Base

class Cartorio(Base):
    __tablename__ = 'cartorios'
    __table_args__ = {'schema': 'principal'}

    id = Column(UUID, primary_key=True)
    nome_fantasia = Column(String)
    cnpj = Column(String, unique=True)
    tabeliao = Column(String)
    tabeliao_substituto = Column(String)
    endereco = Column(String)
    escrevente = Column(String)
    telefone = Column(String)
    telefone2 = Column(String)
    email = Column(String)
    cnj = Column(String, unique=True)


    def to_dict(self):
        return {
            "id": self.id,
            "nome_fantasia": self.nome_fantasia,
            "cnpj": self.cnpj,
            "tabeliao": self.tabeliao,
            "tabeliao_substituto": self.tabeliao_substituto,
            "endereco": self.endereco,
            "escrevente": self.escrevente,
            "telefone": self.telefone,
            "cnj": self.cnj
        }