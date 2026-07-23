from Account import Account


class AccountRegistry:

    def __init__(self):
        self.by_number = {}
        self.order = []

    def add(self, account):

        self.by_number[account.account_number] = account
        self.order.append(account.account_number)

    def find(self, number):

        return self.by_number.get(number)

    def list_all(self):

        accounts = []

        for number in self.order:
            accounts.append(
                self.by_number[number]
            )

        return accounts
    
    def top_by_balance(self, n):

        accounts = self.list_all()

        return sorted(
            accounts,
            key=lambda account: account.balance,
            reverse=True
        )[:n]

    def binary_search(self, sorted_accounts, number):

        low = 0
        high = len(sorted_accounts) - 1

        while low <= high:

            mid = (low + high) // 2

            if sorted_accounts[mid].account_number == number:
                return sorted_accounts[mid]

            elif sorted_accounts[mid].account_number < number:
                low = mid + 1

            else:
                high = mid - 1

        return None
     
    def find_by_number(self, number):

     accounts = sorted(
        self.list_all(),
        key=lambda account: account.account_number
    )

     return self.binary_search(accounts, number)
 
    def total_transactions(self, account):

     def helper(history):

        if not history:
            return 0

        transaction, amount = history[0]

        return amount + helper(history[1:])

     return helper(account.history)