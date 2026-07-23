class BankConfig:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance
# Observer Classes
class SMSAlert:
    def update(self, message):
        print(f"[SMS] {message}")

class AuditLog:

    def update(self, message):
        print(f"[AUDIT] {message}")

# Base Account

class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self._balance = balance
        self._observers = []

    @property
    def balance(self):
        return self._balance

    # Observer Pattern
    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, message):
        for observer in self._observers:
            observer.update(message)

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit.")
            return

        self._balance += amount
        self._notify(
            f"{self.owner} deposited {amount} ETB. Balance = {self.balance}"
        )

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal.")
            return

        if amount > self.balance:
            print("Insufficient funds.")
            return

        self._balance -= amount

        self._notify(
            f"{self.owner} withdrew {amount} ETB. Balance = {self.balance}"
        )

    def statement(self):
        print(f"Account : {self.owner}")
        print(f"Balance : {self.balance}")

# Factory Pattern

class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind.lower() == "savings":
            return SavingsAccount(owner, number, balance)

        elif kind.lower() == "current":
            return CurrentAccount(owner, number, balance)

        raise ValueError("Unknown account type")
    
# Savings Account

class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.rate = BankConfig().interest_rate

    def add_interest(self):
        self.deposit(self.balance * self.rate)

    def statement(self):
        print("=== Savings Account ===")
        super().statement()

# Current Account

class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.overdraft = BankConfig().overdraft_limit

    def withdraw(self, amount):

        if self.balance - amount < -self.overdraft:
            print("Overdraft exceeded.")
            return

        self._balance -= amount

        self._notify(
            f"{self.owner} withdrew {amount} ETB. Balance = {self.balance}"
        )

    def statement(self):
        print("=== Current Account ===")
        super().statement()