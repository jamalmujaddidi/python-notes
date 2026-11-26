# ============================================================
# PYTHON DATA TYPES
# Complete Study Notes and Practical Examples
# ============================================================
#
# Topics:
# 1. Integer and Floating-Point Numbers (int & float)
# 2. Complex Numbers (complex)
# 3. Strings (str)
# 4. String Functions, Operators and Methods
# 5. Lists (list)
# 6. List Operations, Methods and Built-in Functions
# 7. List Indexing, Slicing and Iteration
# 8. Nested Lists and List Comprehension
# 9. Tuples (tuple)
# 10. Tuple Packing, Unpacking and Operations
# 11. Sets (set)
# 12. Set Methods, Operators and Built-in Functions
# 13. Hashing and Hash Collisions
# 14. Frozen Sets (frozenset)
# 15. Dictionaries (dict)
# 16. Dictionary Methods, Operators and Traversal
# 17. Practical Dictionary Programs
# 18. Boolean (bool)
# 19. Truth Value Testing and Boolean Operators
#
# ============================================================

# ---------------------------
# Introduction to Data Types
# ---------------------------

# Data types define the kind of value represented by an object
# and determine the operations that can be performed on it.
#
# Python treats all values as objects, and every object has
# an associated type.
#
# Important distinction:
#
# In this example:
#
# x = 10
#
# int  -> A class representing the integer data type.
# 10   -> An integer object (instance of the int class).
# x    -> A variable name referring to that object.
#
# We can check the type using type().


x = 10

print(type(x))

# Output:
# <class 'int'>


# ---------------------------
# Python Numeric Data Types
# ---------------------------

# Python provides three main built-in numeric types:
#
# 1. Integer (int)
# 2. Floating-Point (float)
# 3. Complex (complex)


# ============================================================
# 1. INTEGER (int)
# ============================================================

# An integer is a numeric data type used to represent
# whole numbers without a decimal or fractional part.
#
# Integers can be:
#
# Positive: 10, 25, 100
# Negative: -5, -20, -100
# Zero:      0
#
# Integers belong to the int class.


# ---------------------------
# Examples of Integers
# ---------------------------

age = 25
temperature = -10
students = 50
balance = 0

print(age)
# Output:
# 25

print(type(age))
# Output:
# <class 'int'>


# Other examples:

print(type(temperature))
# Output:
# <class 'int'>

print(type(students))
# Output:
# <class 'int'>

print(type(balance))
# Output:
# <class 'int'>


# ---------------------------
# Python Integers Have No Fixed Size
# ---------------------------

# Unlike fixed-width integer types commonly found in
# other programming languages, Python integers can grow
# to represent very large values.
#
# Their practical limit is mainly determined by
# the available memory.


x = 999999999999999999999999999999999999

print(x)

# Output:
# 999999999999999999999999999999999999

print(type(x))

# Output:
# <class 'int'>


# ============================================================
# INTEGER LITERALS AND NUMBER SYSTEM PREFIXES
# ============================================================

# Python supports different number systems for integer literals.
#
# The prefixes tell Python how to interpret a number.
#
# 1. Decimal      -> No special prefix
# 2. Binary       -> 0b or 0B
# 3. Octal        -> 0o or 0O
# 4. Hexadecimal  -> 0x or 0X


# ---------------------------
# Decimal (Base 10)
# ---------------------------

# Decimal is the default number system in Python.

decimal_number = 25

print(decimal_number)
# Output:
# 25


# ---------------------------
# Binary (Base 2)
# ---------------------------

# Binary literals use the prefix 0b or 0B.

binary_number = 0b11001

print(binary_number)
# Output:
# 25


# ---------------------------
# Octal (Base 8)
# ---------------------------

# Octal literals use the prefix 0o or 0O.

octal_number = 0o31

print(octal_number)
# Output:
# 25


# ---------------------------
# Hexadecimal (Base 16)
# ---------------------------

# Hexadecimal literals use the prefix 0x or 0X.

hex_number = 0x19

print(hex_number)
# Output:
# 25


# ---------------------------
# Checking Their Types
# ---------------------------

print(type(decimal_number))
# Output:
# <class 'int'>

print(type(binary_number))
# Output:
# <class 'int'>

print(type(octal_number))
# Output:
# <class 'int'>

print(type(hex_number))
# Output:
# <class 'int'>


# Important:
# Although these numbers are written using different
# number systems, Python interprets all of them as int objects.
#
# Decimal:      25
# Binary:       0b11001
# Octal:        0o31
# Hexadecimal:  0x19
#
# All represent the same integer value: 25.


# ============================================================
# UNDERSCORES IN INTEGER LITERALS
# ============================================================

# Python allows underscores inside numeric literals
# to improve readability, especially for large numbers.
#
# Underscores do not change the actual numeric value.


population = 1_000_000

print(population)
# Output:
# 1000000


# This is equivalent to:

population = 1000000

print(population)
# Output:
# 1000000


# Underscores are only for readability.
# They are not part of the actual numeric value.



# ============================================================
# 1. FLOATING-POINT NUMBERS (float)
# ============================================================

# A floating-point number is a numeric value that can contain
# a fractional or decimal part.
#
# Floating-point numbers are represented by the float class.
#
# Examples:
# 10.5
# -3.14
# 0.75
# 0.0


# ---------------------------
# Creating a float
# ---------------------------

x = 10.5

print(x)
# Output:
# 10.5

print(type(x))
# Output:
# <class 'float'>


# ---------------------------
# Scientific Notation
# ---------------------------

# Python allows very large or very small floating-point
# numbers to be represented using scientific notation.
#
# The letter 'e' means:
# "Multiply by 10 raised to the power of."


# Example 1:
x = 1.5e3

print(x)
# Output:
# 1500.0
#
# 1.5e3 = 1.5 x 10^3 = 1500.0


# Example 2:
x = 2.5e-3

print(x)
# Output:
# 0.0025
#
# 2.5e-3 = 2.5 x 10^-3 = 0.0025


# More examples:

print(1e3)       # 1000.0
print(5e2)       # 500.0
print(2.5e2)     # 250.0
print(3e-2)      # 0.03

# Note:
# Numbers written using scientific notation are still floats.



# ============================================================
# 3. COMPLEX NUMBERS (complex)
# ============================================================

# A complex number contains two parts:
#
# 1. Real part
# 2. Imaginary part
#
# Mathematical representation:
#
# a + bj
#
# a = Real part
# b = Imaginary part
# j = Imaginary unit
#
# Note:
# Mathematics commonly uses 'i' for the imaginary unit.
# Python uses 'j'.


# ---------------------------
# Creating Complex Numbers
# ---------------------------

x = 3 + 2j

print(x)
# Output:
# (3+2j)

print(type(x))
# Output:
# <class 'complex'>


# More examples:

print(5 + 3j)
print(-2 + 4j)
print(7 - 2j)
print(3j)
print(-5j)

# These are all complex numbers.