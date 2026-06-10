# create student class that takes name and marks of 3 subjects as arguments in constructor. then create a method to print the average
class Student:
  def __intit__(self, name, marks):
    self.name = name
    self.marks = marks
    
  def get_avg(self):
    sum = 0
    for val in marks:
      sum += val
      print(self.name, "your avg score is ", sum/3)
      
s1=Student("tony stark", [98,99,67])
