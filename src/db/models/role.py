from sqlalchemy import String, Integer, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


role_permission_association = Table(
    'role_permission', Base.metadata,
    mapped_column('role_id', Integer, ForeignKey('role.id')),
    mapped_column('permission_id', Integer, ForeignKey('permission.id'))
)


class Role(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    permissions: Mapped = relationship("Permission", secondary=role_permission_association)
