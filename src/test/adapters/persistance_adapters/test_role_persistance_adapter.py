from domain.models.role import Role
from infrastructure.persistance.adapters.role import RolePersistanceAdapter
from infrastructure.persistance.models.role import RoleSQL
from test.conftest import BaseTestClass


class TestRolePersistanceAdapter(BaseTestClass):
    def test_domain_to_persistance(self, domain_role):
        sql_role = RolePersistanceAdapter.domain_to_persistance(domain_role)

        assert isinstance(sql_role, RoleSQL)
        assert sql_role.id == domain_role.id.value
        assert sql_role.name == domain_role.name.value
        assert sql_role.permissions == [permission.value for permission in domain_role.permissions]
        assert sql_role.created_date == domain_role.created_date
        assert sql_role.updated_date == domain_role.updated_date
        assert sql_role.deleted_date == domain_role.deleted_date

    def test_persistance_to_domain(self, sql_role):
        domain_role = RolePersistanceAdapter.persistance_to_domain(sql_role)

        assert isinstance(domain_role, Role)
        assert domain_role.id.value == sql_role.id
        assert domain_role.name.value == sql_role.name
        assert [permission.value for permission in domain_role.permissions] == sql_role.permissions
        assert domain_role.created_date == sql_role.created_date
        assert domain_role.updated_date == sql_role.updated_date
        assert domain_role.deleted_date == sql_role.deleted_date