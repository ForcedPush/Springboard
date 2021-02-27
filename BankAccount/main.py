from BankAccount import BankAccount
from Person import Person
from Service import Service


def run():
    try:
        selection = int(input("1. BankAccount \n"
                              "2. Person"
                              "3. Service"))
        if selection not in [1, 2, 3]:
            raise ValueError
    except ValueError:
        print("Invalid selection")
    else:
        if selection == 1:
            account = BankAccount()
            account.run()
        elif selection == 2:
            person = Person()
            person.run()
        elif selection == 3:
            service = Service()
            service.run()

