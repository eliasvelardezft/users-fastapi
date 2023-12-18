from sqlalchemy.orm import Session
from fastapi import Depends

from infrastructure.persistance.base import get_session
from domain.services.permission import PermissionService
from domain.services.role import RoleService
from domain.services.user import UserService
from domain.services.auth import AuthService
from infrastructure.auth.hash_service import HashService
from infrastructure.persistance.repositories.permission import PermissionRepository
from infrastructure.persistance.repositories.role import RoleRepository
from infrastructure.persistance.repositories.user import UserRepository



def get_permission_service(session: Session = Depends(get_session)) -> PermissionService:
    return PermissionService(repository=PermissionRepository(session))


def get_role_service(session: Session = Depends(get_session)) -> RoleService:
    return RoleService(repository=RoleRepository(session))


def get_user_service(session: Session = Depends(get_session)) -> UserService:
    return UserService(
        repository=UserRepository(session),
        hash_service=HashService(),
    )


def get_auth_service(session: Session = Depends(get_session)) -> AuthService:
    return AuthService(
        repository=UserRepository(session),
        hash_service=HashService()
    )
