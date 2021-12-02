from System.custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException
from System.entities.customers import Customer
from System.service_layer.abstract_services.customer_service import CustomerService
from System.service_layer.implementation_services.customer_postgres_dao import CustomerPostgresDAO


class CustomerPostgresService(CustomerService):
    def __init__(self, customer_dao: CustomerPostgresDAO):
        self.customer_dao = customer_dao

    # need to check and make sure customers do not have the same account number
    def service_create_customer_entry(self, customer: Customer) -> Customer:
        customers = self.customer_dao.get_all_customers_information()
        for existing_customer in customers:
            if existing_customer.account_id == customer.account_id:  # BANK
                if existing_customer.account_number == customer.account_number:
                    raise DuplicateAccountNumberException("Account number is already taken!")
        created_customer = self.customer_dao.create_customer_entry(customer)
        return created_customer

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_by_id(customer_id)

    def service_get_all_customers_information(self) -> list[Customer]:
        return self.customer_dao.get_all_customers_information()

    # need to check and make sure customers do not have the same account number
    def service_update_customer_by_id(self, customer: Customer) -> Customer:
        customers = self.customer_dao.get_all_customers_information()
        for current_customer in customers:
            if current_customer.account_id == customer.account_id:  # BANK
                if current_customer.customer_id != customer.customer_id:
                    if current_customer.account_number == customer.account_number:
                        raise DuplicateAccountNumberException("Account number is already taken!")
        updated_customer = self.customer_dao.update_customer_by_id(customer)
        return updated_customer

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_by_id(customer_id)
