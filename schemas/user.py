from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    is_admin: bool
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True
