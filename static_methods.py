#static methods - methods that don't use the self parameter (work at class level)
class Student:
  @staticmethod #converts a normal function to be a static method
  def college():
    print("ABC college")

#decorators allow us to wrap another function in order to extend behavior of the wrapped function, without permanently modifying it


