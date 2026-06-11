# class method - is bound to teh class and recieves the class as an implicit first argument
# static method cannot access or modify class state and generally used for utility
class Person():
  name = 'kas'
  
''' 
  def change_name(self,name):
    #self.name = name creates a new name instance
    Person.name = name 
    self.__class__.name = "kai"
  
p1 = Person()
p1.change_name('kai')
print(p1.name)
print(Person.name) #kas still appearing as output
'''
  
  @classmethod #decorator
  def change_name(cls, name):
    cls.name = name #changes in the class directly

#types of functions
# 1. static methods - () do not change or access 
# 2. class methods - (cls)
# 3. instance methods - uses (self) as an argument
