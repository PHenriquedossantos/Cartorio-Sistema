from sqlalchemy import Column, String, UUID
from src.database.dbconfig import Base
from sqlalchemy.orm import relationship
from bcrypt import hashpw, checkpw, gensalt


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "principal"}

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    login = Column(String, unique=True)
    password = Column(String, nullable=False)

    receipts = relationship(
        "Receipt", back_populates="user", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {"id": self.id, "name": self.name, "login": self.login}

    @staticmethod
    def hash_password(password: str):
        password = password.encode("utf-8")
        return hashpw(password, gensalt(8))

    @staticmethod
    def check_password(self, password: str):
        return checkpw(
            password=password.encode("utf-8"),
            hashed_password=self.password.encode("utf8"),
        )
