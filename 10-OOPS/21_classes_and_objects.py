# ============================================================
# Topic 21 - Object-Oriented Programming (OOP)
# ============================================================


# ============================================================
# 21.0 Overview of OOP
# ============================================================

# Object-Oriented Programming (OOP) is a programming paradigm
# based on objects, which encapsulate data (attributes) and
# behavior (methods), and classes, which define the structure
# and behavior of those objects.

# A programming paradigm is a general approach or style used
# to design and structure programs.

# OOP helps developers build modular, maintainable, and
# scalable applications.

# Attributes represent an object's data/state.
# Methods represent or implement an object's behavior.

# Object = attributes (data/state) + methods (behavior/actions)


# ============================================================
# 21.1 Classes and Objects
# ============================================================

# A class defines the structure and behavior that objects
# created from it can have.

# An object is an instance of a class.


class Student:
    pass


student1 = Student()
student2 = Student()

print(isinstance(student1, Student))
# Output:
# True


# One class can create many objects.
# Each object is a separate instance of the class.


# ------------------------------------------------------------
# Class Attributes
# ------------------------------------------------------------

class Student:
    name = "John Smith"
    age = 25
    course = "Computer Science"


student1 = Student()

print(student1.name)
print(student1.age)
print(student1.course)

# Output:
# John Smith
# 25
# Computer Science


# ------------------------------------------------------------
# Instance Attributes
# ------------------------------------------------------------

# Instance attributes belong to a particular object.
# Different objects can have different values.


class Student:
    pass


student1 = Student()
student2 = Student()

student1.name = "John Smith"
student2.name = "Alice"

print(student1.name)
print(student2.name)

# Output:
# John Smith
# Alice


# ------------------------------------------------------------
# __new__()
# ------------------------------------------------------------

# __new__() is responsible for creating and returning a
# new instance of a class.
#
# It runs before __init__().
#
# It is normally not overridden in ordinary classes.


# ------------------------------------------------------------
# __init__()
# ------------------------------------------------------------

# __init__() initializes a newly created instance.
#
# It is commonly used to initialize instance attributes
# and establish the object's initial state.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("John Smith", 25)

print(student1.name)
print(student1.age)

# Output:
# John Smith
# 25


# ------------------------------------------------------------
# __new__() vs __init__()
# ------------------------------------------------------------

# __new__() -> creates and returns the new instance.
# __init__() -> initializes the newly created instance.

# General sequence:
#
# Student()
#     ↓
# __new__()
#     ↓
# New instance is created
#     ↓
# __init__()
#     ↓
# Instance is initialized
#     ↓
# Object is ready to use

# If __new__() and __init__() are not explicitly defined,
# Python uses inherited/default behavior.