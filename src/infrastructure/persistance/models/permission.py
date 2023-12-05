from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistance.base import SQLBaseModel
from infrastructure.persistance.models.role import role_permission_association, RoleSQL


class PermissionSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    description: Mapped[str] = mapped_column(String)

    roles: Mapped[list[RoleSQL]] = relationship(
        "RoleSQL",
        secondary=role_permission_association,
        back_populates="permissions",
        viewonly=True,
    )
