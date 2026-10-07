
"""
TOPIC 15: LAMBDA FUNCTIONS
==========================

A lambda function is a small anonymous function defined using
the lambda keyword. It can accept zero or more arguments but
contains only one expression, whose result is returned automatically.

Topics:
    15.1 Introduction to Lambda Functions
    15.2 Syntax and Structure
    15.3 Lambda Function Arguments
    15.4 Lambda with map(), filter(), and sorted()
    15.5 Limitations of Lambda Functions
    15.6 Lambda vs. Regular Functions (def)
    15.7 Practice Examples
"""


# ============================================================
# 15.1 INTRODUCTION TO LAMBDA FUNCTIONS
# ============================================================

# A lambda function is an anonymous function defined using
# the lambda keyword. It contains a single expression and
# returns the expression's result automatically.

# Example 1: Regular function using def

def add_numbers(a, b):
    return a + b

print(add_numbers(10, 20))
# Output: 30


# Example 2: Equivalent lambda function

add = lambda a, b: a + b

print(add(10, 20))
# Output: 30


# Example 3: Lambda function without parameters

greet = lambda: "Hello, John Smith"

print(greet())
# Output: Hello, John Smith


# Example 4: Reusing a lambda function

square = lambda x: x ** 2

print(square(4))
# Output: 16

print(square(6))
# Output: 36


# ============================================================
# 15.2 SYNTAX AND STRUCTURE
# ============================================================

# Syntax:
# lambda arguments: expression

# Example 1: One parameter

double = lambda x: x * 2

print(double(5))
# Output: 10


# Example 2: Multiple parameters

multiply = lambda a, b: a * b

print(multiply(5, 4))
# Output: 20


# Example 3: Conditional expression

check_number = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_number(4))
# Output: Even

print(check_number(7))
# Output: Odd


# ============================================================
# 15.3 LAMBDA FUNCTION ARGUMENTS
# ============================================================

# Example 1: Default argument

greet_person = lambda name="John Smith": "Hello, " + name

print(greet_person())
# Output: Hello, John Smith

print(greet_person("Alex"))
# Output: Hello, Alex


# Example 2: Multiple arguments

subtract = lambda a, b: a - b

print(subtract(20, 5))
# Output: 15


# Example 3: Keyword arguments

divide = lambda a, b: a / b

print(divide(a=20, b=4))
# Output: 5.0


# ============================================================
# 15.4 LAMBDA WITH BUILT-IN HIGHER-ORDER FUNCTIONS
# ============================================================

# Python provides built-in higher-order functions that accept
# other functions as arguments. These functions make it easier
# to transform, filter, and organize data without explicit loops.


# ------------------------------------------------------------
# 15.4.1 map()
# ------------------------------------------------------------

# Definition:
# map() applies a given function to every element in an iterable
# and returns a map iterator that produces the transformed values.

# Syntax:
# map(function, iterable)


# Example 1: Squaring numbers

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x ** 2, numbers))

print(result)
# Output: [1, 4, 9, 16, 25]


# Example 2: Adding 10 to every number

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x + 10, numbers))

print(result)
# Output: [11, 12, 13, 14, 15]


# ------------------------------------------------------------
# 15.4.2 filter()
# ------------------------------------------------------------

# Definition:
# filter() selects elements from an iterable based on a condition.
# It returns a filter iterator containing elements for which
# the function returns a truthy value.

# Syntax:
# filter(function, iterable)


# Example 1: Filtering even numbers

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
# Output: [2, 4, 6]


# Example 2: Filtering numbers greater than 10

numbers = [5, 12, 8, 20, 3, 15]

result = list(filter(lambda x: x > 10, numbers))

print(result)
# Output: [12, 20, 15]


# ------------------------------------------------------------
# 15.4.3 sorted()
# ------------------------------------------------------------

# Definition:
# sorted() returns a new list containing the elements of an
# iterable in a specified order.

# Syntax:
# sorted(iterable, key=func)

# key:
# An optional parameter that accepts a function to determine
# the sorting criterion for each element.
#
# func is a placeholder for a function, such as a lambda function.
#
# reverse:
# An optional parameter. If True, sorts in descending order.
# Its default value is False.


# Example 1: Sorting by absolute value

numbers = [-10, 5, -3, 8, -1]

result = sorted(numbers, key=lambda x: abs(x))

print(result)
# Output: [-1, -3, 5, 8, -10]


# Example 2: Sorting names by length

names = ["Christopher", "John", "Alexander", "Emma"]

result = sorted(names, key=lambda name: len(name))

print(result)
# Output: ['John', 'Emma', 'Christopher', 'Alexander']


# Example 3: Sorting in descending order

numbers = [5, 2, 8, 1, 9]

result = sorted(numbers, key=lambda x: x, reverse=True)

print(result)
# Output: [9, 8, 5, 2, 1]


# Example 4: Sorting by remainder

numbers = [10, 3, 7, 1, 5]

result = sorted(numbers, key=lambda x: x % 3)

print(result)
# Output: [3, 10, 7, 1, 5]


# ============================================================
# 15.5 LIMITATIONS OF LAMBDA FUNCTIONS
# ============================================================

# 1. A lambda function can contain only one expression.
# 2. It cannot contain multiple statements or an explicit return.
# 3. Complex logic is generally more readable using def.

# Example: A lambda function with a conditional expression

check_number = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_number(8))
# Output: Even


# ============================================================
# 15.6 LAMBDA VS. REGULAR FUNCTIONS (def)
# ============================================================

# Regular function using def

def calculate_square(x):
    result = x ** 2
    return result

print(calculate_square(5))
# Output: 25


# Equivalent lambda function

calculate = lambda x: x ** 2

print(calculate(5))
# Output: 25


# Key differences:
#
# Lambda:
# - Defined using the lambda keyword.
# - Contains a single expression.
# - Returns the expression's result automatically.
# - Suitable for short, simple operations.
#
# Regular function:
# - Defined using the def keyword.
# - Can contain multiple statements.
# - Can use an explicit return statement.
# - Suitable for complex and reusable logic.


# ============================================================
# 15.7 PRACTICE EXAMPLES
# ============================================================

# Example 1: Multiply every number by 2 using map()

numbers = [2, 4, 6, 8]

result = list(map(lambda x: x * 2, numbers))

print(result)
# Output: [4, 8, 12, 16]


# Example 2: Select numbers greater than 10 using filter()

numbers = [5, 12, 8, 20, 3, 15]

result = list(filter(lambda x: x > 10, numbers))

print(result)
# Output: [12, 20, 15]


# Example 3: Sort names by length using sorted()

names = ["Christopher", "John", "Alexander", "Emma"]

result = sorted(names, key=lambda name: len(name))

print(result)
# Output: ['John', 'Emma', 'Christopher', 'Alexander']


# Example 4: Filter even numbers, then square them using map()

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

result = list(map(lambda x: x ** 2, even_numbers))

print(result)
# Output: [4, 16, 36, 64]


# Example 5: Sort by absolute value in descending order

numbers = [-10, 5, -3, 8, -1]

result = sorted(numbers, key=lambda x: abs(x), reverse=True)

print(result)
# Output: [-10, 8, 5, -3, -1]


# Example 5:

numbers = [10, 25, 7, 42, 18]

greatest = max(numbers, key=lambda number: number)

print(greatest)

# Output:
# 42