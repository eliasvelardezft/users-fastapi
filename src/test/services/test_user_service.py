from domain.services.user import UserService
from domain.models.user import User


class TestUserService:
    def test_create_user(
        self,
        test_user_service: UserService,
        domain_user: User
    ):
        user = test_user_service.create_user(user=domain_user)
        assert user.username == domain_user.username
        assert user.password == domain_user.password
        assert user.email == domain_user.email

    def test_get_users(
        self,
        test_user_service: UserService,
        domain_user: User
    ):
        test_user_service.create_user(user=domain_user)
        users = test_user_service.get_users()
        assert len(users) == 1
