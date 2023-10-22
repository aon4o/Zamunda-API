from pydantic import BaseModel


class TorrentBase(BaseModel):
    title: str
    description: str | None = None


class TorrentCreate(TorrentBase):
    pass


class Torrent(TorrentBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    torrents: list[Torrent] = []

    class Config:
        from_attributes = True
