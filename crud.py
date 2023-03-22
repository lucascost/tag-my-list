from typing import Union

from sqlalchemy.orm import Session

import models
import schemas

# LIST
def get_list(db: Session, list_info: Union[int, str]):
    if type(list_info) == int:
        return db.query(models.List).filter(models.List.id == list_info).first()

    return db.query(models.List).filter(models.List.title == list_info).first()

def get_lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.List).offset(skip).limit(limit).all()

def create_list(db: Session, list: schemas.ListCreate):
    db_list = models.List(title=list.title, type_id=list.type_id)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list


# LIST_TYPE
def get_list_type(db: Session, list_type_id: int):
    return db.query(models.ListType).filter(models.ListType.id == list_type_id).first()

def get_list_types(db: Session, skip: int = 0, limit: int = 3):
    return db.query(models.ListType).offset(skip).limit(limit).all()