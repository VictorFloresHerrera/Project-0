from System.data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
from System.entities.accounts import Account

account_dao = AccountDAOImp()
test_account = Account(0, "test account")
updated_account = Account(2, "updated account")


def test_create_account_success():
    created_account = account_dao.create_account(test_account)
    assert created_account.account_id != 0


def test_select_account_by_id_success():
    selected_account = account_dao.get_account_by_id(1)
    assert selected_account.account_id == 1


def test_select_all_accounts_success():
    accounts = account_dao.get_all_account()
    assert len(accounts) >= 2


def test_update_account_success():
    result = account_dao.update_account_by_id(updated_account)
    assert result.name == "updated account"


def test_delete_account_success():
    result = account_dao.delete_account_by_id(3)
    assert result
