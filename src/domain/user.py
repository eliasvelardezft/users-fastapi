from dataclasses import dataclass, field
from datetime import datetime

from .data_objects import Username, Password, Email
from .role import Role

@dataclass
class User:
    id: int | None = None
    active: bool | None = True
    username: Username
    password: Password
    email: Email
    roles: list[Role] = field(default_factory=list)

    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
