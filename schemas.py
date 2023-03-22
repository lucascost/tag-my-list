from pydantic import BaseModel


# LIST

class ListBase(BaseModel):
    title: str

class ListCreate(ListBase):
    type_id: int

class List(ListBase):
    id: int
    type_id: int

    class Config:
        orm_mode = True


# LIST_TYPE
class ListTypeBase(BaseModel):
    name: str

class ListType(ListTypeBase):
    id: int

    class Config:
        orm_mode = True
