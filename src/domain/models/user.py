from attrs import define, field
from datetime import datetime

from .value_objects import Username, Password, Email, Id
from .role import Role

@define
class User:
    id: Id | None = None

    active: bool | None = True
    username: Username
    password: Password
    email: Email
    roles: list[Role] = field(default_factory=[])

    created_date: datetime | None = None
    updated_date: datetime | None = None
    deleted_date: datetime | None = None
