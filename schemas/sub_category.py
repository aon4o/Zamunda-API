from pydantic import BaseModel


class CreateSubCategory(BaseModel):
    name: str
    order: int
    category_id: int


class SubCategory(BaseModel):
    id: int
    name: str
    order: int
    category_id: int
    created_at: str
    updated_at: str
