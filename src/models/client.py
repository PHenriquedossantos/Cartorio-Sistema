from pydantic import BaseModel
from uuid import uuid4


class Client(BaseModel):
    id: str = uuid4().hex
    name: str
    document: str
    address: str
    phone: str
    phone_2: str | None = None
    mail: str | None = None
