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


# 3. INHERITANCE
# 4. POLYMORPHISM 
