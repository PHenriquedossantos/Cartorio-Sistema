from pydantic import BaseModel
from uuid import uuid4
#from src.models.tabela_emol import Servico

class Recibo(BaseModel):
    id: str = uuid4().hex
    #atendimento_id: str
    #servicos: list[Servico]
    cliente_id: str
    atendente_id: str
    data: str
    resumo: str = ''
    nome_apresentante: str
