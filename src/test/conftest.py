from glob import glob

import pytest
from sqlalchemy.orm import Session

from infrastructure.persistance.models.permission import PermissionSQL
from infrastructure.persistance.models.role import RoleSQL
from infrastructure.persistance.models.user import UserSQL
from test.fixtures.db import seed_db

class BaseTestClass:
    def _load_permissions(self):
        sql_permissions = [
            PermissionSQL(
                name="testpermission",
                description="testdescription",
            ),
            PermissionSQL(
                name="testpermission_2",
                description="testdescription_2",
            )
        ]
        seed_db(self.session, sql_permissions)
        return sql_permissions

    def _load_roles(self, sql_permissions):
        sql_roles = [
            RoleSQL(
                name="testrole",
                permission_ids=[permission.id for permission in sql_permissions],
            ),
            RoleSQL(
                name="testrole_2",
                permission_ids=[permission.id for permission in sql_permissions],
            )
        ]
            
        seed_db(self.session, sql_roles)
        return sql_roles

    def _load_users(self, sql_roles):
        sql_users = [
            UserSQL(
                active=True,
                username="testusername",
                password="testpw",
                email="liomessi@gmail.com",
                role_ids=[role.id for role in sql_roles],
            ),
            UserSQL(
                active=True,
                username="testusername_2",
                password="testpw_2",
                email="charlygarcia@gmail.com",
                role_ids=[sql_roles[0].id],
            )
        ]
        seed_db(self.session, sql_users)
        return sql_users

    def _load_test_data(self):
        sql_permissions = self._load_permissions()
        sql_roles = self._load_roles(sql_permissions=sql_permissions)
        self._load_users(sql_roles=sql_roles)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, test_session: Session):
        self.session = test_session


def refactor(string: str) -> str:
    return string.replace("/", ".").replace("\\", ".").replace(".py", "")


pytest_plugins = [
    refactor(fixture)
    for fixture in glob("test/fixtures/*.py")
    if "__" not in fixture
]
