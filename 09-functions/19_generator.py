"""
===========================================================
19. GENERATORS AND yield
===========================================================

A generator is a special kind of iterator that produces
values one at a time, on demand, using yield.

Topics covered:
19.0  Overview of Generators
19.1  Generator Functions, yield, and Generator Objects
19.2  Generator Execution with next()
19.3  yield vs return
19.4  Generator State and Lazy Evaluation
19.5  Generators with Loops
19.6  Generator Expressions
19.7  Practical Examples
19.8  Practical Exercises
19.9  Summary
"""


# ===========================================================
# 19.0 OVERVIEW OF GENERATORS
# ===========================================================

"""
A generator is a special kind of iterator that produces
values one at a time, on demand, using yield.

Important terms:

- Generator function
- Generator object
- yield
- next()
- Generator state
- Lazy evaluation

Generators are useful when:

- We have many values to produce.
- We do not want to store all values in memory at once.
- Values can be produced when they are needed.
- We are processing large or potentially infinite sequences.
"""


# ===========================================================
# 19.1 GENERATOR FUNCTIONS, yield, AND GENERATOR OBJECTS
# ===========================================================

"""
A generator function is a function that contains the yield
keyword.

When a generator function is called, it returns a generator
object instead of immediately executing the function body.

A generator object is an iterator created when a generator
function is called.

The generator object manages the execution of the generator
function, preserves its current execution state, and produces
values one at a time when requested.

Important relationship:

    Generator function
          |
          | calling the function
          v
    Generator object
          |
          | next()
          v
    yield produces a value


yield:
- Produces a value.
- Pauses execution.
- Preserves the current execution state.
- Allows execution to resume later.
- Can produce multiple values.
"""


# Example: Basic generator function

def numbers():
    yield 1
    yield 2
    yield 3


generator = numbers()

print(generator)

# Output:
# <generator object numbers at 0x...>


# Important:
# numbers      -> generator function
# numbers()    -> generator object
# generator    -> reference to the generator object


# ===========================================================
# 19.2 GENERATOR EXECUTION WITH next()
# ===========================================================

"""
The next() function requests the next value from a generator.

When next() is called:

1. The generator starts or resumes execution.
2. It continues until it reaches yield.
3. yield produces a value.
4. The generator pauses.
5. The produced value is returned by next().

When the generator reaches the end of the function, it becomes
exhausted. A further next() call raises StopIteration.
"""


def number_sequence():
    yield 10
    yield 20
    yield 30


generator = number_sequence()

print(next(generator))
# Output:
# 10

print(next(generator))
# Output:
# 20

print(next(generator))
# Output:
# 30


# The generator is now exhausted.
#
# Calling:
# next(generator)
#
# again would raise:
#
# StopIteration



# ===========================================================
# 19.3 yield vs return
# ===========================================================

"""
yield:
- Produces a value.
- Pauses the generator.
- Preserves execution state.
- Allows the function to resume.
- Can produce multiple values.

return:
- Returns a value.
- Terminates the function.
- Does not allow the function to resume.

A generator function can contain both yield and return.

In a generator, return terminates the generator.

A return statement does not produce another normal yielded
value. After the generator terminates, further next() calls
raise StopIteration.
"""


def values():
    yield 10
    yield 20
    return


generator = values()

print(next(generator))
# Output:
# 10

print(next(generator))
# Output:
# 20

# The return statement now terminates the generator.


"""
Main difference:

    yield  -> produce + pause
    return -> terminate

Once a generator is exhausted:

    next(generator)

raises:

    StopIteration
"""


# ===========================================================
# 19.4 GENERATOR STATE AND LAZY EVALUATION
# ===========================================================

"""
A generator preserves its execution state when it pauses at
yield.

The preserved state includes information such as:

- Current execution position
- Local variable values
- Information required to resume execution

This allows the generator to continue exactly where it
previously paused.
"""


# Example: Preserved local variable state

def counter():
    count = 1

    yield count

    count += 1
    yield count

    count += 1
    yield count


generator = counter()

print(next(generator))
# Output:
# 1

print(next(generator))
# Output:
# 2

print(next(generator))
# Output:
# 3


"""
The generator does not restart from the beginning.

After yielding 1:

    count = 1

When execution resumes:

    count += 1

so:

    count = 2

Then it yields 2.

The state is preserved between yield points.
"""


# -----------------------------------------------------------
# Lazy evaluation
# -----------------------------------------------------------

"""
Generators use lazy evaluation.

Lazy evaluation means that a value is not produced until it
is actually requested.
"""


def lazy_numbers():
    print("Producing 1")
    yield 1

    print("Producing 2")
    yield 2


generator = lazy_numbers()

# Creating the generator does not execute the body.

print(next(generator))
# Output:
# Producing 1
# 1

print(next(generator))
# Output:
# Producing 2
# 2


"""
The important point:

This on-demand behavior can reduce memory usage when working
with large sequences.
"""


# ===========================================================
# 19.5 GENERATORS WITH LOOPS
# ===========================================================

"""
A generator object is an iterator, so it can be used directly
with a for loop.

A for loop automatically requests values from the generator
until the generator is exhausted.

Conceptually:

    next(generator)
    next(generator)
    next(generator)
    ...

When the generator raises StopIteration, the for loop
automatically stops.
"""


# Example: Generator with for loop

def numbers_for_loop():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for number in numbers_for_loop():
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5


# -----------------------------------------------------------
# Generator object can be stored first
# -----------------------------------------------------------

generator = numbers_for_loop()

for number in generator:
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5


"""
A generator is exhaustible.

After the generator has been completely consumed, another
for loop will not produce values from the same generator.
"""


# -----------------------------------------------------------
# Example: Squares generator
# -----------------------------------------------------------

def squares(numbers):
    for number in numbers:
        yield number ** 2


for square in squares([1, 2, 3, 4, 5]):
    print(square)

# Output:
# 1
# 4
# 9
# 16
# 25


# -----------------------------------------------------------
# Example: Even numbers generator
# -----------------------------------------------------------

def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


for number in even_numbers(range(1, 11)):
    print(number)

# Output:
# 2
# 4
# 6
# 8
# 10



# -----------------------------------------------------------
# Manual while loop with next()
# -----------------------------------------------------------

"""
A while loop does not automatically call next().

When using a while loop, we can manually request each value
using next().

Because next() raises StopIteration when the generator is
exhausted, we handle it using try/except.
"""


def while_numbers():
    yield 10
    yield 20
    yield 30


generator = while_numbers()

while True:
    try:
        number = next(generator)
        print(number)
    except StopIteration:
        break

# Output:
# 10
# 20
# 30


"""
The pattern is:

    while True:
        try:
            value = next(generator)
            process(value)
        except StopIteration:
            break

This is the manual way of consuming a generator.
"""


# -----------------------------------------------------------
# While loop with filtered generator
# -----------------------------------------------------------

def even_numbers_for_while(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


generator = even_numbers_for_while(range(1, 11))

while True:
    try:
        number = next(generator)
        print(number)
    except StopIteration:
        break

# Output:
# 2
# 4
# 6
# 8
# 10


# -----------------------------------------------------------
# While loop: odd numbers
# -----------------------------------------------------------

def odd_numbers(numbers):
    for number in numbers:
        if number % 2 != 0:
            yield number


generator = odd_numbers(range(1, 11))

while True:
    try:
        number = next(generator)
        print(number)
    except StopIteration:
        break

# Output:
# 1
# 3
# 5
# 7
# 9


# -----------------------------------------------------------
# While loop: numbers greater than 50
# -----------------------------------------------------------

def numbers_greater_than_50_while(numbers):
    for number in numbers:
        if number > 50:
            yield number


generator = numbers_greater_than_50_while(range(45, 56))

while True:
    try:
        number = next(generator)
        print(number)
    except StopIteration:
        break

# Output:
# 51
# 52
# 53
# 54
# 55


# -----------------------------------------------------------
# Manual next() followed by automatic list() consumption
# -----------------------------------------------------------

"""
A generator can be consumed manually with next() and can also
be consumed automatically by other operations such as list().

The generator remembers its current position.
"""


def creator():
    i = 1

    while i <= 200:
        yield i
        i += 1


x = creator()

print(next(x))
# Output:
# 1

print(next(x))
# Output:
# 2

print(next(x))
# Output:
# 3

print(next(x))
# Output:
# 4


"""
The first four values have now been consumed.

The generator's current position is 5.
"""


print(list(x))

# Output begins:
# [5, 6, 7, 8, 9, 10, 11, ... 200]


"""
list(x) automatically consumes the remaining generator values.

Conceptually, it keeps requesting:

    next(x)
    next(x)
    next(x)
    ...

until:

    StopIteration

The important point is that list(x) starts from 5 because
1, 2, 3, and 4 were already consumed manually.

list() is a Python built-in that creates a list from an
iterable. It is not a method of a for loop or a generator.
"""


# ===========================================================
# 19.6 GENERATOR EXPRESSIONS
# ===========================================================

"""
A generator expression is a compact way to create a generator
without defining a separate generator function using def and
yield.

Basic syntax:

    (expression for item in iterable)

With a condition:

    (expression for item in iterable if condition)
"""


# -----------------------------------------------------------
# Example: Basic generator expression
# -----------------------------------------------------------

squares_expression = (number ** 2 for number in range(1, 6))

print(squares_expression)

# Output:
# <generator object <genexpr> at 0x...>


"""
The expression creates a generator object.

It does not immediately create a complete list containing:

    [1, 4, 9, 16, 25]
"""


# -----------------------------------------------------------
# Generator expression with next()
# -----------------------------------------------------------

squares_expression = (number ** 2 for number in range(1, 6))

print(next(squares_expression))
# Output:
# 1

print(next(squares_expression))
# Output:
# 4

print(next(squares_expression))
# Output:
# 9


# -----------------------------------------------------------
# Generator expression with for loop
# -----------------------------------------------------------

squares_expression = (number ** 2 for number in range(1, 6))

for square in squares_expression:
    print(square)

# Output:
# 1
# 4
# 9
# 16
# 25


# -----------------------------------------------------------
# Example: Even numbers generator expression
# -----------------------------------------------------------

even_numbers_expression = (
    number for number in range(1, 11)
    if number % 2 == 0
)

for number in even_numbers_expression:
    print(number)

# Output:
# 2
# 4
# 6
# 8
# 10


# -----------------------------------------------------------
# Example: Names with a condition
# -----------------------------------------------------------

names = [
    "John Smith",
    "Alice",
    "Andrew",
    "Michael",
    "Anna"
]

long_names = (
    name for name in names
    if len(name) > 5
)

for name in long_names:
    print(name)

# Output:
# John Smith
# Andrew
# Michael


"""
Generator expression structure:

    (expression for item in iterable if condition)

"""


# -----------------------------------------------------------
# Generator expression vs list comprehension
# -----------------------------------------------------------

"""
List comprehension:

    [number ** 2 for number in range(1, 6)]

Creates the list immediately.

Generator expression:

    (number ** 2 for number in range(1, 6))

Creates a generator object and produces values lazily.

Main difference:

    [] -> list comprehension -> complete list
    () -> generator expression -> generator object

List comprehension:
    values are created immediately.

Generator expression:
    values are produced when requested.
"""


# ===========================================================
# 19.7 PRACTICAL EXAMPLES
# ===========================================================


# -----------------------------------------------------------
# Example 1: Generate a sequence of numbers
# -----------------------------------------------------------

def generate_numbers(start, end):
    number = start

    while number <= end:
        yield number
        number += 1


for number in generate_numbers(1, 10):
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# -----------------------------------------------------------
# Example 2: Generate even numbers
# -----------------------------------------------------------

def generate_even_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number


for number in generate_even_numbers(1, 20):
    print(number)

# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20


# -----------------------------------------------------------
# Example 3: Generate Fibonacci numbers
# -----------------------------------------------------------

def fibonacci(count):
    first = 0
    second = 1

    for _ in range(count):
        yield first
        first, second = second, first + second


for number in fibonacci(8):
    print(number)

# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13


"""
The generator preserves first and second between yield points,
allowing the Fibonacci sequence to continue correctly.
"""


# -----------------------------------------------------------
# Example 4: Process numbers one at a time
# -----------------------------------------------------------

def process_numbers(numbers):
    for number in numbers:
        yield number * 10


numbers = range(1, 6)

for result in process_numbers(numbers):
    print(result)

# Output:
# 10
# 20
# 30
# 40
# 50





# -----------------------------------------------------------
# Example 5: Generator expression with sum()
# -----------------------------------------------------------

numbers = (number ** 2 for number in range(1, 6))

total = sum(numbers)

print(total)

# Output:
# 55


"""
The generator expression produces:

    1, 4, 9, 16, 25

sum() consumes the generator and calculates:

    1 + 4 + 9 + 16 + 25 = 55
"""


# ===========================================================
# 19.8 PRACTICAL EXERCISES
# ===========================================================

"""
Exercise 1:
Create a generator function called multiples_of_five()
that generates the first 10 multiples of 5.

"""


# Exercise 1 solution

def multiples_of_five(numbers):
    for number in numbers:
        yield number * 5


for number in multiples_of_five(range(1, 11)):
    print(number)

# Output:
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50


"""
Exercise 2:
Create a generator function called
numbers_greater_than_50(numbers) that yields only numbers
greater than 50.

Test data:

[25, 75, 40, 90, 55, 30, 100]

"""


# Exercise 2 solution

def numbers_greater_than_50(numbers):
    for number in numbers:
        if number > 50:
            yield number


for number in numbers_greater_than_50(
    [25, 75, 40, 90, 55, 30, 100]
):
    print(number)

# Output:
# 75
# 90
# 55
# 100


"""
Exercise 3:
Create a generator expression that produces the cubes of
even numbers from 1 to 10.


"""


# Exercise 3 solution

cube_of_numbers = (
    number ** 3
    for number in range(1, 11)
    if number % 2 == 0
)

for number in cube_of_numbers:
    print(number)

# Output:
# 8
# 64
# 216
# 512
# 1000


# ===========================================================
# 19.9 SUMMARY
# ===========================================================

"""
GENERATOR
---------
A generator is a special kind of iterator that produces values
one at a time, on demand, using yield.


GENERATOR FUNCTION
------------------
A function containing yield is called a generator function.

Calling the function creates and returns a generator object.


GENERATOR OBJECT
----------------
A generator object is an iterator created when a generator
function is called.

It:

- Manages generator execution.
- Preserves execution state.
- Preserves local variable values between suspensions.
- Produces values one at a time.
- Can be consumed using next(), for loops, and other iterable
  operations.


yield
-----
yield:

- Produces a value.
- Pauses execution.
- Preserves the current state.
- Allows execution to resume later.
- Can produce multiple values.

Main idea:

    yield -> produce + pause


return
------
return:

- Returns a value.
- Terminates the function.

In a generator:

    return -> terminates the generator

After termination, another next() call raises StopIteration.


next()
------
next(generator) requests the next value from a generator.

Each next() call resumes the generator from where it previously
paused and continues until the next yield.


STOPITERATION
-------------
When a generator has no more values to produce, it becomes
exhausted.

A further next() call raises StopIteration.

A for loop handles StopIteration automatically and stops.


GENERATOR STATE
---------------
A generator preserves its execution state between yield points.

This includes information such as:

- Current execution position
- Local variable values
- Information required to resume execution


LAZY EVALUATION
---------------
Generators are lazy because they produce values only when
those values are requested.

This can reduce memory usage when processing large sequences.


GENERATORS WITH FOR LOOPS
-------------------------
A for loop automatically requests the next value from a
generator until the generator is exhausted.

Example:

    for value in generator:
        print(value)


GENERATORS WITH WHILE LOOPS
---------------------------
A while loop does not automatically call next().

When manually consuming a generator with while, next() must
be called explicitly.

Example:

    while True:
        try:
            value = next(generator)
            print(value)
        except StopIteration:
            break


GENERATOR EXPRESSIONS
---------------------
A generator expression is a compact way to create a generator
without defining a separate generator function.

Syntax:

    (expression for item in iterable)

With a condition:

    (expression for item in iterable if condition)


LIST COMPREHENSION VS GENERATOR EXPRESSION
------------------------------------------
List comprehension:

    [expression for item in iterable]

Creates a list immediately.

Generator expression:

    (expression for item in iterable)

Creates a generator object and produces values lazily.


MAIN ADVANTAGES OF GENERATORS
-----------------------------
- Produce values one at a time.
- Use lazy evaluation.
- Preserve execution state.
- Can process large sequences efficiently.
- Avoid unnecessary storage of an entire result sequence.
- Can represent potentially infinite sequences.


CORE IDEA
---------
Instead of:

    create everything -> store everything -> process everything

a generator can:

    produce one value -> process it -> produce next value
"""
