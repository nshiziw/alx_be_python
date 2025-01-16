# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance (default is 0)."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if funds are sufficient."""
        if amount > self.__account_balance:
            return False
        elif amount > 0:
            self.__account_balance -= amount
            return True
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
