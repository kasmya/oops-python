# oops-python

A beginner-friendly repository to learn and revise **Object-Oriented Programming (OOP) concepts in Python**.  
Perfect for placement preparation, interview revision, and hands-on coding practice.

---

## 📘 What is OOP?

Object-Oriented Programming (OOP) is a paradigm based on the concept of **objects**.  
Objects contain **data** (attributes) and **methods** (functions) that operate on the data.

### 🔑 Key Concepts

- **Class** → A blueprint for creating objects.  
- **Object** → An instance of a class.  
- **Encapsulation** → Bundling data and methods together, restricting direct access.  
- **Inheritance** → Mechanism to derive new classes from existing ones.  
- **Polymorphism** → Ability to use the same interface for different data types.  
- **Abstraction** → Hiding implementation details and showing only essential features.

---

## 🐍 Example Code

### 1. Class and Object
```python
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

# Object creation
s1 = Student("Alice", 101)
s1.display()
```
### 2. Inheritance
```python
class Animal:
    def speak(self):
        print("This is an animal.")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

# Example
a = Animal()
a.speak()

d = Dog()
d.speak()
```
### 3. Polymorphism
```python
class Bird:
    def fly(self):
        print("Bird can fly.")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly.")

# Polymorphism in action
for b in [Bird(), Penguin()]:
    b.fly()
```
### 4. Abstraction
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print("Area of circle:", c.area())
```
