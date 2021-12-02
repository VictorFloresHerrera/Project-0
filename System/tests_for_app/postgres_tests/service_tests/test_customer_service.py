from System.custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException
from System.entities.customers import Customer
from System.service_layer.implementation_services.customer_postgres_dao import CustomerPostgresDAO
from System.service_layer.implementation_services.customer_postgres_service import CustomerPostgresService

customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresService(customer_dao)

customer_with_duplicate_account = Customer("first", "last", 200, 0, 1)


def test_catch_duplicate_account_number_for_create_method():
    try:
        customer_service.service_create_customer_entry(customer_with_duplicate_account)
        assert False
    except DuplicateAccountNumberException as e:
        assert str(e) == "Account number is already taken!"


def test_catch_duplicate_account_number_for_update_method():
    try:
        customer_service.service_update_customer_by_id(customer_with_duplicate_account)
        assert False
    except DuplicateAccountNumberException as e:
        assert str(e) == "Account number is already taken!"
