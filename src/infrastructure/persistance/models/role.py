from sqlalchemy import String, Integer, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, relationship, mapped_column

from infrastructure.persistance.base import SQLBaseModel
from infrastructure.persistance.models import PermissionSQL


role_permission_association = Table(
    'role_permission', SQLBaseModel.metadata,
    Column('role_id', Integer, ForeignKey('role.id')),
    Column('permission_id', Integer, ForeignKey('permission.id'))
)


class RoleSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    permissions: Mapped[list[PermissionSQL]] = relationship("Permission", secondary=role_permission_association)
