from domain.models.permission import Permission
from domain.services.permission import PermissionService


class TestPermissionService:
    def test_create_permission(
        self,
        test_permission_service: PermissionService,
        domain_permission: Permission
    ):
        permission = test_permission_service.create_permission(permission=domain_permission)
        assert permission.name == domain_permission.name

    def test_get_permissions(
        self,
        test_permission_service: PermissionService,
        domain_permission: Permission
    ):
        test_permission_service.create_permission(permission=domain_permission)
        permissions = test_permission_service.get_permissions()
        assert len(permissions) == 1
