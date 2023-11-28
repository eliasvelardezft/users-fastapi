from fastapi import APIRouter

from api.v1.dtos.role import RoleCreate, RoleRead


router = APIRouter()


@router.post("")
def create_role(role: RoleCreate):
    return RoleRead.model_dump(role)
