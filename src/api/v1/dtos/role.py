from pydantic import BaseModel, validator, Field

from domain.data_objects import RoleName


class RoleBase(BaseModel):
    name: str
    description: str = Field(..., max_length=200)
    permissions: list[int] = []

    @validator
    def validate_name(cls, value: str) -> str:
        return RoleName(value).value


class RoleCreate(RoleBase):
    pass


class RoleRead(RoleBase):
    id: int

    class Config:
        orm_mode = True


class RoleUpdate(RoleBase):
    name: str | None = None
    description: str | None = Field(max_length=200)
    permissions: list[int] | None = None
