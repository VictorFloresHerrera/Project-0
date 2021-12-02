from System.custom_exceptions.duplicate_account_name_exception import DuplicateAccountNameException
from System.data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
from System.entities.accounts import Account
from System.service_layer.implementation_services.account_service_imp import AccountServiceImp

account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)

bad_account = Account(0, "duplicate name")
bad_update_account = Account(1, "duplicate name")


def test_catch_creating_account_with_duplicate_name():
    try:
        account_service.service_create_account(bad_account)
        assert False
    except DuplicateAccountNameException as e:
        assert str(e) == "You can not use that name: it is already taken"


def test_catch_updating_account_with_duplicate_name():
    try:
        account_service.service_update_account_by_id(bad_update_account)
        assert False
    except DuplicateAccountNameException as e:
        assert str(e) == "You can not use that name: it is already taken"
