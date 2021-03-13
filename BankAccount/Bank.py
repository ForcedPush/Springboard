from Customer import Customer


class Bank():
    def is_existing_customer(self, first_name, last_name):
        return False

    def add_customer(self, first_name, last_name):
        return Customer(first_name, last_name)

    def save_customer(self):
        pass
