from Account import AccountFactory, AuditLog, BankConfig, SMSAlert

# Singleton
config1 = BankConfig()
config2 = BankConfig()

print(config1 is config2)      # True

# Observers
sms = SMSAlert()
audit = AuditLog()

# Factory
acc1 = AccountFactory.create(
    "savings",
    "Binyam",
    "CBE1001",
    5000
)

acc2 = AccountFactory.create(
    "current",
    "CBE1002",
    "CBE1002",
    2000
)

# Subscribe observers
acc1.subscribe(sms)
acc1.subscribe(audit)

acc2.subscribe(sms)
acc2.subscribe(audit)

# Transactions
acc1.deposit(1000)
acc1.add_interest()

acc2.withdraw(1500)

accounts = [acc1, acc2]

print("\n--- Account Statements ---\n")

for account in accounts:
    account.statement()