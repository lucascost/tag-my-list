from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

import crud
import models
import schemas
import serializers
from database import engine, SessionLocal
from serializers import serialize_list, ListSerializer

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# LIST
@app.get("/lists/{list_id}", response_model=serializers.ListSerializer)
def read_list(list_id: int, db: Session = Depends(get_db)):
    db_list = crud.get_list(db, list_info=list_id)
    if db_list is None:
        raise HTTPException(status_code=404, detail="List not found")
    return serialize_list(db_list)


@app.get("/", response_model=list[serializers.ListSerializer])
def read_lists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lists = crud.get_lists(db, skip, limit)
    db_lists = []
    for list in lists:
        list.tags = []
        db_lists.append(serialize_list(list))
    return db_lists


@app.post("/", response_model=serializers.ListSerializer)
def create_list(list: schemas.ListCreate, db: Session = Depends(get_db)):
    db_list = crud.get_list(db, list_info=list.title)
    if db_list:
        raise HTTPException(status_code=400, detail="Title already registered")
    new_list = crud.create_list(db=db, list=list)
    return serialize_list(new_list)


# LIST_TYPES

@app.get("/listtypes/", response_model=list[schemas.ListType])
def read_listtypes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_list_types(db, skip, limit)


# TAG
@app.get("/lists/{list_id}/tags", response_model=list[schemas.Tag])
def read_tags_by_list(list_id: int, db: Session = Depends(get_db)):
    db_list = crud.get_list(db, list_id)
    if db_list is None:
        raise HTTPException(status_code=400, detail="List not found")
    db_tags = crud.get_tags_by_list(db, list_id)
    return db_tags


@app.post("/lists/{list_id}/tags", response_model=schemas.Tag)
def create_tag(list_id: int, tag: schemas.TagCreate, db: Session = Depends(get_db)):
    list = read_list(list_id, db)
    return crud.create_tag(db, list['id'], tag)
