from Account import Checking, Savings, FailedTransaction
from Customer import Customer


def select_from_menu(prompt, options):
    """
    Interact with the terminal user via a formatted menu.
    return selected option
    """
    print("\033c", end="")  # clear screen
    print(prompt)
    for i, option in enumerate(options):
        print("[" + str(i + 1) + "] " + option[0])

    while True:

        print("\n Select an option: ", end="")
        s = input().strip()
        if s.isnumeric() and int(s) in range(1, len(options) + 1):
            return options[int(s) - 1][1]


def get_parameter_of_type(text, parm_type):
    while True:
        s = input(text).strip()
        if parm_type == "non_negative_float":
            try:
                typed_value = round(float(s), 2)
                if typed_value < 0:
                    print(
                        "Enter a valid amount"
                    )
                    continue
            except ValueError:
                print(
                    "Enter a valid amount"
                )
                continue
        elif parm_type == "non_negative_int":
            try:
                typed_value = int(s)
                if typed_value < 0:
                    print("Enter a valid amount")
                    continue
            except ValueError:
                print("Enter a valid amount")
                continue
        else:
            typed_value = s

        return typed_value


def get_kwargs(metadata_parameters):
    return {
        parm: get_parameter_of_type(text, parm_type)
        for parm, text, parm_type in metadata_parameters
    }


def is_existing_customer():
    prompt = "Are you already a customer?"
    options = (("Yes", Bank.YES), ("No", Bank.NO))

    return select_from_menu(prompt, options)


class Bank:
    OPEN_NEW_ACCOUNT = "OPEN_NEW_ACCOUNT"
    RUN_TRANSACTION = "RUN_TRANSACTION"
    EXIT = "EXIT"
    YES = "YES"
    NO = "NO"

    customers = {}
    accounts = {}

    class InvalidCredentials(Exception):
        pass

    class ExistingCustomer(Exception):
        pass

    class InvalidInput(Exception):
        pass

    def main_activity(self):
        prompt = "Select an option"
        options = (
            ("Open an account", Bank.OPEN_NEW_ACCOUNT),
            ("View account", Bank.RUN_TRANSACTION),
            ("Exit", Bank.EXIT),
        )

        return select_from_menu(prompt, options)

    def new_account_type(self):
        prompt = "Which type of account do you want to open?"
        options = (
            ("Checking", Checking),
            ("Savings", Savings),
        )

        return select_from_menu(prompt, options)

    def transactions(self, transaction_metadata):
        prompt = "Transactions:"
        options = [
            (transaction_metadata[meta][0], meta) for meta in transaction_metadata
        ]  # (display_name, method)

        return select_from_menu(prompt, options)

    def make_new_customer(self):
        customer = Customer()
        info = customer.info()
        info_metadata_parameters = info["set_info"][1]
        kwargs = get_kwargs(info_metadata_parameters)
        customer.set_info(**kwargs)

        if customer in self.customers.values():
            raise self.ExistingCustomer
        else:
            self.customers[customer.id] = customer
            print(
                "\n Customer ID is: {n}.".format(
                    n=customer.id
                )
            )
            input("\n Please hit return to open your new account")
            return customer

    def make_valid_customer(self):
        option = is_existing_customer()
        if option == Bank.YES:
            customer_id = input("Bank id: ").strip()
            pin = input("PIN: ").strip()
            customer = self.customers.get(customer_id)
            if not customer or customer.pin != pin:
                raise self.InvalidCredentials
            return customer
        elif option == Bank.NO:
            print("\n Open an account")
            return self.make_new_customer()
        else:
            raise self.InvalidInput(
                "Invalid input"
            )

    def get_new_account(self):

        customer = self.make_valid_customer()
        account_type = self.new_account_type()
        account = account_type(customer_id=customer.id)

        open_metadata = account.get_open_metadata()
        open_metadata_parameters = open_metadata["open"][1]
        kwargs = get_kwargs(open_metadata_parameters)
        account.open(**kwargs)

        self.accounts[account.id] = account
        customer.add_account(account.id)

        input(
            "Hit return to continue".format(account.id)
        )

    def get_validated_account(self):
        account_id = input("\nPlease enter your account id ").strip()
        pin = input("\nPlease enter your PIN ").strip()

        account = Bank.accounts.get(account_id)
        if account:
            customer = self.customers[account.customer_id]
            if pin == customer.pin:
                return account

        raise self.InvalidCredentials

    def run_transaction(self):

        account = self.get_validated_account()
        customer = self.customers[account.customer_id]

        print("\033c", end="")  # clear screen
        print(f"Hi, {customer.first_name}.")
        another_transaction = Bank.YES

        while another_transaction == Bank.YES:

            transaction_metadata = account.get_transaction_metadata()
            transaction_method = self.transactions(
                transaction_metadata
            )
            transaction_parameters = transaction_metadata[transaction_method][1]
            kwargs = get_kwargs(transaction_parameters)

            try:
                getattr(account, transaction_method)(**kwargs)  # call method
                print("\n Transaction succeeded")
                print(account.status())
            except FailedTransaction as ex:
                print("\n Transaction failed.")
                print(ex)

            input("\n Please hit return to continue")
            prompt = f" Would you like to perform another transaction on this account, {customer.first_name}?"
            options = (("Yes", Bank.YES), ("No", Bank.NO))

            another_transaction = select_from_menu("", prompt, options)

    def run(self):
        while True:
            try:
                activity = self.main_activity()
                if activity == Bank.RUN_TRANSACTION:
                    self.run_transaction()
                elif activity == Bank.OPEN_NEW_ACCOUNT:
                    self.get_new_account()
                elif activity == Bank.EXIT:
                    print("\n Bye")
                    break
                else:
                    raise Bank.InvalidInput("Invalid input")

            except Bank.InvalidCredentials:
                input(
                    "Invalid credentials"
                )
            except Bank.ExistingCustomer:
                input(
                    "Customer already exists"
                )
            except Exception as ex:
                print(ex)
                input("Unexpected error")


def __main__():
    Bank().run()


if __name__ == "__main__":
    Bank().run()
