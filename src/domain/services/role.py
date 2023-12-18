from typing import Any

from domain.models.role import Role
from domain.interfaces.repository import IRepository


class RoleService:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def create_role(self, role: Role) -> Role:
        return self.repository.create(role)

    def get_roles(
        self,
        filters: dict[str, Any] = {},
    ) -> list[Role]:
        return self.repository.filter(filters=filters)

    def get_role(self, id: str) -> Role | None:
        return self.repository.get(id=id)

    def update_role(self, id: str, role: Role) -> Role:
        return self.repository.update(id=id, data=role)

    def delete_role(self, id: str) -> Any:
        return self.repository.delete(id=id)
