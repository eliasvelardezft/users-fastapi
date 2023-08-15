from datetime import datetime

from pydantic import BaseModel, validator

from domain.data_objects import Name, BirthDate


class ProfileBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    birthdate: datetime | None = None

    @validator('first_name', 'last_name')
    def validate_name(cls, value: str) -> str:
        return Name(value).value
    
    @validator('birthdate')
    def validate_birthdate(cls, value: datetime) -> datetime:
        return BirthDate(value).value


class ProfileCreate(ProfileBase):
    pass


class ProfileRead(ProfileBase):
    id: int
    
    class Config:
        orm_mode = True


class ProfileUpdate(ProfileBase):
    pass
