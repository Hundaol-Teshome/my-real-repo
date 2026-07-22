class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Must be positive")
        self.__balance += amount
        print(f"Deposited {amount} ETB. New balance: {self.__balance} ETB")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        print(f"Withdrew {amount} ETB. New balance: {self.__balance} ETB")

    def statement(self):
        print("\n--- Account Statement ---")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance, "ETB")
        print("-" * 25)

# Create account with input
print("--- Create New Account ---")
name = input("Enter owner name: ")
number = int(input("Enter account number: "))
initial = float(input("Enter starting balance (0 if empty): ") or "0")

acc = Account(name, number, initial)

# Simple menu loop
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Statement")
    print("4. Exit")
    
    choice = input("Choose (1-4): ")
    
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        acc.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        acc.withdraw(amount)
    elif choice == "3":
        acc.statement()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")