class Account:
    def __init__(self, account_id: int, name: str):
        self.account_id = account_id
        self.name = name

    def __str__(self):
        return "Id: {}, name: {}".format(self.account_id, self.name)

    def create_account_dictionary(self):
        return {
            "accountId": self.account_id,
            "name": self.name
        }
