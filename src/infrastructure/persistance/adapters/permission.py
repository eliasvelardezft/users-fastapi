from domain.models.permission import Permission
from domain.models.value_objects import Name, Description, Id
from domain.interfaces.adapters.persistance_adapter import IPersistanceAdapter
from infrastructure.persistance.models import PermissionSQL


class PermissionPersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(
        permission: Permission,
    ) -> PermissionSQL:
        return PermissionSQL(
            id=permission.id.value,
            name=permission.name.value,
            description=permission.description.value,
            created_date=permission.created_date,
            updated_date=permission.updated_date,
            deleted_date=permission.deleted_date,
        )

    @staticmethod
    def persistance_to_domain(
        permission: PermissionSQL,
    ) -> Permission:
        return Permission(
            id=Id(value=permission.id),
            name=Name(value=permission.name),
            description=Description(value=permission.description),
            created_date=permission.created_date,
            updated_date=permission.updated_date,
            deleted_date=permission.deleted_date,
        )
