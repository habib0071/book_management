class Information:
    def __init__(self):
        self.users = []
        self.transactions = []
        self.loan_feature_enabled = True

    def add_user(self, user):
        self.users.append(user)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_users(self):
        return self.users

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled

