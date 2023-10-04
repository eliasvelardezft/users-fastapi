from dataclasses import dataclass
from datetime import datetime

from .user import User


@dataclass
class Profile:
    id: int | None = None
    first_name: str | None = None
    last_name: str | None = None
    birthdate: datetime | None = None
    user: User | None = None