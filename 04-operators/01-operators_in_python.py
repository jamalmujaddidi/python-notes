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

