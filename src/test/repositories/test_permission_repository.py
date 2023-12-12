from domain.models.permission import Permission
from domain.models.value_objects import Name, Id, Description
from infrastructure.persistance.repositories.permission import PermissionRepository
from test.conftest import BaseTestClass


class TestPermissionRepository(BaseTestClass):
    def test_create(self, test_permission_repository: PermissionRepository):
        permission = Permission(
            name=Name(value="create_testpermission"),
            description=Description(value="create_testpermission_description"),
        )
        test_permission_repository.create(permission)

        created_permission = test_permission_repository.get(1)
        assert permission.name == created_permission.name

    def test_filter(self, test_permission_repository: PermissionRepository):
        self._load_test_data()

        permissions = test_permission_repository.filter(
            filters={
                "name": "testpermission_2",
            }
        )
        assert len(permissions) == 1
        assert permissions[0].id == Id(value=2)
        assert permissions[0].name == Name(value="testpermission_2")

    def test_get(self, test_permission_repository: PermissionRepository):
        self._load_test_data()

        permission = test_permission_repository.get(1)

        assert permission is not None
        assert permission.id == Id(value=1)
        assert permission.name == Name(value="testpermission")

    def test_bulk_create(self, test_permission_repository: PermissionRepository):
        permission_1 = Permission(
            name=Name(value="bulk_testpermission"),
            description=Description(value="bulk_testpermission_description"),
        )
        permission_2 = Permission(
            name=Name(value="bulk_testpermission_2"),
            description=Description(value="bulk_testpermission_2_description"),
        )

        test_permission_repository.bulk_create([permission_1, permission_2])

        created_permissions = test_permission_repository.filter()

        assert len(created_permissions) == 2
        assert created_permissions[0].name == Name(value="bulk_testpermission")