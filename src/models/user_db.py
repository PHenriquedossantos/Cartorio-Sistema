from sqlalchemy import Column, String, UUID
from src.database.dbconfig import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'principal'}

    id = Column(UUID, primary_key=True)
    name = Column(String)
    login = Column(String, unique=True)
    password = Column(String)