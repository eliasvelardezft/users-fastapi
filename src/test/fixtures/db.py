import pytest
from typing import Generator
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from infrastructure.persistance.base import Base


@pytest.fixture(scope="session")
def sql_engine() -> Generator[Engine, None, None]:
    engine = create_engine("sqlite:///:memory:?check_same_thread=False")
    Base.metadata.create_all(engine)
    yield engine


@pytest.fixture(scope="function")
def test_session(sql_engine) -> Generator[Session, None, None]:
    connection = sql_engine.connect()

    connection.begin()

    db = Session(bind=connection)

    yield db

    db.rollback()
    connection.close()
