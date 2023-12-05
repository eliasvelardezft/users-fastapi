from dataclasses import dataclass, field
from datetime import datetime

from .value_objects import Name, Id
from .permission import Permission


@dataclass(kw_only=True)
class Role:
    id: Id
    name: Name
    permissions: list[Permission] = field(default_factory=list)
    permission_ids: list[Id] = field(default_factory=list)

    created_date: datetime | None = None
    updated_date: datetime | None = None
    deleted_date: datetime | None = None
