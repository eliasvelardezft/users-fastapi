from typing import Any

from psycopg2 import errors
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from domain.interfaces.repository import IRepository
from domain.models.role import Role
from domain.exceptions import InvalidFilter, UserAlreadyHasRole, UserDoesNotExist
from infrastructure.persistance.adapters.role import RolePersistanceAdapter
from infrastructure.persistance.models import RoleSQL


class RoleRepository(IRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, id: str) -> Role | None:
        db_role = self.session.get(RoleSQL, id)
        role = None
        if db_role:
            role = RolePersistanceAdapter.persistance_to_domain(db_role)
        return role

    def filter(self, filters: dict[str, Any] = {}) -> list[Role]:
        query = self.session.query(RoleSQL)
        for key, value in filters.items():
            try:
                if key == "user":
                    query = query.join(RoleSQL.users)
                    for k, v in value.items():
                        query = query.filter(
                            getattr(RoleSQL.users.property.mapper.class_, k) == v
                        )
                else:
                    query = query.filter(getattr(RoleSQL, key) == value)
            except Exception as e:
                raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_roles = query.all()
        roles = [RolePersistanceAdapter.persistance_to_domain(role) for role in db_roles]
        return roles

    def create(self, role: Role) -> Role:
        db_role = RolePersistanceAdapter.domain_to_persistance(role)
        self.session.add(db_role)
        try:
            self.session.commit()
        except IntegrityError as sa_error:
            try:
                raise sa_error.orig
            except errors.ForeignKeyViolation:
                raise UserDoesNotExist
            except errors.UniqueViolation:
                raise UserAlreadyHasRole
        self.session.refresh(db_role)
        role = RolePersistanceAdapter.persistance_to_domain(db_role)
        return role

    def bulk_create(self, roles: list[Role]) -> list[Role]:
        db_roles = [
            RolePersistanceAdapter.domain_to_persistance(role)
            for role in roles
        ]
        self.session.add_all(db_roles)

        try:
            self.session.commit()
        except IntegrityError as sa_error:
            try:
                raise sa_error.orig
            except errors.ForeignKeyViolation:
                raise UserDoesNotExist
            except errors.UniqueViolation:
                raise UserAlreadyHasRole

        roles = [
            RolePersistanceAdapter.persistance_to_domain(role)
            for role in db_roles
        ]
        return roles
