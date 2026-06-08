# 1. class and object
# create car class with attributes(variables) like brand and model. then create an instance of that class

class Car:
  total_cars = 0 
  def __init__(self, brand, model): #self refers to whoever calls the function/context, __init__ function is known as a  constructor
      self.__brand = brand #self.brand refers to the variables within the class, whereas brand model refers to paramaters passed by the user
      #brand is privated using encapsulation 
      self.model = model
      Car.total_car += 1
    
  # 4. Encapsulation
  # modify car class to encapsulate the brand attribute, making it private and provide a getter method for it 

  def get_brand(self):
    return self.__brand + " !"
    
  # 2. class method and self 
  # add a method to car which displays the full name of the car the model and the name

  def full_name(self):
    return f"{self.__brand}{self.model}" #formatted string

# 5. Polymorphism
# demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes with different behaviour
def fuel_type(self): # method 
  return "Petrol and Diesel"

# 3. Inheritance 
# create an electric car class that oinherits from car class and has an additional attribute battery_size 
class ElectricCar(Car): # inherits proprties of car class ie brand and model
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model) 
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"
  
my_tesla = ElectricCar("tesla", "model s", "85kWH")
print(my_tesla.model)
print(my_tesla.get_brand())

safari = Car("tata", "safari")
print(safari.fuel_type())

my_car = Car("toyota", "corolla") # object 
print(my_car.__brand)
print(my_car.model)
my_new_car = Car("tata", "safari")
print(my_new_car.model) # class defination hence no paranthesis needed
# generalised form, usually the class is created in a seperate file imported whenever it is to be used 

print(my_new_car.full_name()) # defined functions adds functionality, hence paranthesis should be added to the function call
