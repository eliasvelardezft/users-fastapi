from pydantic import BaseModel, Field, EmailStr, field_validator


class Email(BaseModel):
    value: EmailStr


class Password(BaseModel):
    value: str = Field(min_length=6)


class Username(BaseModel):
    value: str = Field(min_length=2, max_length=30)


class Name(BaseModel):
    value: str = Field(min_length=1, max_length=30)


class Id(BaseModel):
    value: str | int

    @field_validator("value")
    def validate_value(cls, value):
        if isinstance(value, str):
            if not value.isnumeric():
                raise ValueError("Id must be numeric")
            if not 1 <= len(value) <= 36:
                raise ValueError("Id must be between 1 and 36 characters")
        elif isinstance(value, int):
            if not 1 <= len(str(value)) <= 36:
                raise ValueError("Id must be between 1 and 36 characters") 
        return value


class Description(BaseModel):
    value: str = Field(min_length=1, max_length=200)
