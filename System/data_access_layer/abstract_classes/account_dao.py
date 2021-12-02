from abc import ABC, abstractmethod
from typing import List

from System.entities.accounts import Account


class AccountDAO(ABC):

    # create Account
    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    # get Account
    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    # get all account info
    @abstractmethod
    def get_all_account(self) -> List[Account]:
        pass

    # update Account
    @abstractmethod
    def update_account_by_id(self, account: Account) -> Account:
        pass

    # delete Account
    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass
