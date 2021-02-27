# from Service import Service
#
#
# class Loan(Service):
#     def __init__(self):
#         self.loanAmount = 50
#         self.json = {"loan": self.loanAmount}
#
#     def run(self):
#         try:
#             amount = int(input("How much do you want to borrow?"))
#             if type(amount) != int:
#                 raise TypeError
#         except TypeError:
#             print("Invalid input")
#         else:
#             self.loanAmount += amount
#             self.json["loan"] = self.loanAmount
