from pydantic import BaseModel

from models import List
from schemas import Tag


class ListSerializer(BaseModel):
    id: int
    title: str
    type: str
    tags: list[Tag]

    class Config:
        orm_mode = True


def serialize_list(list: List):
    return {
        'id': list.id,
        'title': list.title,
        'type': list.type.name,
        'tags': list.tags
    }