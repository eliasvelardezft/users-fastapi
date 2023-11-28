from pydantic import BaseModel, Field, EmailStr


class Email(BaseModel):
    value: EmailStr


class Password(BaseModel):
    value: str = Field(min_length=8)


class Username(BaseModel):
    value: str = Field(min_length=2, max_length=20)


class Name(BaseModel):
    value: str = Field(min_length=1, max_length=20)


class Id(BaseModel):
    value: str = Field(min_length=1, max_length=36)


class Description(BaseModel):
    value: str = Field(min_length=1, max_length=200)
