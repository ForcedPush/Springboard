from Savings import Savings
from Checking import Checking

class Person:
    def __init__(self, firstname, lastname, address, networth):
        self.fisrtname = firstname
        self.lastname = lastname
        self.address = address
        self.networth = networth

    def openAccount(self):
        inputString = input("Do you want to open a checking or savings account?")
        if inputString.lower not in ["c", "1", "checking", "s", "2", "savings"]):
            print("unable to process input")
        else:
            account = [inputString for s in inputString.split() if s.isstring()][0]
            isChecking = True if account.lower in ["c", "1", "checking"] else False
            if isChecking:
                account = Checking()
            else:
                account = Savings()
