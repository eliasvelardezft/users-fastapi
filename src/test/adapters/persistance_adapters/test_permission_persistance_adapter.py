from domain.models.permission import Permission
from infrastructure.persistance.adapters.permission import PermissionPersistanceAdapter
from infrastructure.persistance.models.permission import PermissionSQL
from test.conftest import BaseTestClass


class TestPermissionPersistanceAdapter(BaseTestClass):
    def test_domain_to_persistance(self, domain_permission):
        sql_permission = PermissionPersistanceAdapter.domain_to_persistance(domain_permission)

        assert isinstance(sql_permission, PermissionSQL)
        assert sql_permission.name == domain_permission.name.value
        assert sql_permission.created_date == domain_permission.created_date
        assert sql_permission.updated_date == domain_permission.updated_date
        assert sql_permission.deleted_date == domain_permission.deleted_date

    def test_persistance_to_domain(self, sql_permission):
        domain_permission = PermissionPersistanceAdapter.persistance_to_domain(sql_permission)

        assert isinstance(domain_permission, Permission)
        assert domain_permission.name.value == sql_permission.name
        assert domain_permission.created_date == sql_permission.created_date
        assert domain_permission.updated_date == sql_permission.updated_date
        assert domain_permission.deleted_date == sql_permission.deleted_date
