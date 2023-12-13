from domain.models.permission import Permission
from api.v1.adapters.permission import PermissionClientAdapter
from api.v1.dtos.permission import PermissionRead, PermissionCreate
from test.conftest import BaseTestClass


class TestPermissionClientAdapter(BaseTestClass):
    def test_client_to_domain(self, permission_create):
        domain_permission = PermissionClientAdapter.client_to_domain(permission_create)

        assert isinstance(domain_permission, Permission)
        assert domain_permission.name.value == permission_create.name
        assert domain_permission.description.value == permission_create.description

    def test_domain_to_client(self, domain_permission):
        permission_read_dto = PermissionClientAdapter.domain_to_client(domain_permission)

        assert isinstance(permission_read_dto, PermissionRead)
        assert permission_read_dto.id == domain_permission.id.value
        assert permission_read_dto.name == domain_permission.name.value
        assert permission_read_dto.description == domain_permission.description.value

