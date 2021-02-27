from BankAccount import BankAccount


class Checking(BankAccount):
    def withdraw(self):
        try:
            inputString = input("Is this bank in your network? ")
            if inputString.lower not in ['y', 'yes', 'n', 'no']:
                raise Exception
        except Exception:
            print("answer not recognized")
            return
        else:
            if inputString.lower in ['n', 'no']:
                return super(Checking, self).withdraw() + 1
            else:
                return super(Checking, self).withdraw()
