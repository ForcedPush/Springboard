# from CreditCard import CreditCard
# from Loan import Loan


class Service:
    def __init__(self):
        self.services = ["Loan", "Credit Card"]

    def run(self):
        try:
            selection = int(input("1. Loan \n"
                                  "2. Credit Card"))
            if selection not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Invalid selection")
        else:
            if selection == 1:
                loan = Loan()
                loan.run()
            elif selection == 2:
                cc = CreditCard()
                cc.run()


class Loan(Service):
    def __init__(self):
        self.loanAmount = 50
        self.json = {"loan": self.loanAmount}

    def run(self):
        try:
            amount = int(input("How much do you want to borrow?"))
            if type(amount) != int:
                raise TypeError
        except TypeError:
            print("Invalid input")
        else:
            self.loanAmount += amount
            self.json["loan"] = self.loanAmount


class CreditCard(Service):
    def __init__(self):
        self.chargeAmount = 50
        self.json = {"creditCardBalance": self.chargeAmount}

    def run(self):
        try:
            amount = int(input("How much do you want to charge?"))
            if type(amount) != int:
                raise TypeError
        except TypeError:
            print("Invalid input")
        else:
            self.chargeAmount += amount
            self.json["creditCardBalance"] = self.chargeamount
            print("Thank you")
