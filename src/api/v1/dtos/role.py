from datetime import datetime

from pydantic import BaseModel, field_validator

from api.v1.dtos import UpdateDTOMixin
from domain.models.value_objects import Name, Id


class RoleBase(BaseModel):
    name: str
    permission_ids: list[int] = []

    @field_validator("name")
    def validate_name(cls, value: str) -> str:
        return Name(value=value).value

    @field_validator("permission_ids")
    def validate_permission_ids(cls, value: list[int]) -> list[int]:
        return [Id(value=permission_id).value for permission_id in value]


class RoleCreate(RoleBase):
    pass


class RoleRead(RoleBase):
    id: int

    permissions: list = []

    created_date: datetime
    updated_date: datetime
    deleted_date: datetime | None = None

    model_config = {"from_attributes": True}


class RoleUpdate(RoleBase, UpdateDTOMixin):
    pass
