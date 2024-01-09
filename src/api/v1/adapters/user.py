from domain.interfaces.adapters.client_adapter import IClientAdapter
from domain.models.user import User
from domain.models.value_objects import Email, Password, Username, Id
from api.v1.dtos.user import UserCreate, UserRead

class UserClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(user: UserCreate) -> User:
        return User(
            username=Username(value=user.username),
            password=Password(value=user.password),
            email=Email(value=user.email),
            role_ids=[Id(value=role_id) for role_id in user.role_ids]
        )

    @staticmethod
    def domain_to_client(user: User) -> UserRead:
        return UserRead(
            id=user.id.value,
            username=user.username.value,
            email=user.email.value,
            role_ids=[role_id.value for role_id in user.role_ids],
            created_date=user.created_date,
            updated_date=user.updated_date,
            deleted_date=user.deleted_date,
        )

    @staticmethod
    def update_to_domain(user: User, update_data: dict) -> User:
        username = update_data.get("username", user.username.value)
        password = update_data.get("password", user.password.value)
        email = update_data.get("email", user.email.value)
        role_ids = [
            Id(value=role_id)
            for role_id
            in update_data.get(
                "role_ids",
                [role_id.value for role_id in user.role_ids]
            )
        ]
        return User(
            id=user.id,
            username=Username(value=username),
            password=Password(value=password),
            email=Email(value=email),
            role_ids=role_ids,
            created_date=user.created_date,
            updated_date=user.updated_date,
            deleted_date=user.deleted_date,
        )