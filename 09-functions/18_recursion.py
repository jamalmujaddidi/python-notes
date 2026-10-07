"""
# ============================================================
# TOPIC 18 — RECURSION
# ============================================================

18.0 Overview of Recursion
18.1 Introduction to Recursion
18.2 Base Case and Recursive Case
18.3 How Recursive Function Calls Work
18.4 Basic Recursion Examples
18.5 Recursion with Parameters and Return Values
18.6 Recursion with Strings and Sequences
18.7 Recursion vs Iteration
18.8 Practical Examples
18.9 Recursion Limit and RecursionError
18.10 Practical Exercises
18.11 Summary
"""


# ============================================================
# 18.0 OVERVIEW OF RECURSION
# ============================================================

"""
Recursion is a programming technique in which a function
calls itself to solve a problem.

A recursive function usually breaks a larger problem into
smaller versions of the same problem.

A correct recursive function needs:
- A base case
- A recursive case
- Progress toward the base case

Important concepts:
- Recursive functions
- Base case and recursive case
- Call stack and stack frames
- Arguments and return values
- Strings and sequences
- Recursion vs iteration
- Practical recursive problems
- Recursion limit and RecursionError
"""


# ============================================================
# 18.1 INTRODUCTION TO RECURSION
# ============================================================

"""
A recursive function is a function that calls itself during
its execution.

The recursive calls continue until a stopping condition
(the base case) is reached.

Basic structure:

def recursive_function(parameter):

    if base_case:
        return result

    return recursive_function(modified_parameter)
"""


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


# ============================================================
# 18.2 BASE CASE AND RECURSIVE CASE
# ============================================================

"""
Base case:
The condition that tells the recursive function to stop.

Recursive case:
The part of the function where it calls itself.

Each recursive call should move the problem closer to the
base case.

Example:
5 -> 4 -> 3 -> 2 -> 1 -> 0

Without a proper base case, or if calls move away from the
base case, recursion can continue until RecursionError.
"""


# ============================================================
# 18.3 HOW RECURSIVE FUNCTION CALLS WORK
# ============================================================

"""
Python uses a call stack to keep track of active function
calls.

Each active function call has its own stack frame.

The call stack follows LIFO (Last In, First Out).

Example:

def count_down(number):

    if number == 0:
        return

    count_down(number - 1)
    print(number)

count_down(4)

Calls go down:
count_down(4)
count_down(3)
count_down(2)
count_down(1)
count_down(0)

The base case is reached at count_down(0).

Calls then complete in reverse order, so the output is:

# 1
# 2
# 3
# 4

If print() is before the recursive call, output occurs while
going down instead.

Important mental model:
- Going down: new calls are added to the call stack.
- Base case: recursion stops going deeper.
- Coming back up: deeper calls return and previous calls resume.
"""


# ============================================================
# 18.4 BASIC RECURSION EXAMPLES
# ============================================================

def basic_countdown(number):

    if number == 0:
        return

    print(number)
    basic_countdown(number - 1)


basic_countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1


def basic_countup(number):

    if number == 0:
        return

    basic_countup(number - 1)
    print(number)


basic_countup(5)

# Output:
# 1
# 2
# 3
# 4
# 5


def basic_sum_numbers(number):

    if number == 1:
        return 1

    return number + basic_sum_numbers(number - 1)


result = basic_sum_numbers(5)
print("Sum:", result)

# Output:
# Sum: 15


def basic_factorial(number):

    if number == 1:
        return 1

    return number * basic_factorial(number - 1)


result = basic_factorial(5)
print("Factorial:", result)

# Output:
# Factorial: 120


# ============================================================
# 18.5 RECURSION WITH PARAMETERS AND RETURN VALUES
# ============================================================

"""
In each recursive call, the function's parameter can receive
a new argument.

The new argument should move the problem closer to the base
case.

Example:
5 -> 4 -> 3 -> 2 -> 1

The base case returns a value, and that value travels back
through the previous calls.

For sum_numbers(5):

sum_numbers(1) -> 1
sum_numbers(2) -> 3
sum_numbers(3) -> 6
sum_numbers(4) -> 10
sum_numbers(5) -> 15

Core idea:
Parameter -> controls recursive progression.
Return value -> carries the calculated result back.
"""


def parameter_sum(number):

    if number == 1:
        return 1

    return number + parameter_sum(number - 1)


result = parameter_sum(5)
print("Parameter/return example:", result)

# Output:
# Parameter/return example: 15


# ============================================================
# 18.6 RECURSION WITH STRINGS AND SEQUENCES
# ============================================================

# 18.6.1 — Strings

def print_characters(text):

    if text == "":
        return

    print(text[0])
    print_characters(text[1:])


print_characters("Python")

# Output:
# P
# y
# t
# h
# o
# n

# text[0] -> first character
# text[1:] -> remaining string


# 18.6.2 — Lists

def print_items(items):

    if items == []:
        return

    print(items[0])
    print_items(items[1:])


print_items(["Apple", "Banana", "Orange", "Mango"])

# Output:
# Apple
# Banana
# Orange
# Mango

# items[0] -> first element
# items[1:] -> remaining list


"""
Common base cases:

String:
if text == "":
    return

List:
if items == []:
    return

The sequence becomes smaller until the empty sequence is
reached.

Recursive case:
1. Process the current element.
2. Reduce the sequence.
3. Call the function again with the smaller sequence.

Recursion can also return results by combining the current
value with the value returned by the recursive call.
"""


# ============================================================
# 18.7 RECURSION VS ITERATION
# ============================================================

"""
Iteration uses loops such as for and while.

Recursion uses function calls.

Iteration -> repetition through loops
Recursion  -> repetition through function calls

Iteration is often simpler for straightforward repetition.

Recursion can be natural for problems that are defined in
terms of smaller versions of themselves or hierarchical data.

Recursion uses the call stack, so deep recursion can use more
memory and can reach Python's recursion limit.
"""


def iterative_sum(number):

    total = 0

    for value in range(1, number + 1):
        total += value

    return total


result = iterative_sum(5)
print("Iterative result:", result)

# Output:
# Iterative result: 15


def recursive_sum(number):

    if number == 1:
        return 1

    return number + recursive_sum(number - 1)


result = recursive_sum(5)
print("Recursive result:", result)

# Output:
# Recursive result: 15


# ============================================================
# 18.8 PRACTICAL EXAMPLES
# ============================================================

# 18.8.1 — Factorial

def practical_factorial(number):

    if number == 1:
        return 1

    return number * practical_factorial(number - 1)


result = practical_factorial(5)
print("Practical factorial:", result)

# Output:
# Practical factorial: 120


# 18.8.2 — Fibonacci

def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


result = fibonacci(6)
print("Fibonacci:", result)

# Output:
# Fibonacci: 8


"""
Fibonacci uses two recursive calls.

F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2)
"""


# 18.8.3 — Sum of a List

def list_sum(numbers):

    if numbers == []:
        return 0

    return numbers[0] + list_sum(numbers[1:])


result = list_sum([10, 20, 30, 40])
print("List sum:", result)

# Output:
# List sum: 100


# 18.8.4 — Reverse a String

def reverse_string(text):

    if text == "":
        return ""

    return reverse_string(text[1:]) + text[0]


result = reverse_string("Python")
print("Reversed:", result)

# Output:
# Reversed: nohtyP


# 18.8.5 — Nested Structures

def print_nested(items):

    for item in items:

        if isinstance(item, list):
            print_nested(item)
        else:
            print(item)


nested_data = [
    "Apple",
    ["Banana", "Orange"],
    ["Mango", ["Grapes", "Peach"]]
]

print_nested(nested_data)

# Output:
# Apple
# Banana
# Orange
# Mango
# Grapes
# Peach


# Additional nested example: Sum of a Nested List

def nested_sum(items):

    total = 0

    for item in items:

        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item

    return total


result = nested_sum([1, [2, 3], [4, [5, 6]]])
print("Nested list sum:", result)

# Output:
# Nested list sum: 21


# ============================================================
# 18.9 RECURSION LIMIT AND RECURSIONERROR
# ============================================================

"""
Python limits how deeply Python-level function calls can
recurse.

The current recursion limit can be checked with:

import sys
print(sys.getrecursionlimit())

The exact limit is implementation/configuration dependent.

Every active function call requires a stack frame. If
recursive calls continue indefinitely, the call stack can
grow excessively.

Incorrect example:

def infinite_recursion(number):
    print(number)
    infinite_recursion(number + 1)

Do not call the function above. It will eventually raise
RecursionError because it does not terminate.

A base case alone is not enough. The recursive argument must
also move toward the base case.

Correct:
5 -> 4 -> 3 -> 2 -> 1 -> 0

Incorrect:
5 -> 6 -> 7 -> 8 -> ...

sys.setrecursionlimit() can change the recursion limit, but
increasing it is not normally the solution to incorrect or
unnecessarily deep recursion.
"""


# ============================================================
# 18.10 PRACTICAL EXERCISES
# ============================================================

# Exercise 1 — Countdown

def exercise_countdown(number):

    if number == 0:
        return

    print(number)
    exercise_countdown(number - 1)


exercise_countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1


# Exercise 2 — Count Up

def exercise_countup(number):

    if number == 0:
        return

    exercise_countup(number - 1)
    print(number)


exercise_countup(5)

# Output:
# 1
# 2
# 3
# 4
# 5


# Exercise 3 — Sum of Numbers

def exercise_sum_numbers(number):

    if number == 1:
        return 1

    return number + exercise_sum_numbers(number - 1)


result = exercise_sum_numbers(5)
print("Exercise 3:", result)

# Output:
# Exercise 3: 15


# Exercise 4 — Factorial

def exercise_factorial(number):

    if number == 1:
        return 1

    return number * exercise_factorial(number - 1)


result = exercise_factorial(5)
print("Exercise 4:", result)

# Output:
# Exercise 4: 120


# Exercise 5 — Sum of a List

def exercise_list_sum(numbers):

    if numbers == []:
        return 0

    return numbers[0] + exercise_list_sum(numbers[1:])


result = exercise_list_sum([10, 20, 30, 40])
print("Exercise 5:", result)

# Output:
# Exercise 5: 100


# Exercise 6 — Print Characters

def exercise_print_characters(text):

    if text == "":
        return

    print(text[0])
    exercise_print_characters(text[1:])


exercise_print_characters("Python")

# Output:
# P
# y
# t
# h
# o
# n


# Exercise 7 — Fibonacci

def exercise_fibonacci(number):

    if number <= 1:
        return number

    return exercise_fibonacci(number - 1) + exercise_fibonacci(number - 2)


result = exercise_fibonacci(6)
print("Exercise 7:", result)

# Output:
# Exercise 7: 8


# Exercise 8 — Find Maximum in a List

def find_max(numbers):

    if len(numbers) == 1:
        return numbers[0]

    maximum = find_max(numbers[1:])

    if numbers[0] > maximum:
        return numbers[0]

    return maximum


result = find_max([10, 25, 7, 42, 18])
print("Exercise 8:", result)

# Output:
# Exercise 8: 42


# Exercise 9 — Nested List Sum

def exercise_nested_sum(items):

    total = 0

    for item in items:

        if isinstance(item, list):
            total += exercise_nested_sum(item)
        else:
            total += item

    return total


result = exercise_nested_sum([1, [2, 3], [4, [5, 6]]])
print("Exercise 9:", result)

# Output:
# Exercise 9: 21


# Exercise 10 — Fibonacci

def exercise_fibonacci_final(number):

    if number <= 1:
        return number

    return exercise_fibonacci_final(number - 1) + exercise_fibonacci_final(number - 2)


result = exercise_fibonacci_final(6)
print("Exercise 10:", result)

# Output:
# Exercise 10: 8



# Example 11
# Find the smallest number in a list using recursion

def find_min(numbers):
    if len(numbers) == 1:
        return numbers[0]

    minimum = find_min(numbers[1:])

    if numbers[0] < minimum:
        return numbers[0]

    return minimum


numbers = [10, 25, 7, 42, 18]

result = find_min(numbers)

print(result)

# Output:
# 7


# ============================================================
# 18.11 SUMMARY
# ============================================================

"""
Recursion is a programming technique in which a function
calls itself to solve a problem.

A recursive function usually works on a smaller or simpler
version of the same problem.

Key concepts:

1. Base Case
The condition that stops recursion.

2. Recursive Case
The part of the function that makes the recursive call.

3. Progress Toward the Base Case
Each recursive call should move the problem closer to the
base case.

4. Parameters
Each recursive call can receive a new argument.

5. Return Values
A recursive call can return a value to the function call
that invoked it.

6. Call Stack
Python uses a call stack to keep track of active calls.

7. Stack Frames
Each active function call has its own stack frame.

8. LIFO
The call stack follows Last In, First Out.

9. Strings and Sequences
Strings and lists can be processed recursively by reducing
the sequence.

String:
text[1:]

List:
items[1:]

10. Recursion vs Iteration
Recursion uses function calls.
Iteration uses loops.

11. Practical Uses
- Factorial
- Fibonacci
- List processing
- String processing
- Nested structures
- Hierarchical data

12. Recursion Limit and RecursionError
Python limits recursion depth. Excessive or non-terminating
recursion can raise RecursionError.

Final mental model:

Recursive function
        ↓
Check base case
        ↓
If not reached
        ↓
Make the problem smaller
        ↓
Recursive call
        ↓
Repeat
        ↓
Base case reached
        ↓
Return value
        ↓
Previous calls resume
        ↓
Final result

Most important rule:

A correct recursive function needs a base case and must make
progress toward that base case.
"""


# ============================================================
# END OF TOPIC 18 — RECURSION
# ============================================================
