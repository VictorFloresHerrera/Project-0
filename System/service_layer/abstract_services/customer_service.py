from abc import ABC, abstractmethod

from System.entities.customers import Customer


class CustomerService(ABC):

    # create customer method?
    @abstractmethod
    def service_create_customer_entry(self, customer: Customer) -> Customer:
        pass

    # View my personal information
    @abstractmethod
    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    # get all customers information
    @abstractmethod
    def service_get_all_customers_information(self) -> list[Customer]:
        pass

    # Update personal information
    @abstractmethod
    def service_update_customer_by_id(self, customer: Customer) -> Customer:
        pass

    # End business relationship with the place
    @abstractmethod
    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        pass
