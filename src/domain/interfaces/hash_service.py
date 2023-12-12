from abc import ABC

from domain.models.value_objects import Password


class IHashService(ABC):
    def get_hash(self, password: str) -> str:
        raise NotImplementedError

    def verify(self, Password: str, hashed_password: str) -> bool:
        raise NotImplementedError
