# 4 pillars of OOPS
# 1. ABSTRACTION - hiding implementation details(unnecessary features) of a class and only showing the essential features to the user
class Car():
  def __init__(self):
    self.clutch = False
    self.brr = False
    self.acc = False

  def start(self):
    self.clutch = True
    self.acc = True
    print("car is starting ...")

car1 = Car()
car1.start()

# 2. ENCAPSULATION - wrapping data and functions into a single unit (object)
# Private attributes exist to enforce encapsulation. 
# They prevent external code from directly modifying sensitive data.
# _attribute → protected (intended for internal use, but still accessible).
# __attribute → private (name-mangled to prevent direct access outside the class).

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute

    # Public method to access private data
    def get_balance(self):
        return self.__balance

    # Public method to modify private data safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

# Usage
account = BankAccount("Alice", 1000)
print(account.get_balance())   # Access via method
account.deposit(500)
print(account.get_balance())

# print(account.__balance)    Error: Attribute not directly accessible

# 3. INHERITANCE
# 4. POLYMORPHISM 
