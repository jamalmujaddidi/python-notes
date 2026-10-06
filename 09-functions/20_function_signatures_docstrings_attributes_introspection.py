# ============================================================
# Python Functions - Topic 20
# Function Signatures, Docstrings, Attributes & Introspection
# ============================================================


# ============================================================
# 20.1 Function Signatures
# ============================================================

# A function signature describes the structure of a function,
# especially its parameters and the rules for passing arguments.

def greet(name, age=25):
    print(name, age)


# Signature:
# greet(name, age=25)

# Function definition:
# def greet(name, age=25):

# Function call:
# greet("John Smith", 30)


# A function can have different kinds of parameters in its signature.

def example(a, b=10, *args, c=20, **kwargs):
    pass


# Signature:
# example(a, b=10, *args, c=20, **kwargs)


# inspect.signature() can be used to retrieve a function's
# signature programmatically.

import inspect


def calculate_total(price, quantity=1, *, tax=0):
    return price * quantity + tax


print(inspect.signature(calculate_total))

# Output:
# (price, quantity=1, *, tax=0)


# ============================================================
# 20.2 Docstrings
# ============================================================

# A docstring is a string used to document a function, class,
# method, or module.
#
# For a function, the docstring must be the first statement
# inside the function body.

def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")


print(greet.__doc__)

# Output:
# Greet a person by name.


# A docstring can contain more detailed information.

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle.
    """
    return length * width


print(calculate_area.__doc__)

# Output:
#
#     Calculate the area of a rectangle.
#
#     Parameters:
#         length: The length of the rectangle.
#         width: The width of the rectangle.
#
#     Returns:
#         The area of the rectangle.


# help() can also display documentation about a function.

help(greet)


# Difference between a comment and a docstring:
#
# Comment:
#   Used mainly for explaining code to programmers.
#
# Docstring:
#   Used to document a function, class, method, or module
#   and can be accessed at runtime through __doc__.


# ============================================================
# 20.3 Function Attributes
# ============================================================

# Functions are objects in Python, so they can have attributes.

# Attributes are accessed using the dot (.) operator:
#
# function.attribute


def greet_person(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")


print(greet_person.__name__)
print(greet_person.__doc__)

# Output:
# greet_person
# Greet a person by name.


# Some useful function attributes:

# __name__
#   The name of the function.

# __doc__
#   The function's docstring.

# __module__
#   The module where the function was defined.

# __annotations__
#   A dictionary containing the function's annotations.


def add(a: int, b: int) -> int:
    return a + b


print(add.__annotations__)

# Output:
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


# Functions can also have custom attributes.

def greet_user(name):
    print(f"Hello, {name}!")


greet_user.category = "Greeting"
greet_user.author = "John Smith"

print(greet_user.category)
print(greet_user.author)

# Output:
# Greeting
# John Smith


# dir() can be used to see the attributes and methods
# available on a function object.

print(dir(greet_user))


# ============================================================
# 20.4 Function Introspection
# ============================================================

# Function introspection is the process of examining a function
# at runtime to obtain information about its attributes,
# signature, docstring, annotations, and other details.


# Using __name__ and __doc__

def welcome(name):
    """Welcome a person by name."""
    print(f"Welcome, {name}!")


print(welcome.__name__)
print(welcome.__doc__)

# Output:
# welcome
# Welcome a person by name.


# Using __annotations__

def multiply(a: int, b: int) -> int:
    return a * b


print(multiply.__annotations__)

# Output:
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


# Using inspect.signature()

def calculate_price(price, quantity=1, *, tax=0):
    return price * quantity + tax


print(inspect.signature(calculate_price))

# Output:
# (price, quantity=1, *, tax=0)


# Using dir()

print(dir(calculate_price))


# Important tools for function introspection:
#
# dir(function)
# function.__name__
# function.__doc__
# function.__annotations__
# inspect.signature(function)


# ============================================================
# 20.5 Practical Example
# ============================================================

# The following example combines function signatures,
# docstrings, attributes, annotations, and introspection.

def calculate_bill(price: float, quantity: int = 1, *, tax: float = 0):
    """
    Calculate the total bill including tax.

    Parameters:
        price: Price of one item.
        quantity: Number of items.
        tax: Additional tax amount.

    Returns:
        The total bill.
    """
    return price * quantity + tax


# Function name
print(calculate_bill.__name__)

# Function documentation
print(calculate_bill.__doc__)

# Function annotations
print(calculate_bill.__annotations__)

# Function signature
print(inspect.signature(calculate_bill))

# Available attributes and methods
print(dir(calculate_bill))

# Output:
# calculate_bill
#
#     Calculate the total bill including tax.
#
#     Parameters:
#         price: Price of one item.
#         quantity: Number of items.
#         tax: Additional tax amount.
#
#     Returns:
#         The total bill.
#
# {'price': <class 'float'>,
#  'quantity': <class 'int'>,
#  'tax': <class 'float'>,
#  'return': <...>}
#
# (price: float, quantity: int = 1, *, tax: float = 0)
#
# [list of available attributes and methods]



# ============================================================
# 20.7 Summary
# ============================================================

# 1. Function Signature
#    Describes the structure of a function, especially its
#    parameters and argument-passing rules.
#
#    inspect.signature(function) can retrieve the signature.


# 2. Docstring
#    A string used to document a function, class, method,
#    or module.
#
#    A function's docstring can be accessed using:
#    function.__doc__


# 3. Function Attributes
#    Functions are objects, so they can have attributes.
#
#    Important attributes include:
#    __name__
#    __doc__
#    __module__
#    __annotations__
#
#    Custom attributes can also be attached to functions.


# 4. Function Introspection
#    The process of examining a function at runtime to obtain
#    information about its attributes, signature, docstring,
#    annotations, and other details.
#
#    Common tools:
#    dir()
#    __name__
#    __doc__
#    __annotations__
#    inspect.signature()


# ============================================================
# End of Topic 20
# Python Functions - COMPLETE
# ============================================================