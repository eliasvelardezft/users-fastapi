from sqlalchemy import String, Integer, ForeignKey, Table, Boolean, Column
from sqlalchemy.orm import Mapped, relationship, mapped_column

from infrastructure.persistance.base import SQLBaseModel
from infrastructure.persistance.models import RoleSQL


user_role_association = Table(
    'user_role', SQLBaseModel.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('role_id', Integer, ForeignKey('role.id'))
)


class UserSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    roles: Mapped[list[RoleSQL]] = relationship("Role", secondary=user_role_association)
