from fastapi import APIRouter

from api.v1.dtos.user import UserCreate, UserRead


router = APIRouter()


@router.post("")
def create_user(user: UserCreate):
    return UserRead.model_dump(user)
