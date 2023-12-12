from domain.interfaces.hash_service import IHashService
from domain.models.value_objects import Password


class HashService(IHashService):
    def get_hash(self, str_password: str) -> str:
        # TODO: implement in auth branch
        return str_password + "hashed"

    def verify(self, password: Password, hashed_password: str) -> bool:
        # TODO: implement in auth branch
        return self.get_hash(password.value) == hashed_password
