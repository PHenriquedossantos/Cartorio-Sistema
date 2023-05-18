from pydantic import BaseModel


class Emolument(BaseModel):
    codigo: str
    descricao: str = ""
    tipo_servico: str = ""
    tipo_selo: str
    emolumentos: str
    fermoju: float = 0.0
    valor_selo: float = 0.0
    subtotal: float = 0.0
    faadep: float = 0.0
    frmmp: float = 0.0
    total: float = 0.0
    limite: float = 0.0
    limete_excedente: float = 0.0
    valor_por_excedente: float = 0.0
    parcela_excedente: float = 0.0
