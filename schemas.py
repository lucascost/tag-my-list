from pydantic import BaseModel


class ListBase(BaseModel):
    title: str


class ListCreate(ListBase):
    pass


class List(ListBase):
    id: int

    class Config:
        orm_mode = True