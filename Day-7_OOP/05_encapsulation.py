class Bank:
    def __init__(self):
        self.__balance=0
    def deposit(self,a):
        self.__balance+=a
    def show(self):
        print("Balance:",self.__balance)
a=Bank()
b=int(input("Enter Amount: "))
a.deposit(b)
a.show()