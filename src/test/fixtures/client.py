from typing import Generator

import pytest
from fastapi.testclient import TestClient

from api.v1.dependencies.services import (
    get_permission_service,
    get_role_service,
    get_user_service,
    get_auth_service
)
from main import app


@pytest.fixture(scope="function")
def client(test_session) -> Generator[TestClient, None, None]:
    app.dependency_overrides[get_permission_service] = lambda: get_permission_service(test_session)
    app.dependency_overrides[get_role_service] = lambda: get_role_service(test_session)
    app.dependency_overrides[get_user_service] = lambda: get_user_service(test_session)
    app.dependency_overrides[get_auth_service] = lambda: get_auth_service(test_session)

    with TestClient(app) as c:
        yield c
