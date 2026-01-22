class BankAccount:
    """
    BankAccount represents a simple bank account.

    Abstraction:
    - Users do not need to know how the balance is stored.
    - Interaction is done only through public methods.
    """

    def __init__(self, initial_balance=0):

        self.__balance = initial_balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
    
        return self.__balance

account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)

print("Current Balance:", account.get_balance())
