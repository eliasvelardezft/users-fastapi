from dataclasses import asdict

from fastapi import APIRouter, Depends, HTTPException
import pydantic

from api.v1.adapters.user import UserClientAdapter
from api.v1.dtos.user import (
    UserCreate,
    UserRead,
    UserUpdate,
)
from api.v1.dependencies.services import (
    get_user_service,
)
from api.v1.dependencies.utils import (
    get_query_filters,
)
from domain.models.value_objects import QueryFilters
from domain.services.user import UserService

router = APIRouter()


@router.post("", response_model=UserRead)
def create_user(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    domain_user = UserClientAdapter.client_to_domain(user)
    created_user = user_service.create_user(domain_user)
    return UserClientAdapter.domain_to_client(created_user)


@router.get("", response_model=list[UserRead])
def get_users(
    query_filters: QueryFilters = Depends(get_query_filters),
    user_service: UserService = Depends(get_user_service)
):
    users = user_service.get_users(query_filters)
    return [UserClientAdapter.domain_to_client(user) for user in users]


@router.get("/{user_id}", response_model=UserRead)
def get_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    user = user_service.get_user(user_id)
    if user:
        return UserClientAdapter.domain_to_client(user)
    else:
        raise HTTPException(status_code=404, detail="Role not found")


@router.patch("/{user_id}", response_model=UserRead)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    user_service: UserService = Depends(get_user_service)
):
    update_dict = user_update.model_dump(exclude_unset=True)
    user = user_service.get_user(user_id)
    user_update = UserClientAdapter.update_to_domain(user, update_dict)
    updated_user = user_service.update_user(user_id, user_update)
    return UserClientAdapter.domain_to_client(updated_user)


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    user_service.delete_user(user_id)
    return {"message": "User deleted successfully"}
