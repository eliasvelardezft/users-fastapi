from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, validator


class Email(BaseModel):
    value: str = Field(
        regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )


class Password(BaseModel):
    value: str = Field(min_length=8)


class Username(BaseModel):
    value: str = Field(min_length=2, max_length=20)


class RoleName(Enum, str):
    USER = "user"
    PROFESSIONAL = "professional"
    ADMIN = "admin"


class Name(BaseModel):
    value: str = Field(min_length=1, max_length=20)


class BirthDate(BaseModel):
    value: datetime

    @validator("value")
    def validate_value(cls, value: datetime) -> datetime:
        if value > datetime.now():
            # TODO: refactor with custom exceptions
            raise ValueError("Birth date cannot be in the future")
        return value
