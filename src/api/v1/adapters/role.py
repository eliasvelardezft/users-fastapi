from domain.interfaces.adapters.client_adapter import IClientAdapter
from domain.models.role import Role
from domain.models.value_objects import Id, Name, Description
from api.v1.dtos.role import RoleRead, RoleCreate


class RoleClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(role: RoleCreate) -> Role:
        return Role(
            name=Name(value=role.name),
            permission_ids=[Id(value=permission_id) for permission_id in role.permission_ids]
        )

    @staticmethod
    def domain_to_client(role: Role) -> RoleRead:
        return RoleRead(
            id=role.id.value,
            name=role.name.value,
            permission_ids=[permission_id.value for permission_id in role.permission_ids],
            created_date=role.created_date,
            updated_date=role.updated_date,
            deleted_date=role.deleted_date,
        )
