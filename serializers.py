from pydantic import BaseModel

from models import List


class ListSerializer(BaseModel):
    id: int
    title: str
    type: str

    class Config:
        orm_mode = True

def serialize_list(list: List):
    return {
        'id': list.id,
        'title': list.title,
        'type': list.type.name
    }