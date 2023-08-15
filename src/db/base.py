from datetime import datetime
import re

from sqlalchemy import create_engine, event, DateTime, Column
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase


def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


class Base(DeclarativeBase):
    pass


class SQLBaseModel(Base):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return camel_to_snake(cls.__name__)

    created_date: datetime = Column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )
    updated_date: datetime = Column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    deleted_date: datetime = Column(DateTime(timezone=True))


@event.listens_for(SQLBaseModel, "before_update", propagate=True)
def updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()
