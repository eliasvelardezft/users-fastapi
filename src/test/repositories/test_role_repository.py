import pytest

from domain.models.role import Role
from domain.models.value_objects import Name, Id
from domain.exceptions import InvalidFilter
from infrastructure.persistance.repositories.role import RoleRepository
from test.conftest import BaseTestClass


class TestRoleRepository(BaseTestClass):
    def test_create(self, test_role_repository: RoleRepository):
        self._load_permissions()
        role = Role(
            name=Name(value="create_testrole"),
            permission_ids=[Id(value=1), Id(value=2)],
        )
        test_role_repository.create(role)

        created_role = test_role_repository.get(1)
        assert role.name == created_role.name
        assert role.permission_ids == created_role.permission_ids

    def test_filter(self, test_role_repository: RoleRepository):
        self._load_test_data()

        roles = test_role_repository.filter(
            filters={
                "name": "testrole_2",
            }
        )
        assert len(roles) == 1
        assert roles[0].id == Id(value=2)
        assert roles[0].name == Name(value="testrole_2")
        assert roles[0].permission_ids == [Id(value=1), Id(value=2)]
    
    def test_filter_by_user_id(self, test_role_repository: RoleRepository):
        self._load_test_data()

        roles = test_role_repository.filter(
            filters={"user": {"id": 1}},
        )
        assert len(roles) == 2

    def test_filter_by_user_email(self, test_role_repository: RoleRepository):
        self._load_test_data()

        roles = test_role_repository.filter(
            filters={"user": {"email": "liomessi@gmail.com"}},
        )
        assert len(roles) == 2

    def test_invalid_filter(self, test_role_repository: RoleRepository):
        self._load_test_data()

        with pytest.raises(InvalidFilter):
            test_role_repository.filter(
                filters={"invalid": "invalid"},
            )

    def test_get(self, test_role_repository: RoleRepository):
        self._load_test_data()

        role = test_role_repository.get(1)

        assert role is not None
        assert role.id == Id(value=1)
        assert role.name == Name(value="testrole")
        assert role.permission_ids == [Id(value=1), Id(value=2)]

    def test_bulk_create(self, test_role_repository: RoleRepository):
        self._load_permissions()

        role_1 = Role(
            name=Name(value="bulk_testrole"),
            permission_ids=[Id(value=1), Id(value=2)],
        )
        role_2 = Role(
            name=Name(value="bulk_testrole_2"),
            permission_ids=[Id(value=1), Id(value=2)],
        )

        test_role_repository.bulk_create([role_1, role_2])

        created_roles = test_role_repository.filter()

        assert len(created_roles) == 2
        assert created_roles[0].name == Name(value="bulk_testrole")
        assert created_roles[0].permission_ids == [Id(value=1), Id(value=2)]
        assert created_roles[1].name == Name(value="bulk_testrole_2")
        assert created_roles[1].permission_ids == [Id(value=1), Id(value=2)]
