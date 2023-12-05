from glob import glob

import pytest
from sqlalchemy.orm import Session

from test.fixtures.db import seed_db


class BaseTestClass:
    def _load_permissions(self, sql_permission):
        permission_1 = sql_permission

        permission_2 = sql_permission.copy()
        permission_2.id = 2
        permission_2.name = "testpermission_2"
        permission_2.description = "testdescription_2"

        seed_db(self.session, [permission_1, permission_2])

        return [permission_1, permission_2]

    def _load_roles(self, sql_role):
        role_1 = sql_role

        role_2 = sql_role.copy()
        role_2.id = 2
        role_2.name = "testrole_2"

        seed_db(self.session, [role_1, role_2])

        return [role_1, role_2]

    def _load_user(self, sql_user):
        seed_db(self.session, [sql_user])

        return sql_user

    def _load_test_data(self):
        self._load_permissions()
        self._load_roles()
        self._load_user()

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
