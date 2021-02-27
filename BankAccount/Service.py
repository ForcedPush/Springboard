from CreditCard import CreditCard
from Loan import Loan


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
