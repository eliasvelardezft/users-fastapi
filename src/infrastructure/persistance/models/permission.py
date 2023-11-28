from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.persistance.base import SQLBaseModel


class PermissionSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    description: Mapped[str] = mapped_column(String)
