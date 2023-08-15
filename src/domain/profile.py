from dataclasses import dataclass, field

from .data_objects import RoleName
from .permission import Permission


@dataclass
class Profile:
    id: int | None = None
    name: RoleName
    permissions: list[Permission] = field(default_factory=list)