from datetime import datetime

from pydantic import BaseModel, validator

from api.v1.dtos import UpdateDTOMixin
from domain.models.value_objects import Name, Description


class RoleBase(BaseModel):
    name: str
    description: str
    permissions: list[int] = []

    @validator("name")
    def validate_name(cls, value: str) -> str:
        return Name(value=value).value

    @validator("description")
    def validate_description(cls, value: str) -> str:
        return Description(value=value).value


class RoleCreate(RoleBase):
    pass


class RoleRead(RoleBase):
    id: int

    created_date: datetime
    updated_date: datetime
    deleted_date: datetime | None = None

    model_config = {"from_attributes": True}


class RoleUpdate(RoleBase, UpdateDTOMixin):
    pass
