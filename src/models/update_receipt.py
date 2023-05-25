from pydantic import BaseModel, Field

class UpdateReceipt(BaseModel):
    client_id: str | None = ''
    user_id: str | None = ''
    date: str | None = ''
    resume: str | None = ''
    representative_name: str | None = ''
    emoluments: dict[str, int] = Field(default_factory=dict)



