from BankAccount import BankAccount


class Savings(BankAccount):
    def deposit(self):
        return super(Savings, self).deposit() * 0.15
