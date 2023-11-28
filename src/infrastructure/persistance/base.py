from datetime import datetime
import re

from sqlalchemy import event, DateTime, Column, create_engine, inspect
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, sessionmaker

from config import settings


def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


class Base(DeclarativeBase):
    pass


class SQLBaseModel(Base):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        class_name = cls.__name__
        if class_name.endswith("SQL"):
            class_name = class_name[:-3]
        return camel_to_snake(class_name)

    created_date: Mapped[datetime] = Column(
        DateTime(timezone=True), default=datetime.utcnow
    )
    updated_date: Mapped[datetime] = Column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    deleted_date: Mapped[datetime] = Column(
        DateTime(timezone=True), index=True
    )

    def as_dict(self):
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self).mapper.column_attrs
        }


@event.listens_for(SQLBaseModel, "before_update", propagate=True)
def updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
