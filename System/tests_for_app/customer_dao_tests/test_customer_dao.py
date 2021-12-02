from System.data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from System.entities.customers import Customer
# from System.service_layer.implementation_services.customer_postgres_dao import CustomerPostgresDAO

customer_dao_imp = CustomerDAOImp()
# customer_dao_postgres = CustomerPostgresDAO()
customer = Customer("Victor", "Flores", 100, 0, 10)


# customer_for_postgres = Customer("Jocey", "Flores", 18, 0, 1)


def test_create_customer_success():
    new_customer = customer_dao_imp.create_customer_entry(customer)
    for customers in customer_dao_imp.customer_list:
        print(customers)
    # new_customer: Customer = customer_dao_postgres.create_customer_entry(customer_for_postgres)  # imp #customer_for
    print(new_customer)  # print(new_customer.customer_id)
    assert new_customer.customer_id != 0  # assert new_customer.customer_id != 0


def test_get_customer_success():
    returned_customer: Customer = customer_dao_imp.get_customer_by_id(
        1)  # returned_customer: Customer = customer_dao_postgres.get_customer_by_id(1)
    assert returned_customer.customer_id == 1


def test_get_all_customers_success():
    customer_list = customer_dao_imp.get_all_customers_information()  # customer_list = customer_dao_postgres.get_all_customers_information()

    assert len(customer_list) >= 1  # depending how many in list (trainer default 2)


def test_update_customer_success():
    update_info = Customer("Changed by", "update customer method", 200, 1, 10)
    updated_customer: Customer = customer_dao_imp.update_customer_by_id(update_info)
    assert updated_customer.account_number == update_info.account_number


def test_delete_customer_success():
    confirm_customer_deleted = customer_dao_imp.delete_customer_by_id(3)
    assert confirm_customer_deleted
