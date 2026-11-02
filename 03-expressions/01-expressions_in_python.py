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


# ------------------------------------------------------------
# 5. Expressions Producing Integer Results
# ------------------------------------------------------------

# These examples are expressions whose results are integers.
# Whether an expression returns int depends on the operator and operands.

x = 5
y = 7.5
print(x + int(y))
# Evaluation: 5 + int(7.5) -> 5 + 7 -> 12
# Output: 12

# int() truncates the fractional part toward zero; it does not round.
print(int(7.9))
# Output: 7

print(int(-7.9))
# Output: -7

text_number = "10"
multiplier = 2
print(int(text_number) * multiplier)
# Evaluation: int("10") * 2 -> 10 * 2 -> 20
# Output: 20

print(15 * 5)
# Output: 75

# Note: Not every expression made from integers returns an int.
print(5 / 2)
# Output: 2.5


# ------------------------------------------------------------
# 6. Floating-Point Arithmetic Expressions
# ------------------------------------------------------------

# An arithmetic expression involving float values often produces a
# float result. For built-in numeric arithmetic, int operands are
# converted to a compatible numeric type when needed.

x = 5
y = 7.5
print(x + y)
# Evaluation: 5 + 7.5 -> 12.5
# Output: 12.5

text_number = "10"
multiplier = 2.0
print(float(text_number) * multiplier)
# Evaluation: float("10") * 2.0 -> 10.0 * 2.0 -> 20.0
# Output: 20.0

price = 15.75
tax = 4
total = price + tax
print(total)
# Evaluation: 15.75 + 4 -> 19.75
# Output: 19.75

# A floating-point arithmetic expression is not guaranteed to be the
# result of every expression containing a float: for example, 5.0 > 3
# produces the Boolean value True.
print(5.0 > 3)
# Output: True

# ------------------------------------------------------------
# 7. Comparison Expressions (Relational Expressions)
# ------------------------------------------------------------

# Comparison operators compare values. For ordinary built-in values,
# the result is a Boolean: True or False.
# Operators: ==, !=, <, <=, >, >=

x = 10 + 23
y = 20 - 5
z = x >= y
print(z)
# Evaluation: 33 >= 15 -> True
# Output: True

print(10 == 10)
# Output: True

print(10 != 5)
# Output: True

print(16 < 18)
# Output: True

print(20 <= 20)
# Output: True

print(9 > 12)
# Output: False

print(8 >= 10)
# Output: False

# Python also supports membership comparisons such as in and not in.
print("py" in "python")
# Output: True

# Identity comparisons use is and is not. They test object identity,
# not value equality. Use == to compare values in ordinary cases.
value = None
print(value is None)
# Output: True



# ------------------------------------------------------------
# 8. Logical Expressions and Boolean Operations
# ------------------------------------------------------------

# Logical operators: and, or, not
# These operators are often used to combine or negate conditions.

age = 20
has_id = False
result = (age >= 18) and has_id
print(result)
# Output: False

temperature = 35
is_raining = False
result = temperature > 30 or is_raining
print(result)
# Output: True

is_logged_in = False
print(not is_logged_in)
# Output: True

marks = 85
attendance = 90
eligible = marks >= 80 and attendance >= 75
print(eligible)
# Output: True

# Precedence: not is evaluated before and; and before or.
a = 10
b = 5
c = 8
result = (a > b) and (c < a) or (b == 0)
print(result)
# Evaluation: True and True or False -> True or False -> True
# Output: True

# IMPORTANT: and and or do not necessarily return True or False.
# They return one of their operands. not always returns a Boolean.
print("hello" and "world")
# Output: world

print("" or "default")
# Output: default

print(not "hello")
# Output: False

# and/or use short-circuit evaluation: Python may not evaluate the
# right-hand operand if the left-hand operand determines the result.

# ------------------------------------------------------------
# 9. Bitwise Expressions
# ------------------------------------------------------------

# For built-in integer operands, bitwise operators perform operations
# on integer bits. Bitwise operators are not arithmetic operators for
# float values. User-defined classes can customize operator behavior.
#
# &  Bitwise AND       |  Bitwise OR
# ^  Bitwise XOR       ~  Bitwise NOT
# << Left shift        >> Right shift

# Example 1: Bitwise AND
print(5 & 3)
# Binary illustration: 101 & 011 -> 001
# Output: 1

# Example 2: Bitwise OR
print(5 | 3)
# Binary illustration: 101 | 011 -> 111
# Output: 7

# Example 3: Bitwise XOR (exclusive OR)
print(5 ^ 3)
# Binary illustration: 101 ^ 011 -> 110
# Output: 6

# Example 4: Left shift
print(5 << 1)
# Binary illustration: 101 shifted left by one position -> 1010
# Output: 10

# Example 5: Right shift
print(8 >> 2)
# Binary illustration: 1000 shifted right by two positions -> 10
# Output: 2

# Example 6: Bitwise NOT
print(~5)
# Output: -6

# For any integer x, Python's bitwise NOT follows this identity:
#     ~x == -(x + 1)
print(~10)
# Output: -11

print(~0)
# Output: -1

# The bit patterns above are illustrations. Python integers are not
# restricted to a fixed number of bits; ~x is best understood using
# the identity ~x == -(x + 1), rather than a fixed 8-bit diagram.


# ------------------------------------------------------------
# 10. Combined (Mixed) Expressions
# ------------------------------------------------------------

# A combined expression uses multiple operators or kinds of
# expressions together. "Combinational expression" is not a special
# formal Python syntax category; "mixed expression" is clearer wording.

price = 100
discount = 0.10
final_price = price * (1 - discount)

print(final_price)
# Output: 90.0

is_discounted = final_price < price and price > 0
print(is_discounted)
# Output: True

# Evaluation of final_price:
# 100 * (1 - 0.10) -> 100 * 0.90 -> 90.0

# ------------------------------------------------------------
# 11. Conditional Expressions
# ------------------------------------------------------------

# A conditional expression selects one of two expressions.
# Syntax: value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
# Output: Adult


# example
age = 17
permission = "Allow" if age >= 18 else "Not Allowed "
print (permission)

# Output: Not Allowed


# ------------------------------------------------------------
# 12. Assignment Expressions (Walrus Operator :=)
# ------------------------------------------------------------

# An assignment expression assigns a value to a name and also yields
# that value as part of a larger expression. It was introduced in 3.8.
# The ordinary assignment statement (=) is not the same as :=.

if (length := len("Python")) > 3:
    print(length)
# Output: 6



if (length := len ("program")) > 3:
    print(length)

# Output: 7


# ------------------------------------------------------------
# 13. Operator Precedence
# ------------------------------------------------------------

# Operator precedence determines how an expression is grouped.
# Higher-precedence operators bind more tightly than lower-precedence
# operators. Parentheses can make grouping explicit.

print(5 + 2 * 3)
# Evaluation: 5 + (2 * 3) -> 5 + 6 -> 11
# Output: 11

print((5 + 2) * 3)
# Evaluation: 7 * 3 -> 21
# Output: 21

# Exponentiation groups from right to left.
print(2 ** 3 ** 2)
# Evaluation: 2 ** (3 ** 2) -> 2 ** 9 -> 512
# Output: 512

# Exponentiation has a special interaction with a unary operator
# on its right-hand side.
print(-3 ** 2)
# Evaluation: -(3 ** 2) -> -9
# Output: -9

print(2 ** -1)
# Output: 0.5

# Subtraction groups from left to right.
print(10 - 3 - 2)
# Evaluation: (10 - 3) - 2 -> 7 - 2 -> 5
# Output: 5

# Simplified precedence order, from highest to lowest:
# 1. Grouping / displays: (...), [...], {...}
# 2. Subscription, slicing, calls, attribute access: x[i], f(), x.name
# 3. await x
# 4. Exponentiation: **
# 5. Unary +, -, ~
# 6. *, @, /, //, %
# 7. +, -
# 8. <<, >>
# 9. &
# 10. ^
# 11. |
# 12. Comparisons, membership and identity tests:
#     <, <=, >, >=, ==, !=, in, not in, is, is not
# 13. not
# 14. and
# 15. or
# 16. Conditional expression: x if condition else y
# 17. lambda expression
# 18. Assignment expression: :=
#
# Ordinary assignment (=) and augmented assignment (+=, -=, etc.) are
# statements, not entries in the expression operator-precedence table.
# Exponentiation and conditional expressions group from right to left;
# most binary operators group from left to right.


# ------------------------------------------------------------
# 14. Operators and Expressions: Summary
# ------------------------------------------------------------

# Arithmetic operators       -> arithmetic expressions: a + b
# Comparison operators       -> comparison expressions: a > b
# Logical operators          -> logical expressions: a > b and c < d
# Bitwise operators          -> bitwise expressions: a & b
# Conditional expression     -> result if condition else alternative
# Assignment expression      -> name := expression
#
# Remember:
# - An expression evaluates to a value (or raises an exception).
# - An expression's result type depends on the operation and operands.
# - Parentheses can clarify or change the grouping of an expression.
# - Operator precedence and associativity determine grouping when
#   parentheses are not used.
# - and/or may return operands, not just Boolean values.
# - = is used in assignment statements; := is an assignment expression.