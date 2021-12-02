from abc import ABC, abstractmethod

from System.entities.customers import Customer


class CustomerDAO(ABC):

    # create customer method?
    @abstractmethod
    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    # View my personal information
    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    # get all customers information
    @abstractmethod
    def get_all_customers_information(self) -> list[Customer]:
        pass

    # Update personal information
    @abstractmethod
    def update_customer_by_id(self, customer: Customer) -> Customer:
        pass

    # End business relationship with the place
    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
