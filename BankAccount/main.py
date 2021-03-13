from Bank import Bank


def initial_screen():
    print("[1] Open a new account" )
    print("[2] Access an existing account")
    print("[3] Exit")

    s = ""
    while s != "3":
        try:
            s = input("Enter selection: ")
            if s not in ["1", "2", "3"]:
                raise ValueError
        except ValueError:
            print("Invalid choice")
        if s == "1":
            first_name = input("\n First Name:")
            last_name = input("\n Last Name:")
            if bank.is_existing_customer(first_name, last_name):
                print("This customer already exists")
                return initial_screen
            else:
                customer = bank.create_customer(first_name, last_name)
                customer.street_address = input("Address:")
                customer.city = input("City:")
                customer.state = input("State:")
                customer.zip = input("Zip Code:")
                bank.save_customer()
                print("Welcome")
                return initial_screen
        elif s == "2":
            print("Account")
            return initial_screen
        elif s == "3":
            return initial_screen

            return new_account_screen
        elif s == "2":
            return existing_account_screen
        elif s == "3":
            return None


def new_account_screen():
    print("New Account Screen")
    return initial_screen

def existing_account_screen():
    print("Existing Account Screen")
    return initial_screen

if __name__ == '__main__':
    bank = Bank()
    next = initial_screen

    # process screens until done
    while next:
        print('\033c', end='')  # clean screen
        next = next()
    print("\nExiting")
