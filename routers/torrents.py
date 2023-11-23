from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas.torrent as torrents_schema
import crud.torrents as torrent_crud
from dependencies import get_db

router = APIRouter(
    prefix="/torrents",
    tags=["torrents"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[torrents_schema.Torrent])
def index(db: Session = Depends(get_db)):
    return torrent_crud.list_all(db)


@router.get("/{torrent_id}", response_model=torrents_schema.Torrent)
def show(torrent_id: int, db: Session = Depends(get_db)):
    return torrent_crud.get(db, torrent_id)


@router.post("/", response_model=torrents_schema.Torrent)
def create(torrent: torrents_schema.TorrentCreate, db: Session = Depends(get_db)):
    return torrent_crud.create(db, torrent)


@router.put("/{torrent_id}", response_model=torrents_schema.Torrent)
def update(torrent_id: int, torrent: torrents_schema.TorrentCreate, db: Session = Depends(get_db)):
    return torrent_crud.update(db, torrent_id, torrent)


@router.delete("/{torrent_id}")
def delete(torrent_id: int, db: Session = Depends(get_db)):
    return torrent_crud.delete(db, torrent_id)
