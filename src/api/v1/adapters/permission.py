from domain.interfaces.adapters.client_adapter import IClientAdapter
from domain.models.permission import Permission
from domain.models.value_objects import Id, Name, Description
from api.v1.dtos.permission import PermissionRead, PermissionCreate


class PermissionClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(permission: PermissionCreate) -> Permission:
        return Permission(
            name=Name(value=permission.name),
            description=Description(value=permission.description)
        )

    @staticmethod
    def domain_to_client(permission: Permission) -> PermissionRead:
        return PermissionRead(
            id=permission.id.value,
            name=permission.name.value,
            description=permission.description.value,
            created_date=permission.created_date,
            updated_date=permission.updated_date,
            deleted_date=permission.deleted_date,
        )
