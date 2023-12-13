from datetime import datetime

from pydantic import BaseModel, field_validator

from api.v1.dtos import UpdateDTOMixin
from domain.models.value_objects import Name, Description


class PermissionBase(BaseModel):
    name: str
    description: str

    @field_validator("name")
    def validate_name(cls, value: str) -> str:
        return Name(value=value).value

    @field_validator("description")
    def validate_description(cls, value: str) -> str:
        return Description(value=value).value


class PermissionCreate(PermissionBase):
    pass


class PermissionRead(PermissionBase):
    id: int

    created_date: datetime
    updated_date: datetime
    deleted_date: datetime | None = None

    model_config = {"from_attributes": True}


class PermissionUpdate(PermissionBase, UpdateDTOMixin):
    pass
