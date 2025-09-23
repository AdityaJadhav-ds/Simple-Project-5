class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance 

    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance: {self.__balance}"
        else:
            return "Insufficient funds or invalid amount."

account = BankAccount("Alice", 1000)

print(account.owner)  

print(account.get_balance()) 

print(account.deposit(500)) 

print(account.withdraw(200))  
