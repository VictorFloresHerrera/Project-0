from typing import List

from System.data_access_layer.abstract_classes.account_dao import AccountDAO
from System.entities.accounts import Account


class AccountDAOImp(AccountDAO):
    # Need to add premade data for tests when they are created
    account_one = Account(1, "first account")
    account_two = Account(2, "second account")
    account_three = Account(3, "to be deleted")
    account_four = Account(4, "duplicate name")
    account_list = [account_one, account_two, account_three, account_four]
    account_id_generator = 5

    def create_account(self, account: Account) -> Account:
        new_account = account
        new_account.account_id = AccountDAOImp.account_id_generator
        AccountDAOImp.account_id_generator += 1
        AccountDAOImp.account_list.append(new_account)
        return new_account

    def get_account_by_id(self, account_id: int) -> Account:
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                return account

    def get_all_account(self) -> List[Account]:
        return AccountDAOImp.account_list

    def update_account_by_id(self, account: Account) -> Account:
        for account_in_list in AccountDAOImp.account_list:
            if account_in_list.account_id == account.account_id:
                account_in_list.name = account.name
                return account_in_list

    def delete_account_by_id(self, account_id: int) -> bool:
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                index = AccountDAOImp.account_list.index(account)
                del AccountDAOImp.account_list[index]
                return True
