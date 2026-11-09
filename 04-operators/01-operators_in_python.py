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


# ------------------------------------------------------------
# 5. Bitwise Operators
# ------------------------------------------------------------

# Bitwise operators perform operations on the bits of integer operands.
#
# &   Bitwise AND
# |   Bitwise OR
# ^   Bitwise XOR (exclusive OR)
# ~   Bitwise NOT
# <<  Left shift
# >>  Right shift


# 5.1. Binary number system and conversions
# ------------------------------------------

# Binary is a number system that uses only two digits: 0 and 1.
# Decimal is a number system that uses ten digits: 0 through 9.
#
# Decimal to binary example: 13
#
# Divide by 2 and record each remainder:
# 13 / 2 -> quotient 6, remainder 1
#  6 / 2 -> quotient 3, remainder 0
#  3 / 2 -> quotient 1, remainder 1
#  1 / 2 -> quotient 0, remainder 1
#
# Read the remainders from bottom to top: 1101
# Therefore: 13 (decimal) = 1101 (binary)
#
# Another way: use powers of 2 (8, 4, 2, 1).
# 13 = 8 + 4 + 1, so the corresponding bits are 1, 1, 0, 1.
# This also gives 1101 (binary).

number = 13
print(bin(number))
# Output: 0b1101

# The 0b prefix identifies a binary integer representation.

# Binary to decimal example: 1101
#
# From right to left, use powers of 2 starting at 2**0:
# Binary digit:  1    1    0    1
# Power of 2:   2**3 2**2 2**1 2**0
# Value:         8    4    0    1
# Sum: 8 + 4 + 0 + 1 = 13

print(int("0b10011", 2))
# Output: 19

# int(text, 2) converts a binary string to a decimal integer.



# 5.2. Bitwise AND (&)
# --------------------

# Compares corresponding bits:
# 0 & 0 -> 0
# 0 & 1 -> 0
# 1 & 0 -> 0
# 1 & 1 -> 1
# A result bit is 1 only when both corresponding bits are 1.

a = 3
b = 6

print(a & b)
# Binary:
# 3 = 0011
# 6 = 0110
#     ----
#     0010 -> 2
# Output: 2


# 5.3. Bitwise OR (|)
# -------------------

# A result bit is 1 when at least one corresponding bit is 1.
# 0 | 0 -> 0
# 0 | 1 -> 1
# 1 | 0 -> 1
# 1 | 1 -> 1

a = 10
b = 5

print(a | b)
# Binary:
# 10 = 1010
#  5 = 0101
#      ----
#      1111 -> 15
# Output: 15


# 5.4. Bitwise XOR (^)
# --------------------

# XOR produces 1 when the corresponding bits are different.
# 0 ^ 0 -> 0
# 0 ^ 1 -> 1
# 1 ^ 0 -> 1
# 1 ^ 1 -> 0

a = 10
b = 5

print(a ^ b)
# Binary:
# 10 = 1010
#  5 = 0101
#      ----
#      1111 -> 15
# Output: 15



# 5.5. Bitwise left shift (<<)
# ----------------------------

# Shifts the bits of an integer to the left by a specified number
# of positions. For integers, x << n is equivalent to x * (2 ** n)
# when n is non-negative.

a = 5

print(a << 1)
# Binary: 0101 << 1 -> 1010
# Output: 10

print(a << 2)
# Binary: 0101 << 2 -> 10100
# Output: 20

print(a << 3)
# Binary: 0101 << 3 -> 101000
# Output: 40

# Zeros are added on the right as the bits shift left.


# 5.6. Bitwise right shift (>>)
# -----------------------------

# Shifts the bits of an integer to the right by a specified number
# of positions. For integers and non-negative n, x >> n is equivalent
# to floor division by 2 ** n.

a = 20

print(a >> 1)
# Binary: 10100 >> 1 -> 01010
# Output: 10

print(a >> 2)
# Binary: 10100 >> 2 -> 00101
# Output: 5

print(a >> 3)
# Binary: 10100 >> 3 -> 00010
# Output: 2

# Bits shifted out on the right are discarded. For positive integers,
# zeros are added on the left.


# 5.7. Bitwise NOT (~)
# --------------------

# Bitwise NOT inverts the bits of an integer.
# Python integers have arbitrary precision; conceptually, negative
# integers behave as though they have an unlimited sign extension.
# Therefore, do not rely on a fixed 4-bit or 8-bit representation to
# calculate Python's result.
#
# For every integer n:
#     ~n == -(n + 1)

print(~5)
# Evaluation: -(5 + 1) -> -6
# Output: -6

print(~10)
# Output: -11

print(~0)
# Output: -1

# Signed and unsigned integers (general computing concept):
# - A signed integer representation can represent negative values, zero,
#   and positive values.
# - An unsigned integer representation represents zero and positive
#   values only.
# Python's built-in int type does not require a fixed-width signed or
# unsigned declaration; Python integers support arbitrary precision.
#
# The fixed-width one's-complement and two's-complement method is useful
# when studying hardware representations of signed integers. It is not
# necessary to calculate Python's bitwise NOT results because Python's
# integer behavior is described by the formula above.


# ------------------------------------------------------------
# 6. Assignment Operators
# ------------------------------------------------------------

# Assignment is used to bind a name to an object.
# The simple assignment symbol is =.
# Augmented assignment combines an operation with assignment.
#
# Common augmented assignment operators:
# +=   Addition assignment
# -=   Subtraction assignment
# *=   Multiplication assignment
# /=   Division assignment
# //=  Floor division assignment
# %=   Modulus assignment
# **=  Exponentiation assignment
# &=   Bitwise AND assignment
# |=   Bitwise OR assignment
# ^=   Bitwise XOR assignment
# <<=  Left-shift assignment
# >>=  Right-shift assignment


# 6.1. Simple assignment (=)
# --------------------------

x = 10
print(x)
# Output: 10

# The name x is bound to the integer object 10.


# 6.2. Addition assignment (+=)
# -----------------------------

x = 10
x += 5
print(x)
# Equivalent for this integer example: x = x + 5
# Evaluation: 10 + 5 -> 15
# Output: 15


# 6.3. Subtraction assignment (-=)
# --------------------------------

x = 10
x -= 3
print(x)
# Equivalent for this integer example: x = x - 3
# Evaluation: 10 - 3 -> 7
# Output: 7


# 6.4. Multiplication assignment (*=)
# -----------------------------------

x = 10
x *= 4
print(x)
# Equivalent for this integer example: x = x * 4
# Evaluation: 10 * 4 -> 40
# Output: 40


# 6.5. Division assignment (/=)
# -----------------------------

x = 20
x /= 4
print(x)
# Equivalent for this numeric example: x = x / 4
# Evaluation: 20 / 4 -> 5.0
# Output: 5.0


# 6.6. Floor division assignment (//=)
# ------------------------------------

x = 17
x //= 5
print(x)
# Equivalent for this integer example: x = x // 5
# Evaluation: 17 // 5 -> 3
# Output: 3


# 6.7. Modulus assignment (%=)
# ---------------------------

x = 17
x %= 5
print(x)
# Equivalent for this integer example: x = x % 5
# Remainder: 17 % 5 -> 2
# Output: 2


# 6.8. Exponentiation assignment (**=)
# -----------------------------------

x = 2
x **= 4
print(x)
# Equivalent for this integer example: x = x ** 4
# Evaluation: 2 ** 4 -> 16
# Output: 16



# 6.9. Bitwise AND assignment (&=)
# --------------------------------

x = 6
x &= 3
print(x)
# Equivalent for this integer example: x = x & 3
# Binary: 110 & 011 -> 010
# Output: 2


# 6.10. Bitwise OR assignment (|=)
# -------------------------------

x = 6
x |= 3
print(x)
# Equivalent for this integer example: x = x | 3
# Binary: 110 | 011 -> 111
# Output: 7


# 6.11. Bitwise XOR assignment (^=)
# --------------------------------

x = 6
x ^= 3
print(x)
# Equivalent for this integer example: x = x ^ 3
# Binary: 110 ^ 011 -> 101
# Output: 5


# 6.12. Left-shift assignment (<<=)
# --------------------------------

x = 5
x <<= 1
print(x)
# Equivalent for this integer example: x = x << 1
# Binary: 101 << 1 -> 1010
# Output: 10


# 6.13. Right-shift assignment (>>=)
# ---------------------------------

x = 10
x >>= 1
print(x)
# Equivalent for this integer example: x = x >> 1
# Binary: 1010 >> 1 -> 0101
# Output: 5

# Important note about augmented assignment:
# For simple immutable numeric values, x += y behaves like x = x + y.
# For mutable objects, an augmented assignment may update the existing
# object in place when the type supports it. Therefore, augmented
# assignment is not always identical to writing x = x + y.

numbers = [1, 2]
numbers += [3]
print(numbers)
# Output: [1, 2, 3]



# ------------------------------------------------------------
# 7. Membership Operators
# ------------------------------------------------------------

# Membership operators check whether a value is present in a container.
# Python has two membership operators:
# in      -> True if the value is found
# not in  -> True if the value is not found


# 7.1. The in operator
# --------------------

fruits = ["apple", "banana", "orange"]
name = "Python"

print("banana" in fruits)
print("grape" in fruits)
print("th" in name)

# Output:
# True
# False
# True

# "banana" is in the list.
# "grape" is not in the list.
# The substring "th" occurs in the string "Python".


# 7.2. The not in operator
# ------------------------

colors = ["red", "green", "blue"]

print("red" not in colors)
print("yellow" not in colors)

# Output:
# False
# True
