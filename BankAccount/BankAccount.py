class BankAccount:
    def __init__(self):
        self.balance = 100

    def withdraw(self):
        try:
            amount = int(input("Amount to withdraw: "))
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
        return self.balance

    def deposit(self):
        try:
            inputString = int(input("Amount to deposit: "))
        except ValueError:
            print("Sorry, that isn't a valid amount")
        else:
            amount = [int(inputString) for s in inputString.split() if s.isdigit()][0]
            self.balance += amount
            return self.balance

    def checkBalance(self):
        inputString = input("check balance?")
        try:
            if not (inputString.lower in ['y', 'yes', 'n', 'no', ]):
                raise ValueError
        except ValueError:
            print("Unable to process response")
        else:
            if inputString.lower in ['y', 'yes']:
                print("Account Balance: ", self.balance)
            print("Thanks!")
