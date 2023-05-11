from pydantic import BaseModel
from uuid import uuid4

class Cliente(BaseModel):
    id: str = uuid4().hex
    nome_cliente: str
    cpf: str
    endereco: str
    contato: str
    contato_2: str | None = None 
    email: str | None = None