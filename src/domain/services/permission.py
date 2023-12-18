from typing import Any

from domain.models.permission import Permission
from domain.models.value_objects import QueryFilters
from domain.interfaces.repository import IRepository


class PermissionService:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def create_permission(self, permission: Permission) -> Permission:
        return self.repository.create(permission)

    def get_permissions(
        self,
        filters: QueryFilters | None = {},
    ) -> list[Permission]:
        return self.repository.filter(filters=filters)

    def get_permission(self, id: str) -> Permission | None:
        return self.repository.get(id=id)

    def update_permission(self, id: str, permission: Permission) -> Permission:
        return self.repository.update(id=id, data=permission)

    def delete_permission(self, id: str) -> Any:
        return self.repository.delete(id=id)
