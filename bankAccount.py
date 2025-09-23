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

# Accessing public attribute
print(account.owner)  # Output: Alice

# Accessing private attribute (will raise an error)
# print(account.__balance)  # AttributeError

# Using getter method
print(account.get_balance())  # Output: 1000

# Using methods to modify private attribute
print(account.deposit(500))   # Output: Deposited 500. New balance: 1500
print(account.withdraw(200))  # Output: Withdrew 200. New balance: 1300
