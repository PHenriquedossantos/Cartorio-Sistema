from pydantic import BaseModel, Field
from uuid import uuid4


class Receipt(BaseModel):
    id: str = uuid4().hex
    client_id: str
    user_id: str
    date: str
    resume: str = ""
    representative_name: str
    emoluments: dict[str, int] = Field(default_factory=dict)
