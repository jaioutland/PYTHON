'''
Homework1
Name: Jai Outland
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


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))
