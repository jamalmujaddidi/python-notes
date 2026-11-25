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