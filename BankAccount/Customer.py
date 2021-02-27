from Person import Person


class Employee(Person):
    def __init__(self, firstname, lastname, address, salary):
        Person.__init__(self, firstname, lastname, address)
        self.salary = salary

    def giveRaise(self):
        try:
            amount = int(input("How much is the raise?"))
        except ValueError:
            print("Unable to process")
        else:
            self.salary = self.salary + amount
            return self.salary
