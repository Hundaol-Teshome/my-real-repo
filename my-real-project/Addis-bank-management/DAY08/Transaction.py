from Account import Account, AccountFactory
from registry import AccountRegistry

registry = AccountRegistry()

acc1 = AccountFactory.create(
    "savings",
    "Binyam",
    "CBE1001",
    "0911223344",
    "binyam@email.com",
    "Addis Ababa",
    5000
)

acc2 = AccountFactory.create(
    "current",
    "Almaz",
    "CBE1002",
    "0922334455",
    "almaz@email.com",
    "Bole",
    3000
)

acc3 = AccountFactory.create(
    "savings",
    "Sara",
    "CBE1003",
    "0933445566",
    "sara@email.com",
    "Adama",
    7000
)

registry.add(acc1)
registry.add(acc2)
registry.add(acc3)

acc1.deposit(500)
acc1.withdraw(200)
acc1.deposit(300)

print("===== Leaderboard =====")

for account in registry.top_by_balance(2):
    print(account.owner, account.balance)

print()

print("===== Binary Search =====")

account = registry.find_by_number("CBE1002")

if account:
    account.statement()

print(account.owner, account.balance)

print("===== Recursive Total =====")

print(
    registry.total_transactions(acc1)
)