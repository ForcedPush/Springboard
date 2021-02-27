from BankAccount import BankAccount


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
                return super(Checking, self).processWithdraw() + 1 # out of network fee

    def deposit(self):
        return super(Checking, self).processDeposit()
