from domain.interfaces.adapters.client_adapter import IClientAdapter
from domain.models.user import User
from domain.models.value_objects import Email, Password, Username, Id
from api.v1.dtos.user import UserCreate, UserRead, UserUpdate


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
    def update_to_domain(user: User, user_update: UserUpdate) -> User:
        user.username = Username(value=user_update.username) if user_update.username else user.username
        user.password = Password(value=user_update.password) if user_update.password else user.password
        user.email = Email(value=user_update.email) if user_update.email else user.email
        user.active = user_update.active if user_update.active is not None else user.active
        return user
