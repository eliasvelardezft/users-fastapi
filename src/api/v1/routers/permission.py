from fastapi import APIRouter, Depends

from api.v1.adapters.permission import PermissionClientAdapter
from api.v1.dtos.permission import (
    PermissionCreate,
    PermissionRead,
    PermissionUpdate,
)
from api.v1.dependencies.services import (
    get_permission_service,
)
from api.v1.dependencies.utils import (
    get_query_filters,
)
from domain.models.value_objects import QueryFilters
from domain.services.permission import PermissionService


router = APIRouter()


@router.post("", response_model=PermissionRead, status_code=201)
def create_permission(
    permission: PermissionCreate,
    permission_service: PermissionService = Depends(get_permission_service)
):
    domain_permission = PermissionClientAdapter.client_to_domain(permission)
    created_permission = permission_service.create_permission(domain_permission)
    return PermissionClientAdapter.domain_to_client(created_permission)


@router.get("", response_model=list[PermissionRead])
def get_permissions(
    filters: QueryFilters = Depends(get_query_filters),
    permission_service: PermissionService = Depends(get_permission_service)
):
    permissions = permission_service.get_permissions(filters=filters)
    return [PermissionClientAdapter.domain_to_client(permission) for permission in permissions]


@router.get("/{permission_id}", response_model=PermissionRead)
def get_permission(
    permission_id: int,
    permission_service: PermissionService = Depends(get_permission_service)
):
    permission = permission_service.get_permission(permission_id)
    return PermissionClientAdapter.domain_to_client(permission)


@router.patch("/{permission_id}", response_model=PermissionRead)
def update_permission(
    permission_id: int,
    permission: PermissionUpdate,
    permission_service: PermissionService = Depends(get_permission_service)
):
    domain_permission = PermissionClientAdapter.client_to_domain(permission)
    updated_permission = permission_service.update_permission(permission_id, domain_permission)
    return PermissionClientAdapter.domain_to_client(updated_permission)


@router.delete("/{permission_id}")
def delete_permission(
    permission_id: int,
    permission_service: PermissionService = Depends(get_permission_service)
):
    permission_service.delete_permission(permission_id)
    return {"message": "Permission deleted successfully."}
