import pytest

from domain.services.user import UserService
from domain.services.role import RoleService
from domain.services.permission import PermissionService
from domain.services.auth import AuthService
from infrastructure.auth.hash_service import HashService


@pytest.fixture(scope="function")
def test_user_service(test_user_repository) -> UserService:
    return UserService(
        repository=test_user_repository,
        hash_service=HashService(),
    )

@pytest.fixture(scope="function")
def test_role_service(test_role_repository) -> RoleService:
    return RoleService(
        repository=test_role_repository,
    )

@pytest.fixture(scope="function")
def test_permission_service(test_permission_repository) -> PermissionService:
    return PermissionService(
        repository=test_permission_repository,
    )

@pytest.fixture(scope="function")
def test_auth_service(test_user_repository) -> AuthService:
    return AuthService(
        user_repository=test_user_repository,
        hash_service=HashService(),
    )
