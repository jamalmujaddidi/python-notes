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