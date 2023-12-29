class Person:
    def __init__(self, name, email, information) -> None:
        self.name = name
        self.email = email
        self.information = information

class User(Person):
    def __init__(self, name, email, initial_balance, information) -> None:
        super().__init__(name, email, information)
        self.balance = initial_balance
        self.loan = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.information.add_transaction(f"{self.name} deposited ${amount}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.information.add_transaction(f"{self.name} withdrew ${amount}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer(self, recipient, amount):
        if 0 < amount <= self.balance:
            recipient.deposit(amount)
            self.balance -= amount
            self.information.add_transaction(f"{self.name} transferred ${amount} to {recipient.name}.")
        else:
            print("Invalid transfer amount or insufficient funds.")

    def check_balance(self):
        print(f"{self.name}'s balance: ${self.balance}")

    def take_loan(self):
        if self.loan == 0:
            loan_amount = 2 * self.balance
            self.loan += loan_amount
            self.balance += loan_amount
            self.information.add_transaction(f"{self.name} took a loan of ${loan_amount}.")
        else:
            print(f"{self.name} has already taken a loan.")

    def check_loan(self):
        print(f"{self.name}'s loan amount: ${self.loan}")

class Admin(Person):
    def __init__(self, name, email, information) -> None:
        super().__init__(name, email, information)

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.information.get_users())
        print(f"Total bank balance: ${total_balance}")

    def check_total_loan(self):
        total_loan = sum(user.loan for user in self.information.get_users())
        print(f"Total bank loan amount: ${total_loan}")

    def toggle_loan_feature(self):
        self.information.toggle_loan_feature()
        print("Loan feature is now", "ON" if self.information.loan_feature_enabled else "OFF")
