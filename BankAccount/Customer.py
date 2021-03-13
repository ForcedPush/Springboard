class CustomerAlreadyExistsException(Exception):
    pass


class Customer:
    next_customer_id = 1

    def __init__(self):

        self._id = str(Customer.next_customer_id)
        self._accounts = []

        self._first_name = ""
        self._last_name = ""
        self._street_address = ""
        self._state = ""
        self._zip_code = ""
        self._pin = ""

        Customer.next_customer_id += 1

    def info(self):

        return {
            "set_info": (
                "No Display",
                [
                    ("first_name", "Enter your first name: ", "string"),
                    ("last_name", "Enter your last name: ", "string"),
                    (
                        "pin",
                        "Enter your PIN: ",
                        "string",
                    ),
                ],
            )
        }

    def set_info(self, **kwargs):

        self._first_name = kwargs.get("first_name")
        self._last_name = kwargs.get("last_name")
        self._pin = kwargs.get("pin")

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def pin(self):
        return self._pin

    def add_account(self, account_id):
        self._accounts.append(account_id)

    def __eq__(self, other):
        if isinstance(other, Customer):
            if (
                (self.first_name == other.first_name)
                and (self.last_name == other.last_name)
            ):
                return True
        return False
