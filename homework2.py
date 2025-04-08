'''
Homework2
Name: Jai Outland
github link:
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''


class Bank_Account:  # Standard bank account with deposits, withdrawals and account balance check
    def __init__(self, name, starting_amount):
        self.name = name
        self.account_balance = starting_amount
        self.account = starting_amount

    def account(self):  # Will reflect a positive balance
        return self.account_balance

    def __repr__(self):
        return f"Bank_Account(name='{self.name}', Account Balance={self.account_balance})"

    def __str__(self):
        return f"Account Name: {self.name}\nAccount Balance: {self.account_balance}"

    def deposit(self, amount):  # Adds money to account if account is positive
        if amount > 0:
            self.account_balance += amount
            self.account = self.account_balance
            print(f"{amount} deposited. New balance: {self.account_balance}")
        else:
            print("Please deposit a positive number.")

    def withdraw(self, amount):  # Subtracts money from the account if funds are available
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                self.account = self.account_balance
                print(f"{amount} withdrawn. New balance: {self.account_balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Please withdraw an amount greater than zero.")

    def check_balance(self):  # Will displat current account balance
        print(f"Balance: {self.account_balance}")


# Create with name and account balance information
class SavingsAccount(Bank_Account):
    def __init__(self, name, balance, interest_rate=1.0):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def __repr__(self):
        return f"SavingsAccount(account_holder='{self.name}', balance={self.account_balance}, interest_rate={self.interest_rate}%)"

    def __str__(self):
        return f"Savings Account - {self.name}: Balance = ${self.account_balance:.2f}, Interest Rate = {self.interest_rate}%"

    def apply_interest(self):
        interest = self.account_balance * (self.interest_rate / 100)
        self.account_balance += interest
        return round(self.account_balance, 2)


# Create with name and account balance information
class CheckingAccount(Bank_Account):
    def __init__(self, name, balance, overdraft_limit=100.00):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def __repr__(self):
        return f"CheckingAccount(account_holder='{self.name}', balance={self.account_balance}, overdraft_limit={self.overdraft_limit})"

    def __str__(self):
        return f"Checking Account - {self.name}: Balance = ${self.account_balance:.2f}, Overdraft Limit = ${self.overdraft_limit:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.account_balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.account_balance -= amount
            self.account = self.account_balance
            return self.account_balance    # Returning balance after withdrawal


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))
