from System.data_access_layer.abstract_classes.customer_dao import CustomerDAO
from System.entities.customers import Customer
from System.util.database_connection import connection


class CustomerPostgresDAO(CustomerDAO):
    def create_customer_entry(self, customer: Customer) -> Customer:
        # we will use %s as placeholders for our values
        sql = "insert into customer values(%s, %s, %s, default, %s) returning customer_id"
        cursor = connection.cursor()
        # we pass in our sql to the cursor's execute method, and inside a tuple we then pass in the
        # values for the insert command
        cursor.execute(sql,
                       (customer.first_name, customer.last_name, customer.account_number, customer.account_id))  # BANK
        connection.commit()
        customer_id = cursor.fetchone()[0]
        customer.customer_id = customer_id
        cursor.close()
        return customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        sql = "select * from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer

    def get_all_customers_information(self) -> list[Customer]:
        sql = "select * from customer"
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_records = cursor.fetchall()
        customer_list = []
        for customer in customer_records:
            customer_list.append(Customer(*customer))
            return customer_list

    def update_customer_by_id(self, customer: Customer) -> Customer:
        sql = "update customer set first_name = %s, last_name = %s, account_number = %s, account_id = %s where " \
              "customer_id = %s "  # BANK
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.account_number, customer.account_id,
                             customer.customer_id))  # BANK
        connection.commit()
        return customer

    def delete_customer_by_id(self, customer_id: int) -> bool:
        sql = "delete from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True
