from pydantic import BaseModel, validator, Field

from domain.data_objects import PermissionName


class PermissionBase(BaseModel):
    name: str
    description: str = Field(max_length=200)

    @validator("name")
    def validate_name(cls, value: str) -> str:
        return PermissionName(value).value


class PermissionCreate(PermissionBase):
    pass


class PermissionRead(PermissionBase):
    id: int

    class Config:
        orm_mode = True


class PermissionUpdate(PermissionBase):
    name: str | None = None
