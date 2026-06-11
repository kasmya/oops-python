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
## 📝 Types of Methods in Python Classes

### 1. Instance Methods
- Defined with `self` as the first parameter.
- Operate on a specific object instance.
- Can access and modify **instance attributes**.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):   # instance method
        return f"Car brand is {self.brand}"
```
### 2. Class Methods
- Defined with @classmethod decorator.
- First parameter is cls (the class itself).
- Can access and modify class-level attributes.
- Often used for factory methods.
  
```python
class Car:
    wheels = 4

    @classmethod
    def show_wheels(cls):   # class method
        return f"Cars have {cls.wheels} wheels"
```
### 3. Static Methods
- Defined with @staticmethod decorator.
- No self or cls parameter.
- Behave like normal functions but live inside the class namespace.
- Used for utility/helper functions.

```python
class Car:
    @staticmethod
    def greet(name):   # static method
        return f"Hello, {name}!"
```
## 🔑 Static vs Non‑Static Methods in Python

- **Static Methods (`@staticmethod`)**
  - No `self` or `cls`.
  - Do not access or modify instance/class state.
  - Used for utility/helper functions.

- **Non‑Static Methods**
  - **Instance Methods (`self`)** → bound to object, access instance data.
  - **Class Methods (`cls`)** → bound to class, access class data.

## 🎀 Python Decorators 

### 🔹 @staticmethod
- No `self` or `cls`.
- Acts like a plain function inside the class.
- Use for **utility/helper functions** that don’t depend on instance or class data.

### 🔹 @classmethod
- First argument is `cls` (the class itself).
- Can access/modify **class-level attributes**.
- Use for **factory methods** or logic that applies to the whole class.

### 🔹 @property
- First argument is `self` (instance).
- Turns a method into a **read-only attribute**.
- Use for **controlled access to instance data** (getter/setter/deleter).

### ⚖️ Quick Memory Hook
- **Static → utility only**  
- **Class → class-wide logic**  
- **Property → instance attribute access**
