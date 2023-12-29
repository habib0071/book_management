from Bank import Bank

def main():
    bank = Bank()

    user1 = bank.create_user("User1", "user1@gmail.com", 500)
    user2 = bank.create_user("User2", "user2@gmail.com", 1000)

    user1.deposit(200)
    user1.withdraw(50)
    user1.transfer(user2, 30)

    user1.check_balance()
    user2.check_balance()

    user1.take_loan()
    user2.take_loan()

    user1.check_loan()
    user2.check_loan()

    admin = bank.create_admin("Admin", "admin@gmail.com")

    admin.check_total_balance()
    admin.check_total_loan()
    admin.toggle_loan_feature()

if __name__ == "__main__":
    main()
