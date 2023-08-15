from dataclasses import dataclass, field

from .data_objects import PermissionName


@dataclass
class Permission:
    id: int | None = None
    name: PermissionName
    description: str
