import json
from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient

from api.v1.dtos.permission import PermissionCreate
from domain.models.value_objects import ComparisonOperator
from test.conftest import BaseTestClass


class TestPermissionRouter(BaseTestClass):
    base_url = "/api/v1/permissions"

    def test_create(
        self,
        client: TestClient,
        permission_create: PermissionCreate
    ):
        response = client.post(
            self.base_url,
            json=permission_create.model_dump(),
        )
        assert response.status_code == 201
        assert response.json()["name"] == permission_create.name

    def test_get(self, client: TestClient):
        self._load_permissions()

        response = client.get(f"{self.base_url}/1")
        assert response.status_code == 200
        assert response.json()["name"] == "testpermission"

    def test_get_all(self, client: TestClient):
        self._load_permissions()

        response = client.get(self.base_url)
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_get_filter_exact_comparison(self, client: TestClient):
        self._load_permissions()

        filters = {
            "name": {
                "value": "testpermission",
                "comparison_operator": ComparisonOperator.EQ,
            }
        }
        params = {
            "filters": json.dumps(filters)
        }
        response = client.get(f"{self.base_url}", params=params)
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["name"] == "testpermission"


    @pytest.mark.skip(reason="filter by included Not implemented yet")    
    def test_get_filter_in_comparison(self, client: TestClient):
        self._load_permissions()

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
        self._load_permissions()

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
        self._load_permissions()

        response = client.patch(
            f"{self.base_url}/1",
            json={
                "name": "update_testpermission",
                "description": "update_testpermission_description",
            },
        )
        assert response.status_code == 200
        assert response.json()["name"] == "update_testpermission"

    def test_delete(self, client: TestClient):
        self._load_permissions()

        response = client.delete(f"{self.base_url}/1")
        assert response.status_code == 200