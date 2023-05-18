from pydantic import BaseModel

class UpdateUser(BaseModel):
    name: str | None = ''
    login: str | None = ''
    password: str | None = ''
