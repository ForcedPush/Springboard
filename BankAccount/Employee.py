from Person import Person
import json


class Employee(Person):
    def __init__(self, firstname, lastname, address):
        Person.__init__(self, firstname, lastname, address)
        self.salary = 100
        self.json = {"salary": self.salary}

    def run(self):
        try:
            amount = int(input("How much is the raise for this employee?"))
            if type(amount) != int:
                raise ValueError
        except ValueError:
            print("Unable to process")
        else:
            self.salary = self.salary + amount
            self.json["salary"] = self.salary
            return self.salary
