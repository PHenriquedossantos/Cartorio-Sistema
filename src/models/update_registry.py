from pydantic import BaseModel

class UpdateRegistry(BaseModel):
    name: str | None = ''
    cnj: str | None = ''
    cnpj: str | None = ''
    notary: str | None = ''
    notary_sub: str | None = ''
    address: str | None = ''
    clerk: str | None = ''
    phone: str | None = ''
    phone_2: str | None = ''
    mail: str | None = ''


