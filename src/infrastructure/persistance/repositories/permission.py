from dataclasses import asdict
from typing import Any
from datetime import datetime

from psycopg2 import errors
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from domain.interfaces.repository import IRepository
from domain.models.permission import Permission
from domain.models.value_objects import QueryFilters, ComparisonFieldFilter, RangeFieldFilter
from domain.exceptions import InvalidFilter
from infrastructure.persistance.adapters.permission import PermissionPersistanceAdapter
from infrastructure.persistance.models import PermissionSQL


class PermissionRepository(IRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, id: str) -> Permission | None:
        db_permission = self.session.get(PermissionSQL, id)
        permission = None
        if db_permission and not db_permission.deleted_date:
            permission = PermissionPersistanceAdapter.persistance_to_domain(db_permission)
            return permission

    def filter(self, filters: QueryFilters | None = {}) -> list[Permission]:
        query = self.session.query(PermissionSQL)
        if filters:
            for key, value in filters.filters.items():
                try:
                    if key == "role":
                        query = query.join(PermissionSQL.roles)
                        for k, v in value.items():
                            query = query.filter(
                                getattr(PermissionSQL.roles.property.mapper.class_, k) == v
                            )
                    else:
                        if isinstance(value, ComparisonFieldFilter):
                            query = query.filter(
                                getattr(PermissionSQL, key).op(value.comparison_operator)(value.value)
                            )
                        elif isinstance(value, RangeFieldFilter):
                            query = query.filter(
                                getattr(PermissionSQL, key).between(value.start, value.end)
                            )
                        else:
                            query = query.filter(getattr(PermissionSQL, key) == value)
                except Exception as e:
                    raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_permissions = query.all()
        permissions = [PermissionPersistanceAdapter.persistance_to_domain(permission) for permission in db_permissions]
        return permissions

    def create(self, permission: Permission) -> Permission:
        db_permission = PermissionPersistanceAdapter.domain_to_persistance(permission)
        self.session.add(db_permission)
        try:
            self.session.commit()
        except IntegrityError as sa_error:
            try:
                raise sa_error.orig
            except:
                pass
            # except errors.ForeignKeyViolation:
            #     raise UserDoesNotExist
            # except errors.UniqueViolation:
            #     raise UserAlreadyHasPermission
        self.session.refresh(db_permission)
        permission = PermissionPersistanceAdapter.persistance_to_domain(db_permission)
        return permission

    def bulk_create(self, permissions: list[Permission]) -> list[Permission]:
        db_permissions = [
            PermissionPersistanceAdapter.domain_to_persistance(permission)
            for permission in permissions
        ]
        self.session.add_all(db_permissions)

        try:
            self.session.commit()
        except IntegrityError as sa_error:
            try:
                raise sa_error.orig
            except:
                pass
            # except errors.ForeignKeyViolation:
            #     raise UserDoesNotExist
            # except errors.UniqueViolation:
            #     raise UserAlreadyHasPermission

        permissions = [
            PermissionPersistanceAdapter.persistance_to_domain(permission)
            for permission in db_permissions
        ]
        return permissions

    def update(self, id: str, data: Permission) -> Permission:
        db_permission = self.session.get(PermissionSQL, id)
        
        if db_permission:
            data = PermissionPersistanceAdapter.domain_to_persistance(data)
            data_dict = {
                c.key: getattr(data, c.key) 
                for c in inspect(data).mapper.column_attrs
                if getattr(data, c.key) is not None
            }

            for key, value in data_dict.items():
                setattr(db_permission, key, value)
            self.session.commit()
            permission = PermissionPersistanceAdapter.persistance_to_domain(db_permission)
            return permission
        else:
            raise Exception("Permission not found")

    def delete(self, id: int) -> None:
        db_permission = self.session.get(PermissionSQL, id)
        if db_permission and not db_permission.deleted_date:
            db_permission.deleted_date = datetime.now()
            self.session.commit()
