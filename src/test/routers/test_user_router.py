import json
from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient

from api.v1.dtos.user import UserCreate
from domain.models.value_objects import ComparisonOperator
from test.conftest import BaseTestClass


class TestUserRouter(BaseTestClass):
    base_url = "/api/v1/users"

    def test_create(
        self,
        client: TestClient,
        user_create: UserCreate
    ):
        response = client.post(
            self.base_url,
            json=user_create.model_dump(),
        )
        assert response.status_code == 200
        assert response.json()["username"] == user_create.username

    def test_get(self, client: TestClient):
        self._load_test_data()

        response = client.get(f"{self.base_url}/1")
        assert response.status_code == 200
        assert response.json()["username"] == "testusername"

    def test_get_all(self, client: TestClient):
        self._load_test_data()

        response = client.get(self.base_url)
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_get_filter_exact_comparison(self, client: TestClient):
        self._load_test_data()

        filters = {
            "username": {
                "value": "testusername",
                "comparison_operator": ComparisonOperator.EQ,
            }
        }
        params = {
            "filters": json.dumps(filters)
        }
        response = client.get(f"{self.base_url}", params=params)
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["username"] == "testusername"


    @pytest.mark.skip(reason="filter by included Not implemented yet")    
    def test_get_filter_in_comparison(self, client: TestClient):
        self._load_test_data()

        filters = {
            "id": {
                "list": [1, 2],
                "included": True,
            }
        }
        params = {
            "filters": json.dumps(filters)
        }
        response = client.get(f"{self.base_url}", params=params)
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_get_filter_date_range(self, client: TestClient):
        self._load_test_data()

        yesterday = datetime.now() - timedelta(days=1)
        tomorrow = datetime.now() + timedelta(days=1)

        filters = {
            "created_date": {
                "start": yesterday.isoformat(),
                "end": tomorrow.isoformat(),
            }
        }
        params = {
            "filters": json.dumps(filters)
        }

        response = client.get(f"{self.base_url}", params=params)
        assert response.status_code == 200
        assert len(response.json()) == 2


    def test_update(self, client: TestClient):
        self._load_test_data()

        response = client.patch(
            f"{self.base_url}/1",
            json={
                "username": "elias",
                "email": "update_testemail@gmail.com",
            },
        )
        assert response.status_code == 200
        assert response.json()["username"] == "elias"
        assert response.json()["email"] == "update_testemail@gmail.com"

    def test_delete(self, client: TestClient):
        self._load_test_data()

        response = client.delete(f"{self.base_url}/1")
        assert response.status_code == 200

        response = client.get(f"{self.base_url}/1")
        assert response.status_code == 404
