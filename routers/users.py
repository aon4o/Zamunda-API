from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import user as user_crud
from crud import torrents as torrent_crud
from schemas import user as schema
from schemas import torrent as torrent_schema
from dependencies import get_db, get_token_header

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)


@router.get("/", response_model=list[schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/{user_id}/torrents/", response_model=torrent_schema.Torrent)
def create_item_for_user(
        user_id: int, torrent: torrent_schema.TorrentCreate, db: Session = Depends(get_db)
):
    return torrent_crud.create_user_torrent(db=db, torrent=torrent, user_id=user_id)
