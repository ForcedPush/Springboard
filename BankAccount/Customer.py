from Person import Person


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
            self.json["networtth"] = nw
            print("Thank you")
