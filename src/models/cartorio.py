from pydantic import BaseModel
from uuid import uuid4

class Cartorio(BaseModel):
    __tablename__ = 'cartorios'

    id: str = uuid4().hex
    nome_fantasia: str
    cnpj: str
    tabeliao: str
    tabeliao_substituto: str
    endereco: str
    escrevente: str
    telefone: str
    telefone2: str | None = None
    email: str
    cnj: str
