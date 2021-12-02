from typing import List

from System.custom_exceptions.duplicate_account_name_exception import DuplicateAccountNameException
from System.data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
from System.entities.accounts import Account
from System.service_layer.abstract_services.account_service import AccountService


class AccountServiceImp(AccountService):
    # business logic: accounts must not have the same name

    def __init__(self, account_dao: AccountDAOImp):
        self.account_dao = account_dao

    def service_create_account(self, account: Account) -> Account:
        for existing_account in self.account_dao.account_list:
            if existing_account.name == account.name:
                raise DuplicateAccountNameException("You can not use that name: it is already taken")
        new_account = self.account_dao.create_account(account)
        return new_account

    def service_get_account_by_id(self, account_id: int) -> Account:
        return self.account_dao.get_account_by_id(account_id)

    def service_get_all_account(self) -> List[Account]:
        return self.account_dao.get_all_account()

    def service_update_account_by_id(self, account: Account) -> Account:
        for existing_account in self.account_dao.account_list:
            if existing_account.account_id != account.account_id:
                if existing_account.name == account.name:
                    raise DuplicateAccountNameException("You can not use that name: it is already taken")
        updated_account = self.account_dao.update_account_by_id(account)
        return updated_account

    def service_delete_account_by_id(self, account_id: int) -> bool:
        return self.account_dao.delete_account_by_id(account_id)
