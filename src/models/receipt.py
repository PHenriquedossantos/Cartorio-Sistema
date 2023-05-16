from pydantic import BaseModel
from uuid import uuid4

class Receipt(BaseModel):
    id: str = uuid4().hex
    client_id: str
    user_id: str
    date: str
    resume: str = ''
    representative_name: str
