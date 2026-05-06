class BankAccount:
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance 


    def deposit(self, amount: float):
        self.balance += amount
        print(f"{self.owner} hisobiga {amount} qo'shildi.")



    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.owner} hisobidan {amount} yechildi.")
        else:
            print(f"{self.owner} hisobida yetarli mablag' yo'q!")

    
    def show_balance(self):
        print(f"{self.owner} balans: {self.balance}")

acc1 = BankAccount("Ali", 100)
acc2 = BankAccount("Vali", 200)
acc3 = BankAccount("Sami", 50)


acc1.show_balance()
acc2.show_balance()
acc3.show_balance()



