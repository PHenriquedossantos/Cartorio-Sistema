from pydantic import BaseModel

class Cliente(BaseModel):
    apresentante: str
    cliente: str
    cpf: str
    endereco: str
    contato: str
    contato2: str | None = None 
    email: str | None = None