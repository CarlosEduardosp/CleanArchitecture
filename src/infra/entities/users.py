from sqlalchemy import Column, String, Integer
from src.infra.config import Base
from sqlalchemy.orm import relationship


class Users(Base):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id_pet = relationship("Pets")

    def __rep__(self):
        return f"Usr [name={self.name}]"
