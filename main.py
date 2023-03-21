from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/lists/{list_id}", response_model=schemas.List)
def read_list(list_id: int, db: Session = Depends(get_db)):
    db_list = crud.get_list(db, list_info=list_id)
    if db_list is None:
        raise HTTPException(status_code=404, detail="List not found")
    return db_list

@app.get("/all", response_model=list[schemas.List])
def read_lists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_lists = crud.get_lists(db, skip, limit)
    return db_lists

@app.post("/", response_model=schemas.List)
def create_list(list: schemas.ListCreate, db: Session = Depends(get_db)):
    db_list = crud.get_list(db, list_info=list.title)
    if db_list:
        raise HTTPException(status_code=400, detail="Title already registered")
    return crud.create_list(db=db, list=list)