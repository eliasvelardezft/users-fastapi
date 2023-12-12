import pytest

from infrastructure.persistance.repositories.role import RoleRepository
from infrastructure.persistance.repositories.permission import PermissionRepository
from infrastructure.persistance.repositories.user import UserRepository


@pytest.fixture(scope="function")
def test_role_repository(test_session) -> RoleRepository:
    return RoleRepository(test_session)

@pytest.fixture(scope="function")
def test_permission_repository(test_session) -> PermissionRepository:
    return PermissionRepository(test_session)

@pytest.fixture(scope="function")
def test_user_repository(test_session) -> UserRepository:
    return UserRepository(test_session)
