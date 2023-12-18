from domain.models.user import User
from domain.models.value_objects import (
    Email,
    Id,
    Username,
    Password,
    ComparisonOperator,
    QueryFilters,
)
from infrastructure.persistance.repositories.user import UserRepository
from test.conftest import BaseTestClass


class TestUserRepository(BaseTestClass):
    def test_create(self, test_user_repository: UserRepository):
        user = User(
            username=Username(value="create_testuser"),
            password=Password(value="create_testuser_password"),
            email=Email(value="create_testuser_email@gmail.com"),
        )
        test_user_repository.create(user)

        created_user = test_user_repository.get(1)
        assert user.username == created_user.username

    def test_filter(self, test_user_repository: UserRepository):
        self._load_test_data()

        filters_dict = {
            "filters": {
                "username": {
                    "value": "testusername_2",
                    "comparison_operator": ComparisonOperator.EQ,
                }
            }
        }
        filters = QueryFilters.model_validate(filters_dict)

        users = test_user_repository.filter(
            filters=filters
        )
        assert len(users) == 1
        assert users[0].id == Id(value=2)
        assert users[0].username == Username(value="testusername_2")

    def test_get(self, test_user_repository: UserRepository):
        self._load_test_data()

        user = test_user_repository.get(1)

        assert user is not None
        assert user.id == Id(value=1)
        assert user.username == Username(value="testusername")

    def test_bulk_create(self, test_user_repository: UserRepository):
        user_1 = User(
            username=Username(value="bulk_testuser"),
            password=Password(value="bulk_testuser_password"),
            email=Email(value="liomessi@gmail.com"),
        )
        user_2 = User(
            username=Username(value="bulk_testuser_2"),
            password=Password(value="bulk_testuser_2_password"),
            email=Email(value="charlygarcia@gmail.com"),
        )

        test_user_repository.bulk_create([user_1, user_2])

        created_users = test_user_repository.filter()

        assert len(created_users) == 2
        assert created_users[0].username == Username(value="bulk_testuser")
