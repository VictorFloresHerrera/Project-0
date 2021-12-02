"""This is where my API will go: I will create a
 flask object here and define my routes and their functions"""
from flask import Flask, request, jsonify

from System.custom_exceptions.duplicate_account_name_exception import DuplicateAccountNameException
from System.custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException
from System.data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
# from System.data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from System.entities.accounts import Account
from System.entities.customers import Customer
from System.service_layer.implementation_services.account_service_imp import AccountServiceImp
from System.service_layer.implementation_services.customer_postgres_dao import CustomerPostgresDAO
from System.service_layer.implementation_services.customer_postgres_service import CustomerPostgresService

# from System.service_layer.implementation_services.customer_service_imp import CustomerServiceImp

app: Flask = Flask(__name__)

customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresService(customer_dao)

account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)


# create customer method?
@app.post("/customer")
def create_customer_entry():
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["accountNumber"],
            customer_data["customerId"],
            customer_data["accountId"]  # BANK
        )
        customer_to_return = customer_service.service_create_customer_entry(new_customer)
        customer_as_dictionary = customer_to_return.make_customer_dictionary()
        customer_as_json = jsonify(customer_as_dictionary)
        return customer_as_json
    except DuplicateAccountNumberException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


# View my personal information
@app.get("/customer/<customer_id>")
def get_customer_by_id(customer_id: str):
    result = customer_service.service_get_customer_by_id(int(customer_id))
    result_as_dictionary = result.make_customer_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json
    pass


# get all customers information
@app.get("/customer")
def get_all_customers_information():
    customers_as_customers = customer_service.service_get_all_customers_information()
    customers_as_dictionary = []
    for customers in customers_as_customers:
        dictionary_customer = customers.make_customer_dictionary()
        customers_as_dictionary.append(dictionary_customer)
    return jsonify(customers_as_dictionary)


# Update personal information # need to reimplement the service logic for this route
@app.patch("/customer/<customer_id>")
def update_customer_by_id(customer_id: str):
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["accountNumber"],
            int(customer_id),
            customer_data["accountId"]  # BANK
        )
        updated_customer = customer_service.service_update_customer_by_id(new_customer)
        return "Customer updated successfully, the customer info is now" + str(updated_customer)
    except DuplicateAccountNumberException as e:
        return str(e)


# End business relationship with the place
@app.delete("/customer/<customer_id>")
def delete_customer_by_id(customer_id: str):
    result = customer_service.service_delete_customer_by_id(int(customer_id))
    if result:
        return "Customer with id {} was deleted successfully".format(customer_id)
    else:
        # this will run if the customer we try to delete is not in the database. Ideally we would
        # instead use a try except block, but this works for now
        return "Something went wrong: Customer with id {} was not deleted".format(customer_id)


@app.post("/account")
def create_account():
    try:
        body = request.get_json()
        new_account = Account(
            body["accountId"],
            body["name"]
        )
        created_account = account_service.service_create_account(new_account)
        created_account_as_dictionary = created_account.create_account_dictionary(), 201
        return jsonify(created_account_as_dictionary)
    except DuplicateAccountNameException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@app.get("/account/<account_id>")
def get_account_by_id(account_id: str):
    account = account_service.service_get_account_by_id(int(account_id))
    account_as_dictionary = account.create_account_dictionary()
    return jsonify(account_as_dictionary), 200


@app.get("/account")
def get_all_accounts():
    accounts = account_service.service_get_all_account()
    accounts_as_dictionaries = []
    for account in accounts:
        dictionary_account = account.create_account_dictionary()
        accounts_as_dictionaries.append(dictionary_account)
    return jsonify(accounts_as_dictionaries), 200


@app.patch("/account/<customer_id>")
def update_account(customer_id: str):
    try:
        body = request.get_json()
        update_info = Account(
            body["accountId"],
            body["name"]
        )
        updated_customer = account_service.service_update_account_by_id(update_info)
        updated_customer_as_dictionary = updated_customer.create_account_dictionary()
        return jsonify(updated_customer_as_dictionary), 200
    except DuplicateAccountNameException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)


@app.delete("/account/<account_id>")
def delete_account(account_id: str):
    result = account_service.service_delete_account_by_id(int(account_id))
    if result:
        return "Account with id {} was deleted successfully".format(account_id)
    else:
        return "Something went wrong: Account with id {} was not deleted".format(account_id)


app.run()
