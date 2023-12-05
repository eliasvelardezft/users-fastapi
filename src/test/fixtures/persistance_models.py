import pytest

from infrastructure.persistance.models import (
    PermissionSQL,
    RoleSQL,
    UserSQL,
)


@pytest.fixture(scope="function")
def sql_permission():
    return PermissionSQL(
        id=1,
        name="testpermission",
        description="testdescription",
    )

@pytest.fixture(scope="function")
def sql_role():
    return RoleSQL(
        id=1,
        name="testrole",
        permission_ids=[1, 2],
    )

@pytest.fixture(scope="function")
def sql_user():
    return UserSQL(
        id=1,
        active=True,
        username="testusername",
        password="testpw",
        email="liomessi@gmail.com",
        role_ids=[1, 2],
    )
