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