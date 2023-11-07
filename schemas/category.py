from pydantic import BaseModel

from schemas.torrent import Torrent


class CreateCategory(BaseModel):
    name: str
    order: int


class Category(BaseModel):
    id: int
    name: str
    order: int
    created_at: str
    updated_at: str

    sub_categories: list[SubCategory] = []
