from fastapi import APIRouter, Depends

from api.v1.adapters.role import RoleClientAdapter
from api.v1.dtos.role import (
    RoleCreate,
    RoleRead,
    RoleUpdate,
)
from api.v1.dependencies.services import (
    get_role_service,
)
from api.v1.dependencies.utils import (
    get_query_filters,
)
from domain.models.value_objects import QueryFilters
from domain.services.role import RoleService

router = APIRouter()


@router.post("", response_model=RoleRead)
def create_role(
    role: RoleCreate,
    role_service: RoleService = Depends(get_role_service)
):
    domain_role = RoleClientAdapter.client_to_domain(role)
    created_role = role_service.create_role(domain_role)
    return RoleClientAdapter.domain_to_client(created_role)


@router.get("", response_model=list[RoleRead])
def get_roles(
    query_filters: QueryFilters = Depends(get_query_filters),
    role_service: RoleService = Depends(get_role_service)
):
    roles = role_service.get_roles(query_filters)
    return [RoleClientAdapter.domain_to_client(role) for role in roles]


@router.get("/{role_id}", response_model=RoleRead)
def get_role(
    role_id: int,
    role_service: RoleService = Depends(get_role_service)
):
    role = role_service.get_role(role_id)
    return RoleClientAdapter.domain_to_client(role)


@router.patch("/{role_id}", response_model=RoleRead)
def update_role(
    role_id: int,
    role_update: RoleUpdate,
    role_service: RoleService = Depends(get_role_service)
):
    domain_role = RoleClientAdapter.client_to_domain(role_update)
    updated_role = role_service.update_role(role_id, domain_role)
    return RoleClientAdapter.domain_to_client(updated_role)


@router.delete("/{role_id}")
def delete_role(
    role_id: int,
    role_service: RoleService = Depends(get_role_service)
):
    role_service.delete_role(role_id)
    return {"message": "Role deleted successfully"}
