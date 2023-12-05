from sqlalchemy import String, Integer, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy.ext.associationproxy import association_proxy

from infrastructure.persistance.base import SQLBaseModel, Base
from infrastructure.persistance.models.user import user_role_association


role_permission_association = Table(
    'role_permission', SQLBaseModel.metadata,
    Column('role_id', Integer, ForeignKey('role.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permission.id'), primary_key=True)
)



class RoleSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    users = relationship(
        "UserSQL",
        secondary=user_role_association,
        back_populates="roles",
        viewonly=True,
    )

    permissions: Mapped[list["PermissionSQL"]] = relationship(
        "PermissionSQL",
        secondary=role_permission_association,
        back_populates="roles",
        viewonly=True,
    )
    permission_associations: Mapped[list["PermissionAssociation"]] = relationship(
        "PermissionAssociation",
        back_populates="role",
        cascade="all, delete-orphan",
    )
    permission_ids: Mapped[list[int]] = association_proxy(
        "permission_associations",
        "permission_id",
        creator=lambda permission_id: PermissionAssociation(permission_id=permission_id),
    )


class PermissionAssociation(Base):
    __table__ = role_permission_association
    role: Mapped[RoleSQL] = relationship(
        RoleSQL,
        back_populates="permission_associations"
    )