from typing import Any
from datetime import datetime

from psycopg2 import errors
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from domain.interfaces.repository import IRepository
from domain.models.user import User
from domain.models.value_objects import QueryFilters, ComparisonFieldFilter, RangeFieldFilter
from domain.exceptions import InvalidFilter, UserDoesNotExist
from infrastructure.persistance.adapters.user import UserPersistanceAdapter
from infrastructure.persistance.models import UserSQL


class UserRepository(IRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, id: str) -> User | None:
        db_user = self.session.get(UserSQL, id)
        user = None
        if db_user:
            user = UserPersistanceAdapter.persistance_to_domain(db_user)
        return user

    def filter(self, filters: QueryFilters | None = {}) -> list[User]:
        query = self.session.query(UserSQL)
        if filters:
            for key, value in filters.filters.items():
                try:
                    if isinstance(value, ComparisonFieldFilter):
                        query = query.filter(
                            getattr(UserSQL, key).op(value.comparison_operator)(value.value)
                        )
                    elif isinstance(value, RangeFieldFilter):
                        query = query.filter(
                            getattr(UserSQL, key).between(value.start, value.end)
                        )
                    else:
                        query = query.filter(getattr(UserSQL, key) == value)
                except Exception as e:
                    raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_users = query.all()
        users = [UserPersistanceAdapter.persistance_to_domain(user) for user in db_users]
        return users

    def create(self, user: User) -> User:
        db_user = UserPersistanceAdapter.domain_to_persistance(user)
        self.session.add(db_user)
        try:
            self.session.commit()
        except IntegrityError as sa_error:
            try:
                raise sa_error.orig
            except errors.ForeignKeyViolation:
                raise UserDoesNotExist
        self.session.refresh(db_user)
        user = UserPersistanceAdapter.persistance_to_domain(db_user)
        return user

    def bulk_create(self, users: list[User]) -> list[User]:
        db_users = [
            UserPersistanceAdapter.domain_to_persistance(user)
            for user in users
        ]
        self.session.add_all(db_users)

        try:
            self.session.commit()
        except IntegrityError as sa_error:
            try:
                raise sa_error.orig
            except errors.ForeignKeyViolation:
                raise UserDoesNotExist

        users = [
            UserPersistanceAdapter.persistance_to_domain(user)
            for user in db_users
        ]
        return users

    def update(self, id: str, data: User) -> User:
        db_user = self.session.get(UserSQL, id)
        
        if db_user:
            data = UserPersistanceAdapter.domain_to_persistance(data)
            data_dict = {
                c.key: getattr(data, c.key) 
                for c in inspect(data).mapper.column_attrs
                if getattr(data, c.key) is not None
            }

            for key, value in data_dict.items():
                setattr(db_user, key, value)
            self.session.commit()
            user = UserPersistanceAdapter.persistance_to_domain(db_user)
            return user
        else:
            raise Exception("User not found")

    def delete(self, id: int) -> None:
        db_user = self.session.get(UserSQL, id)
        if db_user and not db_user.deleted_date:
            db_user.deleted_date = datetime.now()
            self.session.commit()
