class Customer:

    def __init__(self, first_name: str, last_name: str, account_number: int, customer_id: int, account_id: int):  # BANK
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.customer_id = customer_id
        self.account_id = account_id  # BANK

    def make_customer_dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "accountNumber": self.account_number,
            "customerId": self.customer_id,
            "accountId": self.account_id  # BANK

        }
