from attrs import define, field

from .value_objects import Name, Id
from .permission import Permission


@define
class Role:
    id: Id
    name: Name
    permissions: list[Permission] = field(default_factory=[])
