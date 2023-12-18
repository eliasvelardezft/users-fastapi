import json
from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient

from api.v1.dtos.role import RoleCreate
from domain.models.value_objects import ComparisonOperator
from test.conftest import BaseTestClass


class TestRoleRouter(BaseTestClass):
    base_url = "/api/v1/roles"

    def test_create(
        self,
        client: TestClient,
        role_create: RoleCreate
    ):
        response = client.post(
            self.base_url,
            json=role_create.model_dump(),
        )
        assert response.status_code == 200
        assert response.json()["name"] == role_create.name

    def test_get(self, client: TestClient):
        self._load_test_data()

        response = client.get(f"{self.base_url}/1")
        assert response.status_code == 200
        assert response.json()["name"] == "testrole"

    def test_get_all(self, client: TestClient):
        self._load_test_data()

        response = client.get(self.base_url)
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_get_filter_exact_comparison(self, client: TestClient):
        self._load_test_data()

        filters = {
            "name": {
                "value": "testrole",
                "comparison_operator": ComparisonOperator.EQ,
            }
        }
        params = {
            "filters": json.dumps(filters)
        }
        response = client.get(f"{self.base_url}", params=params)
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["name"] == "testrole"


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
                "name": "update_testrole",
                "description": "update_testrole_description",
            },
        )
        assert response.status_code == 200
        assert response.json()["name"] == "update_testrole"

    def test_delete(self, client: TestClient):
        self._load_test_data()

        response = client.delete(f"{self.base_url}/1")
        assert response.status_code == 200