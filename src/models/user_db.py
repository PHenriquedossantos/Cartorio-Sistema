from sqlalchemy import Column, String, UUID
from src.database.dbconfig import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'principal'}

    id = Column(UUID, primary_key=True)
    name = Column(String)
    login = Column(String, unique=True)
    password = Column(String)
    recibos = relationship('Recibo', back_populates='atendente', cascade='all, delete-orphan')


    