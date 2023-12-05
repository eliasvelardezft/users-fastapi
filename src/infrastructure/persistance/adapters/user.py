from domain.models.user import User
from domain.models.value_objects import Email, Id, Username, Password
from domain.interfaces.adapters.persistance_adapter import IPersistanceAdapter
from infrastructure.persistance.models import UserSQL
from infrastructure.persistance.adapters.role import RolePersistanceAdapter


class UserPersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(
        user: User,
    ) -> UserSQL:
        return UserSQL(
            id=user.id.value,
            active=user.active,
            username=user.username.value,
            password=user.password.value,
            email=user.email.value,
            role_ids=[user_id.value for user_id in user.role_ids],
            created_date=user.created_date,
            updated_date=user.updated_date,
            deleted_date=user.deleted_date,
        )

    @staticmethod
    def persistance_to_domain(
        user: UserSQL,
    ) -> User:
        domain_roles = [
            RolePersistanceAdapter.persistance_to_domain(role)
            for role in user.roles
        ]
        domain_role_ids = [Id(value=role_id) for role_id in user.role_ids]
        return User(
            id=Id(value=user.id),
            email=Email(value=user.email),
            username=Username(value=user.username),
            password=Password(value=user.password),
            active=user.active,
            role_ids=domain_role_ids,
            roles=domain_roles,
            created_date=user.created_date,
            updated_date=user.updated_date,
            deleted_date=user.deleted_date,
        )
