from System.custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException
from System.data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from System.entities.customers import Customer
from System.service_layer.abstract_services.customer_service import CustomerService

"""
we are going to make use of dependency injection with our service class. This allows us to easily change the
implementation of our code by switching out the implementing class. switching from a local to a cloud base database?
just pass in a could based implementation object into the service layer instead of a local based implementation object
"""


# Business Logic : Customers should have unique account balance numbers on the same account


class CustomerServiceImp(CustomerService):
    def __init__(self, customer_dao):
        # we are doing dependency injection with this init dunder method
        self.customer_dao: CustomerDAOImp = customer_dao

    def service_create_customer_entry(self, customer: Customer) -> Customer:
        # need to implement business logic
        for current_customer in self.customer_dao.customer_list:
            if current_customer.account_id == customer.account_id: # BANK
                if current_customer.customer_id != customer.customer_id:
                    if current_customer.account_number == customer.account_number:
                            raise DuplicateAccountNumberException("Account number is already taken!")
        return self.customer_dao.create_customer_entry(customer)

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_by_id(customer_id)

    def service_get_all_customers_information(self) -> list[Customer]:
        return self.customer_dao.get_all_customers_information()

    def service_update_customer_by_id(self, customer: Customer) -> Customer:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.account_id == customer.account_id: # BANK
                if current_customer.account_number == customer.account_number:
                    raise DuplicateAccountNumberException("Account number is already taken!")
        return self.customer_dao.update_customer_by_id(customer)

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_by_id(customer_id)
