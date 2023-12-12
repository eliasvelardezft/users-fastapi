from typing import Any

from domain.models.user import User
from domain.models.value_objects import Password
from domain.interfaces.repository import IRepository
from domain.interfaces.hash_service import IHashService


class UserService:
    def __init__(
        self,
        repository: IRepository,
        hash_service: IHashService,
    ):
        self.repository = repository
        self.hash_service = hash_service

    def create_user(self, user: User) -> User:
        hashed_password = self.hash_service.get_hash(user.password.value)
        user.password = Password(value=hashed_password)
        return self.repository.create(user)

    def get_users(
        self,
        filters: dict[str, Any] = {},
    ) -> list[User]:
        return self.repository.filter(filters=filters)

    def get_user(self, id: str) -> User | None:
        return self.repository.get(id=id)

    def update_user(self, user: User) -> User:
        return self.repository.update(user)

    def delete_user(self, id: str) -> None:
        return self.repository.delete(id=id)
