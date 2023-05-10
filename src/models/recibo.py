from pydantic import BaseModel
from uuid import uuid4
from src.models.tabela_emol import Servico
from src.models.cliente import Cliente
from src.models.user import User

class Recibo(BaseModel):
    id: str = uuid4().hex
    #atendimento_id: str
    servicos: list[Servico]
    cliente: Cliente
    atendente: User
    data: str
    resumo: str = ''
