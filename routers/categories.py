from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas.category as category_schema
import crud.category as category_crud
from dependencies import get_db

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[category_schema.Category])
def index(db: Session = Depends(get_db)):
    return category_crud.list_all(db)


@router.get("/{category_id}", response_model=category_schema.Category)
def show(category_id: int, db: Session = Depends(get_db)):
    return category_crud.get(db, category_id)


@router.post("/", response_model=category_schema.Category)
def create(category: category_schema.CreateCategory, db: Session = Depends(get_db)):
    return category_crud.create(db, category)


@router.put("/{category_id}", response_model=category_schema.Category)
def update(category_id: int, category: category_schema.CreateCategory, db: Session = Depends(get_db)):
    return category_crud.update(db, category_id, category)


@router.delete("/{category_id}")
def delete(category_id: int, db: Session = Depends(get_db)):
    return category_crud.delete(db, category_id)
