from domain.models.user import User
from api.v1.adapters.user import UserClientAdapter
from api.v1.dtos.user import UserRead, UserCreate
from test.conftest import BaseTestClass


class TestUserClientAdapter(BaseTestClass):
    def test_client_to_domain(self, user_create):
        domain_user = UserClientAdapter.client_to_domain(user_create)

        assert isinstance(domain_user, User)
        assert domain_user.username.value == user_create.username
        assert domain_user.password.value == user_create.password
        assert domain_user.email.value == user_create.email

    def test_domain_to_client(self, domain_user):
        user_read = UserClientAdapter.domain_to_client(domain_user)

        assert isinstance(user_read, UserRead)
        assert user_read.id == domain_user.id.value
        assert user_read.username == domain_user.username.value
        assert user_read.email == domain_user.email.value
        assert user_read.role_ids == [role_id.value for role_id in domain_user.role_ids]
        assert user_read.created_date == domain_user.created_date
        assert user_read.updated_date == domain_user.updated_date
        assert user_read.deleted_date == domain_user.deleted_date