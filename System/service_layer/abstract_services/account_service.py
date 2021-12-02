from abc import ABC, abstractmethod
from typing import List

from System.entities.accounts import Account


class AccountService(ABC):

    # create Account
    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass

    # get Account
    @abstractmethod
    def service_get_account_by_id(self, account_id: int) -> Account:
        pass

    # get all account info
    @abstractmethod
    def service_get_all_account(self) -> List[Account]:
        pass

    # update Account
    @abstractmethod
    def service_update_account_by_id(self, account: Account) -> Account:
        pass

    # delete Account
    @abstractmethod
    def service_delete_account_by_id(self, account_id: int) -> bool:
        pass
