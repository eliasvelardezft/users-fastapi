from dataclasses import dataclass
from datetime import datetime

from .value_objects import Name, Id, Description


@dataclass(kw_only=True)
class Permission:
    id: Id
    name: Name
    description: Description

    created_date: datetime | None = None
    updated_date: datetime | None = None
    deleted_date: datetime | None = None
