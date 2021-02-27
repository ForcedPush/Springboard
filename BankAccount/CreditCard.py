# from Service import Service
#
#
# class CreditCard(Service):
#     def __init__(self):
#         self.chargeAmount = 50
#         self.json = {"creditCardBalance": self.chargeAmount}
#
#     def run(self):
#         try:
#             amount = int(input("How much do you want to charge?"))
#             if type(amount) != int:
#                 raise TypeError
#         except TypeError:
#             print("Invalid input")
#         else:
#             self.chargeAmount += amount
#             self.json["creditCardBalance"] = self.chargeamount
#             print("Thank you")
