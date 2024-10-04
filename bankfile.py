class BankAccount():

    def __init__(self, account_id, account_user):
        self.account_id = account_id
        self.account_user = account_user

    def get_user(self):
        return self.account_user

    def set_user(self, new_user):
        self.account_user = new_user

    def get_id(self):
        return self.account_id

    def set_id(self, new_id):
        self.account_id = new_id

    