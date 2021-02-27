from Service import Service


class CreditCard(Service):
    def __init__(self):
        self.paymentAmount = 50

    def makePayment(self):
        return super(CreditCard, self).withdraw() - self.paymentAmount
