# ============================================================
# Topic 21 - Object-Oriented Programming (OOP)
# ============================================================


# ============================================================
# 21.0 Overview of OOP
# ============================================================

# Object-Oriented Programming (OOP) is a programming paradigm
# based on classes and objects. It organizes programs around
# objects that combine data (attributes) and behavior (methods).
#
# OOP helps developers build modular, maintainable, and
# scalable applications.
#
# A programming paradigm is a general approach or style used
# to design and structure programs.


# ============================================================
# 21.1 Classes and Objects
# ============================================================

# A class is a blueprint or definition that describes what
# objects can have and what they can do.
#
# A class can define attributes and methods. Objects created
# from the class can have their own instance attributes and
# access attributes and methods defined by the class.
#
# In Python, a class is itself an object that exists in memory.
# The blueprint analogy describes its role in defining the
# structure and behavior of its instances.
#
# We define a class using the 'class' keyword followed by
# the class name.


class Car:
    pass


# An object is an instance of a class.
# An object is created by calling the class.

car1 = Car()
car2 = Car()

print(isinstance(car1, Car))
# Output:
# True

# One class can create many objects. Each object is a separate
# instance of the same class.


# ------------------------------------------------------------
# Attributes and Methods: Basic Terminology
# ------------------------------------------------------------

# Attributes are data or characteristics associated with an
# object. They describe what an object has.
#
# State is the current condition of an object, represented by
# the values of its attributes.
#
# Methods are functions defined in a class that implement
# behavior associated with its objects.
#
# Behavior describes what an object does, usually through
# its methods.
#
# In a simple model:
# Object = data/state (attributes) + behavior (methods)



# ============================================================
# 21.1.1 Class Attributes
# ============================================================

# Class attributes are defined in the class body, outside
# methods. They belong to the class and can be accessed
# through the class name or through its instances.


class Marks:
    mathematics = 100
    physics = 85
    english = 70


# Accessing class attributes through the class name
print(Marks.mathematics)
print(Marks.physics)
print(Marks.english)

print("=============================================")

# Creating an instance
marks1 = Marks()

# Accessing class attributes through the instance
print(marks1.mathematics)
print(marks1.physics)
print(marks1.english)

# Output:
# 100
# 85
# 70
# =============================================
# 100
# 85
# 70



# ============================================================
# 21.1.2 Instance Attributes
# ============================================================

# Instance attributes belong to individual objects.
# Each object has its own instance attributes, and their
# values can be the same or different from other objects.
#
# They are commonly initialized inside __init__() using self.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"His name is {self.name} and he is {self.age} years old.")


student1 = Student("John Smith", 24)
student1.display_info()
print(student1.name)

print("===========================================")

student2 = Student("Alex", 22)
student2.display_info()
print(student2.age)

# Output:
# His name is John Smith and he is 24 years old.
# John Smith
# ===========================================
# His name is Alex and he is 22 years old.
# 22



# ============================================================
# 21.1.3 Types of Methods in classes and objects:
# ============================================================
'''
A method is a function defined inside a class that represents or performs behaviour(actions) 
associated with the class or its objects.

•	It is similar to a function, but it is associated with a class or an object.
•	It operates on the data (attributes or properties) stored within an object.
•	It helps reuse code by defining a behaviour once and using it across multiple objects

We have three types of methods in python with respect to classes and objects:
1)	Instance methods
 
An instance method is a function defined inside a class that operates on a specific object 
(instance) of that class.
Instance methods commonly use self as their first parameter. When called through an object, 
Python automatically passes that object as the first argument.

'''
# Example

class Teacher:
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

    def instance_method(self):
        print(f"He is our best teacher, and his position is {self.position}.")
        print(f"As he holds the position of {self.position}, his salary is {self.salary}.")

teacher = Teacher("Head Master", "7500$")

print(teacher.position)
print(teacher.salary)
teacher.instance_method()


# output:
# Head Master
# 7500$
# He is our best teacher, and his position is Head Master.
# As he holds the position of Head Master, his salary is 7500$.