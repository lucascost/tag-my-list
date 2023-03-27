from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class List(Base):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    type_id = Column(Integer, ForeignKey("list_types.id", ondelete="CASCADE"))
    type = relationship("ListType")
    tags = relationship("Tag", back_populates="list")


class ListType(Base):
    __tablename__ = 'list_types'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    list_id = Column(Integer, ForeignKey("lists.id", ondelete="CASCADE"))
    list = relationship("List", back_populates="tags")
