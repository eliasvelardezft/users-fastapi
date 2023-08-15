from datetime import datetime

from pydantic import BaseModel, validator

from domain.data_objects import Email, Password, UserName
from .role import RoleRead


class UserBase(BaseModel):
    email: str
    password: str
    username: str

    roles: list[int] = []

    @validator("email")
    def email_validator(cls, value: str) -> str:
        return Email(value).value

    @validator("password")
    def password_validator(cls, value: str) -> str:
        return Password(value).value
    
    @validator("username")
    def username_validator(cls, value: str) -> str:
        return UserName(value).value


class UserCreate(UserBase):
    pass


class UserRead(BaseModel):
    id: int

    email: str
    username: str
    active: bool

    created_date: datetime
    updated_date: datetime
    deleted_date: datetime

    roles: list[RoleRead] = []

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    email: str | None = None
    password: str | None = None
    username: str | None = None
    active: bool | None = None
