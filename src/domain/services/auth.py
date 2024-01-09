from datetime import datetime, timedelta

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

    def authenticate(self, username: str, password: str) -> User | None:
        user = self.user_repository.get(username=username)

        if not user:
            return None

        if not self.hash_service.verify(password, user.password):
            return None

        return user

    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt