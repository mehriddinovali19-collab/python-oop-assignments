class BankAccount:

    def __init__(self, Owner: str, Balance: float ):
        self.owner = Owner
        self.balance = Balance

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Yangi balans: {self.balance}")
    

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Yangi balans: {self.balance}")
        else:
            print("Xatolik: Mablag' yetarli emas!")

account1 = BankAccount("Ali", 1000)

account1.withdraw(800)