from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import torrent as schema
from dependencies import get_token_header, get_db
from crud import user as user_crud

router = APIRouter(
    prefix="/torrents",
    tags=["torrents"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

