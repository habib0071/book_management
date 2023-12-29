from allUser import User, Admin
from information import Information

class Bank:
    def __init__(self):
        self.information = Information()

    def create_user(self, name, email, initial_balance):
        user = User(name, email, initial_balance, self.information)
        self.information.add_user(user)
        return user

    def create_admin(self, name, email):
        admin = Admin(name, email, self.information)
        return admin
