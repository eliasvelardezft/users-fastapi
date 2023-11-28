from datetime import datetime

from pydantic import BaseModel, validator

from domain.models.value_objects import Email, Password, Username
from api.v1.dtos import UpdateDTOMixin
from api.v1.dtos.role import RoleRead


class UserBase(BaseModel):
    email: str
    password: str
    username: str

    roles: list[int] = []

    @validator("email")
    def email_validator(cls, value: str) -> str:
        return Email(value=value).value

    @validator("password")
    def password_validator(cls, value: str) -> str:
        return Password(value=value).value
    
    @validator("username")
    def username_validator(cls, value: str) -> str:
        return Username(value=value).value


class UserCreate(UserBase):
    pass


class UserRead(BaseModel):
    id: int

    created_date: datetime
    updated_date: datetime
    deleted_date: datetime | None = None

    roles: list[RoleRead] = []

    model_config = {"from_attributes": True}


class UserUpdate(UserBase, UpdateDTOMixin):
    pass
