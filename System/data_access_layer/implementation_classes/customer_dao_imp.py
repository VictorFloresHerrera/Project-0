from System.data_access_layer.abstract_classes.customer_dao import CustomerDAO
from System.entities.customers import Customer


class CustomerDAOImp(CustomerDAO):
    # Theres customers are premade so that we can test our methods
    premade_customer = Customer("premade", "Customer", 100, 1, 1)
    # Temporary
    premade_customer_two = Customer("added for", "testing purpose", 101, 2, 1)
    to_delete = Customer("I exist", "to be deleted", 0, 3, 1)
    # we are going to use this list as our "database"
    customer_list = [premade_customer, premade_customer_two, to_delete]
    # we are going to use this value to assign unique customer ids
    customer_id_generator = 4

    def create_customer_entry(self, customer: Customer) -> Customer:
        customer.customer_id = CustomerDAOImp.customer_id_generator
        CustomerDAOImp.customer_id_generator += 1
        CustomerDAOImp.customer_list.append(customer)
        return customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        for customer in CustomerDAOImp.customer_list:
            if customer.customer_id == customer_id:
                return customer

    def get_all_customers_information(self) -> list[Customer]:
        return CustomerDAOImp.customer_list

    def update_customer_by_id(self, customer: Customer) -> Customer:
        for customer_in_list in CustomerDAOImp.customer_list:
            if customer_in_list.customer_id == customer.customer_id:
                index = CustomerDAOImp.customer_list.index(customer_in_list)
                CustomerDAOImp.customer_list[index] = customer
                return customer

    def delete_customer_by_id(self, customer_id: int) -> bool:
        for customer_in_list in CustomerDAOImp.customer_list:
            if customer_in_list.customer_id == customer_id:
                index = CustomerDAOImp.customer_list.index(customer_in_list)
                del CustomerDAOImp.customer_list[index]
                return True
