class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show_balance(self):
        print("Current Balance:", self.__balance)


account = BankAccount()

# User input
deposit_amount = int(input("Enter deposit amount: "))
account.deposit(deposit_amount)

withdraw_amount = int(input("Enter withdrawal amount: "))
account.withdraw(withdraw_amount)

account.show_balance()