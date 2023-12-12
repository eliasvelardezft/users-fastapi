from dataclasses import dataclass, field
from datetime import datetime

from .value_objects import Username, Password, Email, Id
from .role import Role


@dataclass(kw_only=True)
class User:
    id: Id | None = None

    active: bool | None = True
    username: Username
    password: Password
    email: Email
    roles: list[Role] = field(default_factory=list)
    role_ids: list[Id] = field(default_factory=list)

    created_date: datetime | None = None
    updated_date: datetime | None = None
    deleted_date: datetime | None = None
