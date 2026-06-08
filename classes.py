# class and object
# create car class with attributes(variables) like brand and model. then create an instance of that class
class Car:
  def __init__(self, brand, model): #self refers to whoever calls the function/context
      self.brand = brand #self.brand refers to the variables within the class, whereas brand model refers to paramaters passed by the user
      self.model = model

my_car = Car("toyota", "corolla") #object 
print(my_car.brand)
print(my_car.model)
my_new_car = Car("tata", "safari")
print(my_new_car.model)
# generalised form, usually the class is created in a seperate file imported whenever it is to be used 
