from domain.interfaces.repository import IRepository
from domain.interfaces.hash_service import IHashService
from domain.models.user import User


class AuthService:
    def __init__(
        self,
        user_repository: IRepository,
        hash_service: IHashService,
    ):
        self.user_repository = user_repository
        self.hash_service = hash_service

    def login(self, username: str, password: str) -> User | None:
        user = self.user_repository.get(username=username)

        if not user:
            return None

        if not self.hash_service.verify(password, user.password):
            return None

        return user
