class FailedTransaction(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class Account:
    open_json = {
        "open": (
            "No Display",
            [
                (
                    "opening_balance",
                    "Please enter a starting balance: ",
                    "non_negative_float",
                )
            ],
        )
    }
    deposit_json = {
        "deposit": (
            "Deposit to account",
            [
                (
                    "deposit_amount",
                    "Please enter amount to deposit: ",
                    "non_negative_float",
                )
            ],
        )
    }

    def __init__(self, customer_id=None):
        self._balance = 0.0
        self._customer_id = customer_id
        self._id = None

    def open(self, opening_balance=100.00):
        self._balance = opening_balance

    def deposit(self, deposit_amount=0.00):
        self._balance += deposit_amount

    def status(self):
        return f'Your account balance is: {"{:.2f}".format(self._balance)}'

    def get_open(self):
        return Account.open_json

    def get_transaction_json(self):
        return Account.deposit_json

    @property
    def id(self):
        return self._id

    @property
    def customer_id(self):
        return self._customer_id


class Savings(Account):
    savings_id = 1

    savings_withdraw_json = {
        "withdraw": (
            "Withdraw from account",
            [
                (
                    "withdrawal_amount",
                    "Please enter amount to withdraw: ",
                    "non_negative_float",
                )
            ],
        )
    }

    def __init__(self, customer_id=None):
        super().__init__(customer_id)
        self._id = str(Savings.savings_id)
        Savings.savings_id += 1

    def withdraw(self, withdrawal_amount=0.00):
        if withdrawal_amount > self._balance:
            raise FailedTransaction(
                f'Withdrawal amount: {"{:.2f}".format(withdrawal_amount)} exceeded balance: {"{:.2f}".format(self._balance)}'
            )
        self._balance -= withdrawal_amount

    def get_transaction_json(self):
        json = super().get_transaction_json().copy()
        json.update(Savings.savings_withdraw_json)
        return json


class Checking(Account):
    checking_id = 1

    checking_open_json = {
        "open": (
            "No Display",
            [
                (
                    "opening_balance",
                    "Please enter a starting balance: ",
                    "non_negative_float",
                ),
            ],
        )
    }

    def __init__(self, customer_id=None):
        super().__init__(customer_id)
        self._id = str(Checking.checking_id)
        Checking.checking_id += 1

    def open(self, opening_balance=100.00):
        super().open(opening_balance)


    def get_open_json(self):
        json = super().get_open_json().copy()
        json.update(Checking.checking_open_json)
        return json
