from sqlalchemy import String, Integer, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistance.base import SQLBaseModel


role_permission_association = Table(
    'role_permission', SQLBaseModel.metadata,
    mapped_column('role_id', Integer, ForeignKey('role.id')),
    mapped_column('permission_id', Integer, ForeignKey('permission.id'))
)


class Role(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    permissions: Mapped = relationship("Permission", secondary=role_permission_association)
