# from Customer import Customer
# from Employee import Employee
import json


class Person():
    def __init__(self, firstname=None, lastname=None, address=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.json = {"firstname": self.firstname,
                     "lastname": self.lastname,
                     "address": self.address}

    def run(self):
        try:
            firstname = str(input("What is your first name? "))
            lastname = str(input("What is your last name? "))
            address = str(input("What is your address?"))
            personType = int(input("1. Customer \n"
                                   "2. Employee"))

            if len(firstname) == 0 or len(lastname) == 0 or len(address) == 0:
                raise ValueError
            if personType not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Invalid input")
        else:
            if personType == 1:
                customer = Customer()
                customer.run()
            elif personType == 2:
                employee = Employee(firstname=firstname, lastname=lastname, address=address)
                employee.run()

            self.json["firstname"] = firstname
            self.json["lastname"] = lastname
            self.json["address"] = address

            print("Thank you")


class Customer(Person):
    def __init__(self, firstname, lastname, address):
        Person.__init__(self, firstname, lastname, address)
        self.netWorth = 1000
        self.json = {"networth": self.netWorth}

    def run(self):
        try:
            nw = int(input("What is your net worth?"))
            if type(nw) != int:
                raise ValueError
        except ValueError:
            print("Invalid input")
        else:
            self.json["networth"] = nw
            print("Thank you")


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
