from BankAccount import BankAccount


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
