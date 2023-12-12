from typing import Any

from psycopg2 import errors
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from domain.interfaces.repository import IRepository
from domain.models.user import User
from domain.exceptions import InvalidFilter
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

    def filter(self, filters: dict[str, Any] = {}) -> list[User]:
        query = self.session.query(UserSQL)
        for key, value in filters.items():
            try:
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
            except:
                pass
            # except errors.ForeignKeyViolation:
            #     raise UserDoesNotExist
            # except errors.UniqueViolation:
            #     raise UserAlreadyHasUser
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
            except:
                pass
            # except errors.ForeignKeyViolation:
            #     raise UserDoesNotExist
            # except errors.UniqueViolation:
            #     raise UserAlreadyHasUser

        users = [
            UserPersistanceAdapter.persistance_to_domain(user)
            for user in db_users
        ]
        return users
