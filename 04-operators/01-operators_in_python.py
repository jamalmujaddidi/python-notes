"""
TOPIC: OPERATORS IN PYTHON
==========================

An operator is a special symbol or keyword that performs an operation on
one or more operands (values or variables) and produces a result.

Example:
    a = 10
    b = 5
    result = a + b

In this example:
    a and b -> operands
    +       -> operator
    a + b   -> expression

This file contains organized notes and runnable examples for the main
Python operator categories covered in these study notes.
"""


# ------------------------------------------------------------
# 1. Introduction to Operators
# ------------------------------------------------------------

a = 10
b = 5
result = a + b

print(result)
# Output: 15

# a and b are operands; + is the operator.
# The expression a + b is evaluated to produce the result 15.


# ------------------------------------------------------------
# 2. Arithmetic Operators
# ------------------------------------------------------------

# Arithmetic operators perform mathematical operations.
# Common arithmetic operators:
#
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# //  Floor division
# %   Modulus (remainder)
# **  Exponentiation


a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Output:
# Addition: 19
# Subtraction: 11
# Multiplication: 60
# Division: 3.75
# Floor Division: 3
# Modulus: 3
# Exponentiation: 50625


# Important:
# 1. / performs true division and returns a float for built-in numeric
#    operands, even when the division has no fractional part.
# 2. // performs floor division. It rounds the quotient down toward
#    negative infinity; it does not simply remove the decimal part.
# 3. % returns the remainder. Its sign follows the divisor.

print(20 / 4)
# Output: 5.0

print(20 // 4)
# Output: 5

print(15.0 // 4)
# Output: 3.0

# The result type of // depends on the operand types. With integer
# operands, the result is an int; with a float operand, the result is
# a float.

print(-7 // 2)
# Output: -4

print(-7 % 2)
# Output: 1

# Floor division and modulus are related by:
# a == (a // b) * b + (a % b), when b is not zero.

# The + and * operators can also work with sequences such as strings.
# In that context, they perform concatenation and repetition, not
# mathematical addition and multiplication.

word = "Python"
print(word + " Operators")
# Output: Python Operators

print(word * 3)
# Output: PythonPythonPython


# ------------------------------------------------------------
# 3. Comparison (Relational) Operators
# ------------------------------------------------------------

# Comparison operators compare two values.
# For ordinary built-in comparisons, the result is True or False.
#
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to


a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Output:
# False
# True
# False
# True
# False
# True

# Do not confuse = and ==:
# =  assigns a value to a variable.
# == compares two values for equality.


# ------------------------------------------------------------
# 4. Logical Operators
# ------------------------------------------------------------

# Logical operators are commonly used to combine or reverse conditions.
# Python has three logical operators: and, or, and not.
#
# Important: and and or can return one of their operands, not necessarily
# a Boolean value. The not operator always returns True or False.


# 4.1. AND operator
# -----------------

# and returns the first falsy operand if one is found; otherwise, it
# returns the last operand. When used with Boolean values, it is True
# only when both operands are True.
#
# Truth table:
# Expression 1    Expression 2    Result
# True            True            True
# True            False           False
# False           True            False
# False           False           False

age = 20
score = 75

print(age >= 18 and score >= 60)
# Evaluation: True and True
# Output: True

age = 16
score = 80

print(age >= 18 and score >= 60)
# Evaluation: False and True
# Output: False


# 4.2. OR operator
# ----------------

# or returns the first truthy operand if one is found; otherwise, it
# returns the last operand. When used with Boolean values, it is True
# when at least one operand is True.
#
# Truth table:
# Expression 1    Expression 2    Result
# True            True            True
# True            False           True
# False           True            True
# False           False           False

age = 15
has_permission = True

print(age >= 18 or has_permission)
# Evaluation: False or True
# Output: True

age = 15
has_permission = False

print(age >= 18 or has_permission)
# Evaluation: False or False
# Output: False


# 4.3. NOT operator
# ------------------

# not reverses the truth value of an expression:
# not True  -> False
# not False -> True
#
# Truth table:
# Expression    Result
# True          False
# False         True

is_logged_in = False
print(not is_logged_in)
# Output: True

age = 20
print(not (age >= 18))
# Evaluation: not True
# Output: False


# 4.4. Short-circuit evaluation
# -----------------------------

# Short-circuiting means Python may stop evaluating a logical expression
# as soon as its result is determined by the left operand.
#
# With and:
# If the left operand is falsy, Python does not evaluate the right
# operand because the result is already determined.
#
# With or:
# If the left operand is truthy, Python does not evaluate the right
# operand because the result is already determined.

print(False and True)
# Output: False

print(True or False)
# Output: True

# Short-circuiting can avoid unnecessary work and can prevent certain
# errors by avoiding evaluation of an expression that should not run.

# 4.5. Using OR to provide a default value
# ----------------------------------------

# Because or returns an operand, it can be used to provide a default.
# If the first value is truthy, or returns that value.
# If the first value is falsy, or returns the value on the right.

address = "Kabul"
address_result = address or "NA"
print(address_result)
# Output: Kabul

address = ""
address_result = address or "NA"
print(address_result)
# Output: NA

# This works because an empty string is falsy.
# Other common falsy values include:
# False, None, 0, 0.0, "", [], {}, (), and set().

name = "" or "Guest"
print(name)
# Output: Guest

# Common practical use:
# If the user presses Enter without typing a name, input() returns an
# empty string, so the default value "Guest" is selected.
# Uncomment to try it:
# name = input("Enter your name: ") or "Guest"
# print(name)


