from datetime import datetime, timedelta

from domain.models.permission import Permission
from domain.models.value_objects import (
    Name,
    Id,
    Description,
    ComparisonFieldFilter,
    RangeFieldFilter,
    QueryFilters,
    ComparisonOperator,
)
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

    def test_filter_exact(self, test_permission_repository: PermissionRepository):
        self._load_test_data()

        filters_dict = {
            "filters": {
                "name": {
                    "value": "testpermission_2",
                    "comparison_operator": ComparisonOperator.EQ,
                },
            }
        }
        filters = QueryFilters.model_validate(filters_dict)

        permissions = test_permission_repository.filter(
            filters=filters
        )
        assert len(permissions) == 1
        assert permissions[0].id == Id(value=2)
        assert permissions[0].name == Name(value="testpermission_2")

    def test_filter_not_exact(self, test_permission_repository: PermissionRepository):
        self._load_test_data()

        filters_dict = {
            "filters": {
                "name": {
                    "value": "testpermission",
                    "comparison_operator": ComparisonOperator.NEQ,
                },
            }
        }
        filters = QueryFilters.model_validate(filters_dict)
    
        permissions = test_permission_repository.filter(
            filters=filters
        )
        assert len(permissions) == 1

    def test_filter_greater_than(self, test_permission_repository: PermissionRepository):
        self._load_test_data()

        filters_dict = {
            "filters": {
                "created_date": {
                    "value": "2020-01-01",
                    "comparison_operator": ComparisonOperator.GT,
                },
            }
        }
        filters = QueryFilters.model_validate(filters_dict)

        permissions = test_permission_repository.filter(
            filters=filters
        )
        assert len(permissions) == 2

    def test_filter_greater_than_or_equal(
        self, test_permission_repository: PermissionRepository
    ):
        self._load_test_data()

        yesterday = datetime.now() - timedelta(days=1)

        filters_dict = {
            "filters": {
                "created_date": {
                    "value": yesterday.isoformat(),
                    "comparison_operator": ComparisonOperator.GTE,
                },
            }
        }
        filters = QueryFilters.model_validate(filters_dict)

        permissions = test_permission_repository.filter(
            filters=filters
        )
        assert len(permissions) == 2

    def test_filter_range(self, test_permission_repository: PermissionRepository):
        self._load_test_data()

        yesterday = datetime.now() - timedelta(days=1)
        tomorrow = datetime.now() + timedelta(days=1)

        filters_dict = {
            "filters": {
                "created_date": {
                    "start": yesterday.isoformat(),
                    "end": tomorrow.isoformat(),
                },
            }
        }
        filters = QueryFilters.model_validate(filters_dict)

        permissions = test_permission_repository.filter(
            filters=filters
        )
        assert len(permissions) == 2

    def test_filter_invalid(self, test_permission_repository: PermissionRepository):
        self._load_test_data()

        filters_dict = {
            "filters": {
                "created_date": {
                    "value": "invalid_date",
                    "comparison_operator": ComparisonOperator.GT,
                },
            }
        }
        filters = QueryFilters.model_validate(filters_dict)

        try:
            test_permission_repository.filter(
                filters=filters
            )
        except Exception as e:
            assert type(e).__name__ == "InvalidFilter"

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