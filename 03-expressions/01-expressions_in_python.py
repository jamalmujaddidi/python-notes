"""
TOPIC: EXPRESSIONS IN PYTHON
===========================

An expression is a piece of Python code that Python evaluates to produce
an object/value. Expressions can contain literals, names, operators,
function calls, and other expressions.

The headings in these notes (such as integral and floating-point
expressions) are learning categories based on the result or operation.
They are not an official exhaustive list of Python expression types.
"""


# ------------------------------------------------------------
# 1. Introduction to Expressions
# ------------------------------------------------------------

x = 10
print(x + 3)
# Output: 13

# x + 3 is an expression because Python evaluates it to the value 13.
# Important: print("x + 3") prints the text x + 3; it does not evaluate
# the expression because the content is inside quotation marks.


# ------------------------------------------------------------
# 2. Components of an Expression
# ------------------------------------------------------------

a = 10
b = 5

print((a + b) * 2)
# Output: 30

# Expression: (a + b) * 2
# Components:
#   a, b     -> names referring to objects
#   10, 5, 2 -> integer values
#   +, *     -> operators
#   ()       -> parentheses used to group an expression
# Evaluation:
#   (10 + 5) * 2
#   15 * 2
#   30

# Expressions can produce values of many types, including int, float,
# bool, str, lists, tuples, and other Python objects.


# ------------------------------------------------------------
# 3. Constant Expressions (Learning Category)
# ------------------------------------------------------------

# A constant expression uses literal values and operators without
# referring to variables. "Constant expression" is a useful learning
# label, not a separate official expression category in Python syntax.

print(10 + 30)
# Output: 40

print((5 + 3) * 2)
# Output: 16


# ------------------------------------------------------------
# 4. Arithmetic Expressions
# ------------------------------------------------------------

# Arithmetic expressions perform arithmetic operations. Common
# arithmetic operators are +, -, *, /, //, %, and **.

a = 10
b = 5

print(a + b)   # Addition:       15
print(a - b)   # Subtraction:     5
print(a * b)   # Multiplication: 50
print(a / b)   # Division:        2.0
print(a // 3)  # Floor division:  3
print(a % 3)   # Remainder:       1
print(a ** 2)  # Exponentiation: 100

# Output:
# 15
# 5
# 50
# 2.0
# 3
# 1
# 100

# The result type depends on the operation and operand types.
# For example, / produces a float for ordinary numeric operands.

# The + and * operators also have meanings for strings. These are
# sequence operations rather than mathematical arithmetic.
word = "Python"
print(word + " notes")
# Output: Python notes

print(word * 3)
# Output: PythonPythonPython

# Parentheses can change the order of evaluation.
a = 10
b = 5
c = 2
print((a + b) * c)
# Output: 30

