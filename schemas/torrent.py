import datetime

from pydantic import BaseModel

from schemas.sub_category import SubCategory


class TorrentCreate(BaseModel):
    user_id: int
    name: str
    description: str
    image: str | None = None
    file: str
    times_downloaded: int
    sub_category_id: int


class Torrent(BaseModel):
    id: int
    name: str
    description: str
    image: str | None = None
    file: str
    times_downloaded: int
    user_id: int
    sub_category_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    sub_category: SubCategory | None = None

    class Config:
        from_attributes = True

