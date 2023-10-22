from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas
from dependencies import get_token_header, get_db

router = APIRouter(
    prefix="/torrents",
    tags=["torrents"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[schemas.Torrent])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
