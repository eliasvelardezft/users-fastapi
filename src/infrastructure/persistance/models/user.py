from sqlalchemy import String, Integer, ForeignKey, Table, Boolean, Column
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import Mapped, relationship, mapped_column

from infrastructure.persistance.base import SQLBaseModel, Base


user_role_association = Table(
    'user_role_association',
    SQLBaseModel.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('role.id'), primary_key=True)
)


class UserSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    roles: Mapped[list["RoleSQL"]] = relationship(
        "RoleSQL",
        secondary=user_role_association,
        back_populates="users",
        viewonly=True,
    )
    role_associations: Mapped[list["RoleAssociation"]] = relationship(
        "RoleAssociation",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    role_ids: Mapped[list[int]] = association_proxy(
        "role_associations",
        "role_id",
        creator=lambda role_id: RoleAssociation(role_id=role_id),
    )


class RoleAssociation(Base):
    __table__ = user_role_association
    user: Mapped[UserSQL] = relationship(
        UserSQL,
        back_populates="role_associations"
    )