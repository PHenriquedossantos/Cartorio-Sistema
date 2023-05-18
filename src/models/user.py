from pydantic import BaseModel
from uuid import uuid4


class User(BaseModel):
    id: str = uuid4().hex
    name: str
    login: str
    password: str
