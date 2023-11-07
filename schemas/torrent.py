from pydantic import BaseModel

from schemas.sub_category import SubCategory


class TorrentCreate(BaseModel):
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
    created_at: str
    updated_at: str

    sub_category: SubCategory

    class Config:
        from_attributes = True

