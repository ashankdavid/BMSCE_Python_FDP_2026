class BankAccount:
    def __init__(self, name, balance, pin):  # Constructor
        self.name = name
        self._balance = balance  # Protected
        self.__pin = pin  # Private

    def showBalance(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance is: {self._balance}")
        print(f"PIN: {self.__pin}")

acct = BankAccount("Ashank", 10000, 1234)
print(acct.name)
print(acct._balance)
# print(acct.__pin) # Error
acct.showBalance()

