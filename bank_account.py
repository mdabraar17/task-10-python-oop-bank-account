# bank_account.py
# Demonstration of OOP concepts using a Bank Account example

# -------- Base Class --------
class BankAccount:
    def __init__(self, name, balance=0):
        """
        Constructor to initialize account holder name and balance
        """
        self.name = name            # public attribute
        self.__balance = balance   # private attribute (encapsulation)

    def deposit(self, amount):
        """Add money to account"""
        self.__balance += amount
        print(f"{amount} deposited. New balance: {self.__balance}")

    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. Balance left: {self.__balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        """Access private balance safely"""
        return self.__balance


# -------- Child Class (Inheritance) --------
class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def withdraw(self, amount):
        """
        Overriding withdraw method
        Savings account must keep minimum balance of 500
        """
        if self.get_balance() - amount < 500:
            print("Cannot withdraw. Minimum balance of 500 required.")
        else:
            super().withdraw(amount)


# -------- Creating Objects --------
account1 = BankAccount("Aman", 1000)
account2 = SavingsAccount("Neha", 2000)

# -------- Simulating Bank Operations --------
print("\n--- BankAccount Operations ---")
account1.deposit(500)
account1.withdraw(300)
print("Balance:", account1.get_balance())

print("\n--- SavingsAccount Operations ---")
account2.withdraw(1200)
account2.withdraw(300)
print("Balance:", account2.get_balance())
