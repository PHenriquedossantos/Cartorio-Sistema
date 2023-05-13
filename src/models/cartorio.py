from pydantic import BaseModel
from uuid import uuid4

class Cartorio(BaseModel):
    __tablename__ = 'cartorios'

    id: str = uuid4().hex
    name: str
    cnpj: str
    notary: str
    notary_sub: str
    address: str
    clerk: str
    phone: str
    phone_2: str | None = None
    mail: str
    cnj: str
