from domain.models.user import User
from infrastructure.persistance.adapters.user import UserPersistanceAdapter
from infrastructure.persistance.models.user import UserSQL
from test.conftest import BaseTestClass


class TestUserPersistanceAdapter(BaseTestClass):
    def test_domain_to_persistance(self, domain_user):
        sql_user = UserPersistanceAdapter.domain_to_persistance(domain_user)

        assert isinstance(sql_user, UserSQL)
        assert sql_user.email == domain_user.email.value
        assert sql_user.username == domain_user.username.value
        assert sql_user.active == domain_user.active
        assert sql_user.role_ids == [id.value for id in domain_user.role_ids]
        assert sql_user.created_date == domain_user.created_date
        assert sql_user.updated_date == domain_user.updated_date
        assert sql_user.deleted_date == domain_user.deleted_date

    def test_persistance_to_domain(self, sql_user):
        domain_user = UserPersistanceAdapter.persistance_to_domain(sql_user)

        assert isinstance(domain_user, User)
        assert domain_user.id.value == sql_user.id
        assert domain_user.email.value == sql_user.email
        assert domain_user.username.value == sql_user.username
        assert domain_user.active == sql_user.active
        assert [id.value for id in domain_user.role_ids] == sql_user.role_ids
        assert domain_user.created_date == sql_user.created_date
        assert domain_user.updated_date == sql_user.updated_date
        assert domain_user.deleted_date == sql_user.deleted_date
