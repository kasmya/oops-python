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

# print(account.__balance)    Error: Attribute not directly accessible by user but can be accessed by internal functions in the class
# done to prevent exposing instance attributes outside the class

# example:
class Person():
    __name = "kas" #private attribute

 def __hello(self): 
    print("hello person")

 def welcome(self):
   self.__hello()

p1 = Person()
print(p1.welcome())

# 3. INHERITANCE - when one class derives properties and methods of another class 
# inherits logic from another class, reduces rewriting of code
class Car():
  def __init__(self,type):
    self.type = type
  
  color = "pink"
  @staticmethod
  def start():
    print("car is starting...")

  @staticmethod
  def stop():
    print("car is stopping...")

class ToyotaCar(Car): #ToyotaCar inherits from Car class, single level
  def __init__(self, brand):
    #self.name = name
    self.brand = brand

class Fortuner(ToyotaCar): #multi level inheritance 
  def __init__(self):
    self.type = type
    super().__init__(type) #super method - used to access methods of the parent class 
    super.start() 

car2 = Fortuner("diesel")
car2.start()
  
print(car2.type)

#car1=ToyotaCar("fortuner")
#print(car1.start())
#print(car1.color)

#types of inheritance
#1. single inheritance - single parent/base class gives single child/derived class 
#2. multi level inheritance - parent class - child class (parent to next class) - grandchild (child to preceding class, containing properties of both preceding classes) 
#3. multiple inheritance - child/derived class can inherit properties from multiple parent classes

class A:
  varA = "welcome to class A"

class B:
  varB = "welcome to class B"

class C(A,B): #multiple inheritance
  varC = "welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

# 4. POLYMORPHISM - ex. Operator Overloading
# when same operator is allowed to have different meaning according to the context

print(1+2) #add
print(type(1)) #class int 

print('6'+'7') #concatenate
print(type('6') #class string
      
print([6]+[7]) #merge
print(type([6])) #class list

#for each class the meaning of the operator is defined by python implicitly
#in oops we can define the meaning of any operator as per our requirement using dunder functions (functions starting and ending with __)
class Complex:
  def __init__(self, real, img):
    self.real = real
    self.img = img

  def __add__(self, num2): #dunder function
    newReal = self.real + num2.real
    newImg = self.img + num2.img
    return Complex(newReal, newImg)

   def __sub__(self, num2): #dunder function
    newReal = self.real - num2.real
    newImg = self.img - num2.img
    return Complex(newReal, newImg)
     
  def show_number(self):
    print(self.real, "i +", self.img, "j")

num1 = Complex(1,2)
num1.show_number()

num2 = Complex(3,2)
num2.show_number()

num3 = num1 + num2  #using dunder functions complex numbers can be added, logic is defined
num3.show_number()

num4 = num2 - num1
num4.show_number()
