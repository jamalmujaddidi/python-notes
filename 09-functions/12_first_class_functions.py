# ============================================================
# 12. FIRST-CLASS FUNCTIONS
# ============================================================
# In Python, functions are first-class objects.
#
# This means a function can be:
# 1. Assigned to a variable
# 2. Passed as an argument to another function
# 3. Returned from a function
# 4. Stored in data structures


# ============================================================
# 12.1 ASSIGNING A FUNCTION TO A VARIABLE
# ============================================================

def greet():
    print("Hello Mr Smith")


# Assigning the function object to another variable.
# Parentheses are NOT used because we are not calling the function.
message = greet

# Calling the function through the new variable.
message()

# Output:
# Hello Mr Smith


# Both names refer to the same function object.
print(greet is message)

# Output:
# True


# ------------------------------------------------------------
# Difference between a function and calling a function
# ------------------------------------------------------------

def add_numbers(a, b):
    return a + b


# 'add_numbers' refers to the function object.
operation = add_numbers

# 'operation()' calls the function.
result = operation(10, 90)

print(result)

# Output:
# 100


# ============================================================
# 12.2 PASSING A FUNCTION AS AN ARGUMENT
# ============================================================


# ------------------------------------------------------------
# Example 1: Passing a function that takes no arguments
# ------------------------------------------------------------

def demo():
    print("Hello Mr Smith")


def display(func):
    func()


display(demo)

# Output:
# Hello Mr Smith


# ------------------------------------------------------------
# Example 2: Passing another function that takes no arguments
# ------------------------------------------------------------

def add():
    print(10 + 30)


def execute(operation):
    operation()


execute(add)

# Output:
# 40


# ------------------------------------------------------------
# Example 3: Passing a function that requires arguments
# ------------------------------------------------------------

def mul(a, b):
    print(a * b)


def execute_with_values(operation):
    operation(200, 8)


execute_with_values(mul)

# Output:
# 1600


# ------------------------------------------------------------
# Example 4: Passing a function that returns a value
# ------------------------------------------------------------

def bonus():
    bon = 2000
    return bon


def salary(calculation):
    sal = 45000
    total = calculation() + sal
    print(total)


salary(bonus)

# Output:
# 47000


# ------------------------------------------------------------
# Example 5: Passing different functions to the same function
# ------------------------------------------------------------

def addition():
    return 10 + 20


def multiplication():
    return 10 * 20


def calculate(operation):
    print(operation())


calculate(addition)
calculate(multiplication)

# Output:
# 30
# 200



# ============================================================
# 12.3 Returning a Function from a Function
# ============================================================

# A function can return another function because functions
# are first-class objects in Python.

# Example 1: Returning a function

def outer():

    def inner():
        print("Hello Mr Smith")

    return inner


result = outer()

result()

# Output:
# Hello Mr Smith

# Explanation:
# outer() is called first.
# return inner returns the function object itself.
# Therefore, result refers to the inner function.
# result() then calls the returned function.


# ------------------------------------------------------------
# return inner vs return inner()
# ------------------------------------------------------------

# Example 2: Returning the result of calling a function

def outer():

    def inner():
        return 100

    return inner()


result = outer()

print(result)

# Output:
# 100

# Explanation:
# return inner() calls inner immediately.
# inner() returns 100.
# Therefore, outer() returns 100.
# result refers to the returned integer 100.


# Important difference:
#
# return inner
# -> returns the function object itself.
#
# return inner()
# -> calls the function and returns its result.


# ------------------------------------------------------------
# Example 3: Selecting which function to return
# ------------------------------------------------------------

def get_operation(choice):

    def add():
        return 10 + 20

    def multiply():
        return 10 * 20

    if choice == "add":
        return add
    else:
        return multiply


operation = get_operation("add")

print(operation())

# Output:
# 30

# Explanation:
# get_operation("add") returns the add function.
# operation therefore refers to the add function.
# operation() calls add() and returns 30.

# If we used:
#
# operation = get_operation("multiply")
#
# then operation would refer to multiply,
# and print(operation()) would output:
# 200


# ------------------------------------------------------------
# Example 4: Returning a function and using user input
# ------------------------------------------------------------

def square(number):
    return number * number


def get_function():
    return square


final = get_function()

num = int(input("Enter a number to get its square: "))

print(final(num))

# Example Output:
# Enter a number to get its square: 7
# 49

# Explanation:
# get_function() returns the square function.
# Therefore, final refers to the square function.
# final(num) is equivalent to square(num).


# ============================================================
# 12.4 Storing Functions in Data Structures
# ============================================================

# Because functions are first-class objects, they can also be
# stored in Python data structures such as lists, tuples,
# and dictionaries.


# ------------------------------------------------------------
# 12.4.1 Storing Functions in a List
# ------------------------------------------------------------

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


operations = [add, multiply]

print(operations)

# Output will look similar to:
# [<function add at 0x...>, <function multiply at 0x...>]

# The exact memory addresses (0x...) will be different.
#
# add and multiply are stored as function objects.
# We do not use add() or multiply() when storing them because
# parentheses would call the functions.


# Functions stored in the list can also be called.

print(operations[0](10, 5))
print(operations[1](10, 5))

# Output:
# 15
# 50

# operations[0] refers to add.
# Therefore:
# operations[0](10, 5) is equivalent to add(10, 5).
#
# operations[1] refers to multiply.
# Therefore:
# operations[1](10, 5) is equivalent to multiply(10, 5).


# ------------------------------------------------------------
# 12.4.2 Storing Functions in a Tuple
# ------------------------------------------------------------

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


operations = (add, multiply)

print(operations[0](10, 5))
print(operations[1](10, 5))

# Output:
# 15
# 50

# Explanation:
# operations = (add, multiply) stores the function objects
# inside the tuple.
#
# operations[0] refers to add.
# operations[0](10, 5) is equivalent to add(10, 5).
#
# operations[1] refers to multiply.
# operations[1](10, 5) is equivalent to multiply(10, 5).


# ------------------------------------------------------------
# 12.4.3 Storing Functions in a Dictionary
# ------------------------------------------------------------

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


operations = {
    "addition": add,
    "multiplication": multiply
}

print(operations["addition"](10, 5))
print(operations["multiplication"](10, 5))

# Output:
# 15
# 50

# Explanation:
# "addition" is mapped to the add function.
# "multiplication" is mapped to the multiply function.
#
# operations["addition"] refers to add.
# Therefore:
# operations["addition"](10, 5) is equivalent to add(10, 5).
#
# operations["multiplication"] refers to multiply.
# Therefore:
# operations["multiplication"](10, 5) is equivalent to
# multiply(10, 5).


# ============================================================
# Key Summary
# ============================================================

# First-class functions can be:
#
# 1. Assigned to a name
# 2. Passed as an argument
# 3. Returned from a function
# 4. Stored in data structures
#
# Important distinction:
#
# function
# -> refers to the function object
#
# function()
# -> calls the function
#
# Example:
#
# result = get_function()
# -> result refers to whatever get_function() returns.
#
# If get_function() returns a function, result refers to
# that function.
#
# If get_function() returns a value such as 100, result refers
# to the value 100.