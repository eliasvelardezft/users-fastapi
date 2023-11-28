from sqlalchemy import String, DateTime, Integer, ForeignKey, Table
from sqlalchemy.orm import Mapped, relationship, mapped_column

from db.base import Base


user_role_association = Table(
    'user_role', Base.metadata,
    mapped_column('user_id', Integer, ForeignKey('users.id')),
    mapped_column('role_id', Integer, ForeignKey('roles.id'))
)


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)
    created_date: Mapped[str] = mapped_column(DateTime)
    active: Mapped[bool] = mapped_column(bool, default=True)

    roles: Mapped = relationship("Role", secondary=user_role_association)
