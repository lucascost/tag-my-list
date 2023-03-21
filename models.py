from sqlalchemy import Column, Integer, String

from database import Base

class List(Base):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
