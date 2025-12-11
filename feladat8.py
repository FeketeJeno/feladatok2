#8. feladat – OOP: BankAccount osztály
#Készíts egy BankAccount osztályt:
#attribútumok: név, egyenleg
#metódusok: deposit(), withdraw(), get_balance()
#Hozz létre két bankszámla objektumot, és teszteld.

class BankAccount:
    def __init__(self, nev, egyenleg=0):
        self.name = nev
        self.balance = egyenleg

    def deposit(self,amount):
        self.balance += amount
    

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-= amount
        else:
            print("Nincs elég fedezet.")
    
    def get_balance(self):
        return self.balance
    

account1 = BankAccount("Kiss Miska")
account2 = BankAccount("Nagy Tivadar")

account1.deposit(7500)
account1.withdraw(2300)
account1.get_balance()

print(account1.get_balance())
