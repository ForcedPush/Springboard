from Service import Service


class Loan(Service):
    def __init__(self):
        self.loanAmount = 50

    def loan(self):
        return super(Loan, self).deposit() + self.loanAmount
