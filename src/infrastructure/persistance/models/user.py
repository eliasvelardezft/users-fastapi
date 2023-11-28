from sqlalchemy import String, Integer, ForeignKey, Table, Boolean
from sqlalchemy.orm import Mapped, relationship, mapped_column

from infrastructure.persistance.base import SQLBaseModel


user_role_association = Table(
    'user_role', SQLBaseModel.metadata,
    mapped_column('user_id', Integer, ForeignKey('users.id')),
    mapped_column('role_id', Integer, ForeignKey('roles.id'))
)


class User(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    roles: Mapped = relationship("Role", secondary=user_role_association)
