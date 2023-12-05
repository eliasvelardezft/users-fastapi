from datetime import datetime

from pydantic import BaseModel, field_validator

from domain.models.value_objects import Email, Password, Username, Id
from api.v1.dtos import UpdateDTOMixin
from api.v1.dtos.role import RoleRead


class UserBase(BaseModel):
    email: str
    password: str
    username: str

    roles: list[int] = []

    @field_validator("email")
    def email_validator(cls, value: str) -> str:
        return Email(value=value).value

    @field_validator("password")
    def password_validator(cls, value: str) -> str:
        return Password(value=value).value
    
    @field_validator("username")
    def username_validator(cls, value: str) -> str:
        return Username(value=value).value

    @field_validator("roles")
    def roles_validator(cls, value: list[int]) -> list[int]:
        return [Id(value=role_id).value for role_id in value]


class UserCreate(UserBase):
    pass


class UserRead(BaseModel):
    id: int

    created_date: datetime
    updated_date: datetime
    deleted_date: datetime | None = None

    roles: list[RoleRead] = []
    role_ids: list[int] = []

    model_config = {"from_attributes": True}


class UserUpdate(UserBase, UpdateDTOMixin):
    pass
