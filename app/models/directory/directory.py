from sqlalchemy import (
    Column,
    Integer,
    String,
)
from app.database import Base


class Directory(Base):
    __tablename__ = 'directory'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    address = Column(String)
    district = Column(String)
