# Encapsulation..
# hiding internal data and controlling access.
# _protected → Convention (can still access)
# __private → Name mangling (harder to access from outside)

class BankAccount:
    def __init__(self, owner, balanse):
        self._owner = owner
        self._balance = balanse     # protected
        self.__pin = 1234       # private

    def deposite(self, amount):
        self._balance += amount
        print("Dposited: ", amount)

    def get_balance(self):
        return self._balance

    def show_pin(self):
        print("PIN: ", self.__pin)

acc = BankAccount("Rahul", 5000)
print(acc._owner)
print(acc._balance) # possible but not  recommended
# print(acc.__pin)  # error
acc.show_pin()
print(acc.get_balance())