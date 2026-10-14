# ============================================================
# Topic 21 - Object-Oriented Programming (OOP)
# ============================================================
from time import time


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
# 21.1.3 Class Methods in Python:
# ============================================================

"""
We have three types of methods with respect to 
classes and objects:
"""


# ============================================================
# Class method
# 1. Definition of a Class Method
# ============================================================

"""
A class method is a method that is bound to a class rather than
a particular instance of that class.

A class method receives the class itself as its first argument,
conventionally named 'cls'.

The @classmethod decorator is used to define a class method.

- @classmethod converts a function into a class method.
- cls refers to the class passed automatically by Python.
- cls is a conventional parameter name, not a Python keyword.
- A class method can be called through the class without
  creating an instance.
"""


# ============================================================
# 2. Accessing and Modifying Class Attributes
# ============================================================

"""
Class methods can access and modify class attributes using cls.
"""

class School:

    school_name = "Green Valley School"

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school


School.change_school("Central Public School")

print(School.school_name)

# Output:
# Central Public School


# ============================================================
# 3. Calling a Class Method Through the Class and an Instance
# ============================================================

"""
A class method can be called through either the class or an
instance. In both cases, Python automatically passes the class
as the first argument.
"""

class Student:

    school = "Green Valley School"

    @classmethod
    def display_school(cls):
        print(cls.school)


# Calling through the class
Student.display_school()

# Output:
# Green Valley School

# Creating an instance
student1 = Student()

# Calling through the instance
student1.display_school()

# Output:
# Green Valley School

"""
In both calls, cls refers to the Student class, not to student1.

Calling a class method through an instance does not turn it into
an instance method.
"""


# ============================================================
# 4. Class Method vs. Instance Method
# ============================================================

"""
An instance method receives an instance as its first argument,
conventionally named self.

A class method receives the class as its first argument,
conventionally named cls.
"""

class StudentDetails:

    school = "Green Valley School"

    def __init__(self, name):
        self.name = name

    # Instance method
    def display_name(self):
        print(self.name)

    # Class method
    @classmethod
    def display_school(cls):
        print(cls.school)


student2 = StudentDetails("John Smith")

student2.display_name()

# Output:
# John Smith

StudentDetails.display_school()

# Output:
# Green Valley School

"""
Key differences:

- self refers to an instance.
- cls refers to the class.
- Instance methods commonly work with instance data.
- Class methods commonly perform operations related to the class.

Instance methods can also access class attributes, and class
methods can be called through instances.
"""


# ============================================================
# 5. Alternative Constructors
# ============================================================

"""
An alternative constructor provides another way to create an
instance besides the normal class call.

Alternative constructors are commonly implemented using
class methods.

They are useful when input must be processed or converted
before creating an object.
"""

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, product_data):
        name, price = product_data.split(",")
        return cls(name, float(price))


# Regular construction
product1 = Product("Mouse", 25)

# Alternative construction
product2 = Product.from_string("Keyboard,50")

print(product1.name, product1.price)

# Output:
# Mouse 25

print(product2.name, product2.price)

# Output:
# Keyboard 50.0

"""
How the alternative constructor works:

1. from_string() receives the class through cls.
2. product_data receives the input string.
3. split(",") separates the product name and price.
4. float(price) converts the price to a float.
5. cls(name, float(price)) creates a Product instance.
6. return returns the newly created instance.

The statement:

product2 = Product.from_string("Keyboard,50")

calls the class method and assigns the returned object to
product2.

The object is created inside the method by cls(...).
"""


# ============================================================
# 6. When to Use Alternative Constructors
# ============================================================

"""
Alternative constructors are useful when:

- Data is received as a string and must be parsed.
- Data comes from a dictionary or API response.
- Data is loaded from a file or database record.
- A named method provides a convenient way to create an object
  from a particular input format.

Examples of programmer-defined method names include:

- from_string()
- from_dict()
- from_record()

These are not special Python methods.

An alternative constructor is not required for every class.
If the regular constructor already handles the input clearly,
an alternative constructor may be unnecessary.
"""


# ============================================================
# 7. Summary
# ============================================================

"""
- @classmethod defines a class method.
- cls conventionally refers to the class passed automatically.
- Class methods can access and modify class attributes.
- Class methods can be called through the class or an instance.
- Instance methods receive an instance through self.
- Class methods receive the class through cls.
- Alternative constructors provide additional ways to create
  instances.
- cls(...) calls the class to create an instance.
- return sends the created instance back to the caller.
- The assignment statement stores a reference to that instance.
"""


# ============================================================
# 21.1.4 Instance Method in Python
# ============================================================

'''
	Instance methods
Instance Methods works directly with an individual object's data 
and can access its unique variables.
Or 
An instance method is a function defined inside a class that operates 
on a specific object (instance) of that class.

Instance methods commonly use self as their first parameter. When 
called through an object, Python automatically passes that object as the first argument.
'''

class Teacher:
    def __init__ (self, position, salary):
        self.position = position
        self.salary = salary

    def instance_method(self):
        print (f"He is our best teacher, and his position is {self.position}.")
        print (f"As he holds the position of {self.position}, his salary is {self.salary}.")

teacher = Teacher("Head Master", "7500$")

print(teacher.position)
print(teacher.salary)
teacher.instance_method()


# Output

# Head Master
# 7500$
# He is our best teacher and his position is Head Master.
# As he has Head Master position, His salary is 7500$.





# ======================================
# Topic 21.1.5: Static Methods in Python
# ======================================
"""
A static method is a method defined inside a class using the
@staticmethod decorator.

A static method does not receive an instance (self) or the class (cls)
automatically as its first argument.

It is useful when a function is logically related to a class but does
not need instance-specific or class-specific data to perform its task.

The @staticmethod decorator is a built-in Python decorator.
"""


# ============================================================
# 1. Defining a Static Method
# ============================================================

class Product:

    @staticmethod
    def is_valid_price(price):
        """Check whether a price is greater than zero."""
        return price > 0


# Calling the static method using the class name
print(Product.is_valid_price(50))
print(Product.is_valid_price(-10))

# Output:
# True
# False


# ============================================================
# 2. Calling a Static Method Through an Instance
# ============================================================

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def is_valid_price(price):
        """Check whether a given price is valid."""
        return price > 0


product1 = Product("Keyboard", 50)

# Calling the static method through an instance
print(product1.is_valid_price(100))
print(product1.is_valid_price(-5))

# Output:
# True
# False

# Note:
# Python does not automatically pass product1 to the static method.
# The argument 100 is passed explicitly; the method does not
# automatically use product1.price.


# ============================================================
# 3. Accessing Class Attributes in a Static Method
# ============================================================

class Product:

    category = "Electronics"  # Class attribute

    @staticmethod
    def display_category():
        print(Product.category)


Product.display_category()

# Output:
# Electronics

# Note:
# A static method can access a class attribute by explicitly
# referencing it through the class name: Product.category.
#
# Unlike a class method, it does not receive the class
# automatically through a cls parameter.



# ============================================================
# 4. A Practical Example: Price Validation
# ============================================================

class Product:

    category = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        """Display the product's individual information."""
        print(f"Product: {self.name}")
        print(f"Price: ${self.price}")

    @staticmethod
    def is_valid_price(price):
        """Return True if the supplied price is positive."""
        return price > 0


product1 = Product("Keyboard", 50)

product1.display_product()

print(Product.is_valid_price(50))
print(Product.is_valid_price(-10))

# Output:
# Product: Keyboard
# Price: $50
# True
# False


# ============================================================
# 5. Static Method vs Instance Method vs Class Method
# ============================================================

class Example:

    category = "General"

    def instance_method(self):
        """An instance method receives self automatically."""
        return self.category

    @classmethod
    def class_method(cls):
        """A class method receives cls automatically."""
        return cls.category

    @staticmethod
    def static_method():
        """A static method receives neither self nor cls."""
        return Example.category


example1 = Example()

print(example1.instance_method())
print(Example.class_method())
print(Example.static_method())

# Output:
# General
# General
# General


# ============================================================
# 6. When to Use Static Methods
# ============================================================

# Static methods are useful for:
#
# 1. Validation
#    Example: checking whether a price is positive.
#
# 2. Calculations
#    Example: calculating a percentage or converting units.
#
# 3. Formatting
#    Example: formatting a product code.
#
# 4. Utility operations logically related to a class
#    that do not require instance or class state.


# ============================================================
# 7. When NOT to Use Static Methods
# ============================================================

# Use an instance method when the operation needs instance data
# through self.
#
# Use a class method when the operation needs the class through cls,
# such as an alternative constructor.
#
# Use a regular function outside the class when the operation
# is not logically related to the class.


# ============================================================
# 8. Summary
# ============================================================

# 1. Use @staticmethod to define a static method.
#
# 2. A static method receives neither self nor cls automatically.
#
# 3. It can accept ordinary arguments and return values.
#
# 4. It can be called through the class name or an instance.
#
# 5. It can access class attributes explicitly using the class name,
#    for example, Product.category.
#
# 6. Use it for related utility operations that do not need
#    instance-specific or class-specific state.
#
# 7. If an operation needs self or cls automatically, consider
#    an instance method or class method instead.