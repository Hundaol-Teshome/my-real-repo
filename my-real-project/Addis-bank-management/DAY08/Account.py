class BankConfig:
    """Singleton Pattern"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
            cls._instance.bank_name = "Addis Bank of Ethiopia"
        return cls._instance

# ==========================================================
# Observer Pattern
# ==========================================================

class SMSAlert:

    def update(self, message):
        print(f"[SMS] {message}")


class AuditLog:

    def update(self, message):
        print(f"[AUDIT] {message}")


# ==========================================================
# Base Account Class
# ==========================================================

class Account:

    def __init__(
        self,
        owner,
        number,
        phone,
        email,
        branch,
        account_type,
        balance=0
    ):
        self.owner = owner
        self.account_number = number
        self.phone = phone
        self.email = email
        self.branch = branch
        self.account_type = account_type

        self.bank = BankConfig().bank_name
        self.status = "Active"

        # Protected balance
        self._balance = balance

        # Observer list
        self._observers = []

        # Stack (Day 7)
        self.history = []

    @property
    def balance(self):
        return self._balance

    # =============================
    # Observer Methods
    # =============================

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, message):
        for observer in self._observers:
            observer.update(message)

    # =============================
    # Banking Methods
    # =============================

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self._balance += amount

        # Push to stack
        self.history.append(("deposit", amount))

        self._notify(
            f"{self.owner} deposited {amount} ETB. Balance = {self.balance}"
        )

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self._balance -= amount

        # Push to stack
        self.history.append(("withdraw", amount))

        self._notify(
            f"{self.owner} withdrew {amount} ETB. Balance = {self.balance}"
        )

    # =============================
    # Day 7
    # =============================

    def undo_last(self):

        if not self.history:
            print("No transaction to undo.")
            return

        transaction, amount = self.history.pop()

        if transaction == "deposit":
            self._balance -= amount

        elif transaction == "withdraw":
            self._balance += amount

        print("Transaction undone.")

    # =============================
    # Statement
    # =============================

    # def statement(self):

    #     print("===== ACCOUNT =====")
    #     print(f"Bank: {self.bank}")
    #     print(f"Owner: {self.owner}")
    #     print(f"Account Number: {self.account_number}")
    #     print(f"Phone: {self.phone}")
    #     print(f"Email: {self.email}")
    #     print(f"Branch: {self.branch}")
    #     print(f"Type: {self.account_type}")
    #     print(f"Status: {self.status}")
    #     print(f"Balance: {self.balance:.2f} ETB")
    #     print("-" * 40)
    
    def statement(self):
     print(f"===== {self.account_type.upper()} ACCOUNT =====")
     print(f"Bank: {self.bank}")
     print(f"Owner: {self.owner}")
     print(f"Account Number: {self.account_number}")
     print(f"Phone: {self.phone}")
     print(f"Email: {self.email}")
     print(f"Branch: {self.branch}")
     print(f"Type: {self.account_type}")
     print(f"Status: {self.status}")
     print(f"Balance: {self.balance:.2f} ETB")


# ==========================================================
# Savings Account
# ==========================================================

class SavingsAccount(Account):

    def __init__(
        self,
        owner,
        number,
        phone,
        email,
        branch,
        balance=0
    ):

        super().__init__(
            owner,
            number,
            phone,
            email,
            branch,
            "Savings",
            balance
        )

        self.rate = BankConfig().interest_rate

    def add_interest(self):

        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):

        print("===== SAVINGS ACCOUNT =====")
        super().statement()
        print(f"Interest Rate: {self.rate * 100:.1f}%")
        print("-" * 40)


# ==========================================================
# Current Account
# ==========================================================

class CurrentAccount(Account):

    def __init__(
        self,
        owner,
        number,
        phone,
        email,
        branch,
        balance=0
    ):

        super().__init__(
            owner,
            number,
            phone,
            email,
            branch,
            "Current",
            balance
        )

        self.overdraft = BankConfig().overdraft_limit

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if self.balance - amount < -self.overdraft:
            print("Overdraft limit exceeded.")
            return

        self._balance -= amount

        self.history.append(("withdraw", amount))

        self._notify(
            f"{self.owner} withdrew {amount} ETB. Balance = {self.balance}"
        )

    def statement(self):

      print("===== CURRENT ACCOUNT =====")
      super().statement()
      print(f"Overdraft Limit: {self.overdraft:.2f} ETB")
      print("-" * 40)



# ==========================================================
# Factory Pattern
# ==========================================================

class AccountFactory:

    @staticmethod
    def create(
        kind,
        owner,
        number,
        phone,
        email,
        branch,
        balance=0
    ):

        kind = kind.lower()

        if kind == "savings":

            return SavingsAccount(
                owner,
                number,
                phone,
                email,
                branch,
                balance
            )

        elif kind == "current":

            return CurrentAccount(
                owner,
                number,
                phone,
                email,
                branch,
                balance
            )

        raise ValueError("Unknown account type.")