from fastapi import APIRouter, Depends

from dependencies import get_token_header

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def create_user():
    return {"message": "Hello Bigger Applications!"}
