from datetime import datetime
import pytest

from domain.models.user import User
from domain.models.role import Role
from domain.models.permission import Permission
from domain.models.value_objects import (
    Id,
    Username,
    Name,
    Description,
    Email,
    Password,
)


@pytest.fixture(scope="function")
def domain_permission():
    return Permission(
        id=Id(value=1),
        name=Name(value="testpermission"),
        description=Description(value="testdescription"),
        created_date=datetime.now(),
        updated_date=datetime.now(),
    )


@pytest.fixture(scope="function")
def domain_role():
    return Role(
        id=Id(value=1),
        name=Name(value="testrole"),
        permission_ids=[Id(value=1), Id(value=2)],
        created_date=datetime.now(),
        updated_date=datetime.now(),
    )


@pytest.fixture(scope="function")
def domain_user():
    return User(
        username=Username(value="testusername"),
        password=Password(value="testpw"),
        email=Email(value="liomessi@gmail.com"),
        id=Id(value=1),
        active=True,
        role_ids=[Id(value=1), Id(value=2)],
        created_date=datetime.now(),
        updated_date=datetime.now(),
    )
