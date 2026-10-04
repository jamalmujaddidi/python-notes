"""
# ============================================================
# TOPIC 18 — RECURSION
# ============================================================

18.0 Overview of Recursion
18.1 Introduction to Recursion
"""


# ============================================================
# 18.0 OVERVIEW OF RECURSION
# ============================================================

"""
Recursion is a programming technique in which a function
calls itself to solve a problem.

A recursive function usually breaks a larger problem into
smaller versions of the same problem.

A recursive function needs a condition that eventually stops
the recursive calls.

Important concepts we will study in Topic 18:

- Recursive functions
- Base case
- Recursive case
- Function call stack
- Recursive function arguments
- Return values
- Recursion with strings and sequences
- Recursion vs iteration
- Recursion limit
- RecursionError
- Practical recursive problems
"""


# ============================================================
# 18.1 INTRODUCTION TO RECURSION
# ============================================================

"""
Definition:

Recursion is a technique where a function calls itself
repeatedly during its execution.

A function that calls itself is called a recursive function.

A recursive function continues calling itself with a smaller
or simpler version of the problem until a stopping condition
is reached.
"""


# ------------------------------------------------------------
# Example 1: Simple Recursive Countdown
# ------------------------------------------------------------

def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)


countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1


# Explanation:
#
# countdown() is a recursive function because it calls itself:
#
# countdown(number - 1)
#
# Each recursive call receives a smaller number.
#
# When number becomes 0, the function stops making
# additional recursive calls.
#
#another example

def factorial(number):

    if number == 1:
        return 1

    return number * factorial(number - 1)


result = factorial(5)

print("Factorial:", result)


#output
# Factorial: 120

# Example

def sum_numbers(number):

    if number == 1:
        return 1

    return number + sum_numbers(number - 1)


result = sum_numbers(5)

print("Result:", result)

# output
# Result: 15


# Example of recursive function with string

def print_characters (text):

    if text == "":
        return

    print(text[0])

    print_characters(text[1:])

print_characters("Python")