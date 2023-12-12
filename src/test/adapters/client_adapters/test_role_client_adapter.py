from domain.models.role import Role
from api.v1.adapters.role import RoleClientAdapter
from api.v1.dtos.role import RoleRead, RoleCreate
from test.conftest import BaseTestClass


class TestRoleClientAdapter(BaseTestClass):
    def test_client_to_domain(self, role_create):
        domain_role = RoleClientAdapter.client_to_domain(role_create)

        assert isinstance(domain_role, Role)
        assert domain_role.name.value == role_create.name

    def test_domain_to_client(self, domain_role):
        role_read = RoleClientAdapter.domain_to_client(domain_role)

        assert isinstance(role_read, RoleRead)
        assert role_read.id == domain_role.id.value
        assert role_read.name == domain_role.name.value
