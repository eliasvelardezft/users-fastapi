from domain.models.role import Role
from domain.services.role import RoleService


class TestRoleService:
    def test_create_role(
        self,
        test_role_service: RoleService,
        domain_role: Role
    ):
        role = test_role_service.create_role(role=domain_role)
        assert role.name == domain_role.name

    def test_get_roles(
        self,
        test_role_service: RoleService,
        domain_role: Role
    ):
        test_role_service.create_role(role=domain_role)
        roles = test_role_service.get_roles()
        assert len(roles) == 1
