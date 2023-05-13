from pydantic import BaseModel

class Servico(BaseModel):
    codigo_ato: str
    descricao_ato: str
    tabela: str
    item: str
    documento: str
    quantidade: str
    desconto: str
    valor: str
    custas: str
    fermoju: str
    selo: str
    faadep: str
    frmp: str
    outros: str
    iss: str
    total: str
    data: str
    livro: str
    folha: str
    ordem: str