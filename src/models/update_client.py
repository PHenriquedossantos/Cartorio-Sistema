from pydantic import BaseModel

class UpdateClient(BaseModel):
    name: str | None = ''
    document: str | None = ''
    address: str | None = ''
    phone: str | None = ''
    phone_2: str | None = ''
    mail: str | None = ''



