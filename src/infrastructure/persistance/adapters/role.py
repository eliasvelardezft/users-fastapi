from domain.models.role import Role
from domain.models.value_objects import Name, Id
from domain.interfaces.adapters.persistance_adapter import IPersistanceAdapter
from infrastructure.persistance.models import RoleSQL
from infrastructure.persistance.adapters.permission import PermissionPersistanceAdapter


class RolePersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(
        role: Role,
    ) -> RoleSQL:
        return RoleSQL(
            id=role.id.value,
            name=role.name.value,
            permission_ids=role.permission_ids,
            created_date=role.created_date,
            updated_date=role.updated_date,
            deleted_date=role.deleted_date,
        )

    @staticmethod
    def persistance_to_domain(
        role: RoleSQL,
    ) -> Role:
        domain_permissions = [
            PermissionPersistanceAdapter.persistance_to_domain(permission)
            for permission in role.permissions
        ]
        return Role(
            id=Id(value=role.id),
            name=Name(value=role.name),
            permission_ids=role.permission_ids,
            permissions=domain_permissions,
            created_date=role.created_date,
            updated_date=role.updated_date,
            deleted_date=role.deleted_date,
        )
