import pytest

from api.v1.dtos.permission import PermissionCreate
from api.v1.dtos.role import RoleCreate
from api.v1.dtos.user import UserCreate


@pytest.fixture(scope="function")
def user_create() -> UserCreate:
    return UserCreate(
        username="test_user",
        password="test_password",
        email="test_email@gmail.com",
        role_ids=[],
    )

@pytest.fixture(scope="function")
def role_create() -> RoleCreate:
    return RoleCreate(
        name="test_role",
        description="test_description",
        permission_ids=[],
    )

@pytest.fixture(scope="function")
def permission_create() -> PermissionCreate:
    return PermissionCreate(
        name="test_permission",
        description="test_description",
    )
