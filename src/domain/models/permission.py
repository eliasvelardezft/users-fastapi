from attrs import define

from .value_objects import Name, Id, Description


@define
class Permission:
    id: Id
    name: Name
    description: Description
