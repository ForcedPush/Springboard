# from Checking import Checking
# from Savings import Savings
import json


class BankAccount:
    def __init__(self):
        self.balance = 100
        self.json = {"Balance": self.balance}

    def run(self):
        try:
            accountSelection = int(input("1. Withdraw \n"
                                         "2. Deposit \n"
                                         "3. Check Balance"))
            if accountSelection not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Invalid choice")
        else:
            if accountSelection == 1:
                self.withdraw()
            elif accountSelection == 2:
                self.deposit()
            elif accountSelection == 3:
                self.checkBalance()

    def withdraw(self):
        try:
            selection = int(input("1. Withdraw from checking \n"
                                  "2. Withdraw from savings \n"))
            if selection not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Invalid choice")
        else:
            if selection == 1:
                checking = Checking()
                checking.withdraw()
            elif selection == 2:
                savings = Savings()
                savings.withdraw()

    def processWithdraw(self):
        try:
            amount = int(input("Withdraw amount: "))
            if type(amount) != int:
                raise TypeError
            if amount > self.balance:
                raise ValueError
        except TypeError:
            print("Sorry, that isn't valid")
        except ValueError:
            print("Insufficient funds")
        else:
            print(amount)
            self.balance = self.balance - amount
            self.json["Balance"] = self.balance
        return self.balance

    def deposit(self):
        try:
            selection = int(input("1. Deposit to checking \n"
                                  "2. Deposit to savings \n"))
            if selection not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Invalid choice")
        else:
            if selection == 1:
                checking = Checking()
                checking.deposit()
            elif selection == 2:
                savings = Savings()
                savings.deposit()

    def processDeposit(self):
        try:
            amount = int(input("Amount to deposit: "))
        except ValueError:
            print("Sorry, that isn't a valid amount")
        else:
            self.balance += amount
            self.json["Balance"] = self.balance
            return self.balance

    def checkBalance(self):
        inputString = input("check balance?")
        try:
            if inputString.lower not in ['y', 'yes', 'n', 'no', ]:
                raise ValueError
        except ValueError:
            print("Unable to process response")
        else:
            if inputString.lower in ['y', 'yes']:
                print("Account Balance: ", self.balance)
            print("Thanks!")


class Checking(BankAccount):
    def withdraw(self):
        try:
            selection = int(input("1. Bank is in network \n"
                                  "2. Bank is out of network"))
            if selection not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Invalid selection")
        else:
            if selection == 1:
                return super(Checking, self).processWithdraw()
            else:
                return super(Checking, self).processWithdraw() + 1  # out of network fee

    def deposit(self):
        return super(Checking, self).processDeposit()


class Savings(BankAccount):
    def __init__(self):

        self.withdrawCap = 3
        self.withdrawCount = 0
        super().__init__()

    def withdraw(self):
        try:
            if self.withdrawCount > self.withdrawCap:
                raise ValueError
        except ValueError:
            print("Too many withdraws")
        else:
            self.withdrawCount += 1
            return super(Savings, self).processWithdraw()

    def deposit(self):
        return super(Savings, self).deposit() * 0.15
