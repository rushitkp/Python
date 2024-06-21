#Write a program in python to implement Bank System using Class and Methods and perform belowOperations. (Note: Use of object oriented paradigm is compulsory.)
#a) Add Bank account
#b) Deposit of money
#c) withdrawal operation
#d) Money transfer
#e) Show Balance


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_no, initial_balance):
        if account_no not in self.accounts:
            self.accounts[account_no] = initial_balance
            print(f"Account {account_no} added successfully with initial balance: {initial_balance}")
        else:
            print(f"Account {account_no} already exists.")

    def deposit(self, account_no, amount):
        if account_no in self.accounts:
            self.accounts[account_no] += amount
            print(f"Amount {amount} deposited successfully to account {account_no}.")
        else:
            print(f"Account {account_no} does not exist.")

    def withdraw(self, account_no, amount):
        if account_no in self.accounts:
            if self.accounts[account_no] >= amount:
                self.accounts[account_no] -= amount
                print(f"Amount {amount} withdrawn successfully from account {account_no}.")
            else:
                print(f"Insufficient balance in account {account_no}.")
        else:
            print(f"Account {account_no} does not exist.")

    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account] >= amount:
                self.accounts[from_account] -= amount
                self.accounts[to_account] += amount
                print(f"Amount {amount} transferred successfully from account {from_account} to account {to_account}.")
            else:
                print(f"Insufficient balance in account {from_account}.")
        else:
            print(f"One or both of the accounts do not exist.")

    def show_balance(self, account_no):
        if account_no in self.accounts:
            print(f"Account Number: {account_no}, Balance: {self.accounts[account_no]}")
        else:
            print(f"Account {account_no} does not exist.")

# Create an instance of BankSystem
bank = BankSystem()

# Add bank accounts
bank.add_account('123', 1000)
bank.add_account('456', 2000)

# Deposit money
bank.deposit('123', 500)

# Withdraw money
bank.withdraw('123', 200)

# Transfer money
bank.transfer('123', '456', 300)

# Show balance
bank.show_balance('123')
bank.show_balance('456')
