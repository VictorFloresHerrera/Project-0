from System.custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException
from System.data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from System.entities.customers import Customer
from System.service_layer.implementation_services.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
customer = Customer("service", "testing", 100, 0, 1)
customer_update = Customer("Update", "test", 100, 2, 1)


def test_validate_create_customer_method():
    try:
        customer_service.service_create_customer_entry(customer)
        assert False
    except DuplicateAccountNumberException as e:
        assert str(e) == "Account number is already taken!"


def test_validate_update_customer_method():
    try:
        customer_service.service_update_customer_by_id(customer_update)
        assert False
    except DuplicateAccountNumberException as e:
        assert str(e) == "Account number is already taken!"
