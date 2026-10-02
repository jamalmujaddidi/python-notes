
"""
Topic 17: Decorators
====================

17.1 Introduction to Decorators
17.2 Understanding the @ Syntax
17.3 Decorators with Parameters
"""


# ============================================================
# 17.1 INTRODUCTION TO DECORATORS
# ============================================================

"""
Definition:
A decorator is a function that takes another function as an
argument and returns a function, usually a wrapper, that adds
or modifies behavior without changing the original function's
source code.

Decorators are commonly used for:
- Logging
- Authentication
- Timing function execution
- Caching
- Adding extra behavior to functions

General syntax:

def decorator(func):
    def wrapper():
        # Additional behavior
        func()
    return wrapper
"""


# Example 1: A Simple Decorator

def transaction_decorator(func):
    def wrapper():
        print("Transaction Started")
        func()
        print("Transaction Successful")

    return wrapper


def transaction():
    print("Your transaction is being processed")


result = transaction_decorator(transaction)
result()

# Output:
# Transaction Started
# Your transaction is being processed
# Transaction Successful


# Explanation:
# 1. transaction_decorator() receives the transaction function.
# 2. wrapper() adds messages before and after the function call.
# 3. The decorator returns wrapper.
# 4. result refers to the returned wrapper function.
# 5. result() executes wrapper(), which calls transaction().


# ============================================================
# 17.2 UNDERSTANDING THE @ SYNTAX
# ============================================================

"""
Definition:
The @decorator_name syntax is a special syntax used to apply
a decorator to a function.

It automatically passes the original function to the decorator
and rebinds the function's name to the function returned by
the decorator.

It is a shorter and cleaner alternative to manually applying
a decorator.

General syntax:

@decorator_name
def original_function():
    # Main task
    pass
"""


# Example 2: Using the @ Syntax

def welcome_decorator(func):
    def wrapper():
        print("Welcome Message Started")
        func()
        print("Welcome Message Finished")

    return wrapper


@welcome_decorator
def welcome():
    print("Welcome, John Smith!")


welcome()

# Output:
# Welcome Message Started
# Welcome, John Smith!
# Welcome Message Finished


# Explanation:
# The @ syntax is equivalent to:
#
# def welcome():
#     print("Welcome, John Smith!")
#
# welcome = welcome_decorator(welcome)
#
# The original function is passed to the decorator.
# The decorator returns wrapper.
# The name welcome is rebound to the returned wrapper function.
# Calling welcome() executes wrapper().


# Example 3: Applying a Decorator Manually

def greeting_decorator(func):
    def wrapper():
        print("Greeting Started")
        func()
        print("Greeting Finished")

    return wrapper


def greet():
    print("Hello, John Smith!")


greet = greeting_decorator(greet)
greet()

# Output:
# Greeting Started
# Hello, John Smith!
# Greeting Finished


# Explanation:
# Manual application performs the same basic function
# as using @greeting_decorator above the function definition.


# ============================================================
# 17.3 DECORATORS WITH PARAMETERS
# ============================================================

"""
Definition:
A parameterized decorator is a decorator that accepts one or
more arguments to customize its behavior.

It uses an additional outer function to receive the
customization parameters and return the actual decorator.

General syntax:

def outer_function(parameter):
    def decorator(func):
        def wrapper():
            # Additional behavior
            func()
        return wrapper
    return decorator

@outer_function(value)
def original_function():
    # Main task
    pass

Execution:
1. The outer function receives the customization parameter.
2. The outer function returns the actual decorator.
3. The decorator receives the original function.
4. The decorator returns the wrapper.
5. Calling the decorated function executes the wrapper.
"""


# ------------------------------------------------------------
# Example 4: Decorator with a Custom Message
# ------------------------------------------------------------

def message_decorator(message):
    def decorator(func):
        def wrapper():
            print(message)
            func()

        return wrapper
    return decorator


@message_decorator("Welcome to Python!")
def greet_message():
    print("Hello, John Smith!")


greet_message()

# Output:
# Welcome to Python!
# Hello, John Smith!


# Explanation:
# message_decorator(message) receives the custom message.
# decorator(func) receives the original function.
# wrapper() prints the message and calls the original function.
#
# The message can be changed without changing the decorator's
# internal structure.


# ------------------------------------------------------------
# Example 5: Decorator That Repeats a Function
# ------------------------------------------------------------

def repeat_decorator(times):
    def decorator(func):
        def wrapper():
            for i in range(times):
                func()

        return wrapper
    return decorator


@repeat_decorator(3)
def greet_repeatedly():
    print("Welcome, John Smith!")


greet_repeatedly()

# Output:
# Welcome, John Smith!
# Welcome, John Smith!
# Welcome, John Smith!


# Explanation:
# repeat_decorator(times) receives the repetition count.
# decorator(func) receives the original function.
# wrapper() executes the original function the specified
# number of times.
#
# The repetition logic is inside wrapper().
# The original function contains the message-printing task.


# ------------------------------------------------------------
# Example 6: Decorator with Custom Symbols
# ------------------------------------------------------------

def border_decorator(symbol):
    def decorator(func):
        def wrapper():
            print(symbol * 10)
            func()
            print(symbol * 10)

        return wrapper
    return decorator


@border_decorator("*")
def welcome_border():
    print("Welcome, John Smith!")


@border_decorator("#")
def goodbye_border():
    print("Goodbye, John Smith!")


welcome_border()
goodbye_border()

# Output:
# **********
# Welcome, John Smith!
# **********
# ##########
# Goodbye, John Smith!
# ##########


# Explanation:
# border_decorator(symbol) receives the symbol.
# wrapper() prints the border before and after the function.
# The same decorator can be reused with different symbols.


# ------------------------------------------------------------
# Example 7: Parameterized Decorator for Addition
# ------------------------------------------------------------

def add_decorator(a, b):
    def decorator(func):
        def wrapper():
            print("We are going to add two numbers")

            func(a, b)

            print("We successfully got our result")

        return wrapper
    return decorator


@add_decorator(34, 54)
def addition(a, b):
    print(a + b)


addition()

# Output:
# We are going to add two numbers
# 88
# We successfully got our result


# Explanation:
# add_decorator(a, b) receives 34 and 54.
# decorator(func) receives the original addition function.
# wrapper() passes a and b to the original function.
# addition(a, b) performs the actual addition.
#
# The original function receives the values through func(a, b).


# ------------------------------------------------------------
# Example 8: Understanding Scope and Closures
# ------------------------------------------------------------

def custom_message_decorator(message):
    def decorator(func):
        def wrapper():
            print(message)
            func()

        return wrapper
    return decorator


@custom_message_decorator("Welcome!")
def greet_closure():
    print("Hello, John Smith!")


greet_closure()

# Output:
# Welcome!
# Hello, John Smith!


# Explanation:
# message is a local variable of custom_message_decorator().
# wrapper() can access message through its enclosing scope.
#
# This is an example of a closure.
#
# A closure is a function that retains access to variables
# from its enclosing scope even after the enclosing function
# has finished executing.
#
# Local variables are not automatically accessible to
# unrelated functions defined outside their scope.


"""
Topic 17.4 — Decorators with Arguments and Return Values
==========================================================
"""

# ============================================================
# Example 1 — Decorator with Function Arguments and Return Value
# ============================================================

def my_decorator(func):

    def wrapper(a, b):
        print("Function started")

        result = func(a, b)

        print("Function finished")

        return result

    return wrapper


@my_decorator
def addition(a, b):
    return a + b


result = addition(10, 20)

print("Result:", result)

# Output:
# Function started
# Function finished
# Result: 30


# ============================================================
# Example 2 — Decorator with a Function Argument and Return Value
# ============================================================

def square_decorator(func):

    def wrapper(number):
        print("Calculating the square...")

        result = func(number)

        print("Calculation completed.")

        return result

    return wrapper


@square_decorator
def square(number):
    return number ** 2


result = square(5)

print("Result:", result)

# Output:
# Calculating the square...
# Calculation completed.
# Result: 25


# ============================================================
# Example 3 — Decorator with a Function Argument and Return Value
# ============================================================

def calculator_decorator(func):
    def wrapper(a, b):
        print("Calculation started")

        result = func(a, b)

        print("Calculation completed")
        return result

    return wrapper


@calculator_decorator
def multiply(a, b):
    return a * b


result = multiply(6, 7)

print("Result:", result)


# Output:
# Calculation started
# Calculation completed
# Result: 42
#======================================================================
# Example: Parameterized Decorator with Arguments and Return Value
#======================================================================

def message_decorator(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message)

            result = func(*args, **kwargs)
            print(f"Final result is {result}")

            print("Function completed")
            return result

        return wrapper

    return decorator


@message_decorator("Starting calculation...")
def divide(a, b):
    return a / b


result = divide(700, 7)

# ============================================================
# IMPORTANT CONCEPTS AND SUMMARY
# ============================================================

"""
1. A regular decorator receives the original function directly.

2. A parameterized decorator first receives customization
   parameters through an outer function.

3. The actual decorator receives the original function.

4. The wrapper adds or controls behavior and calls the original
   function when appropriate.

5. The @ syntax automatically applies the decorator and rebinds
   the function's name to the returned function.

6. The wrapper can access variables from enclosing scopes
   through closures.

7. Decorator parameters customize the decorator's behavior.
   They are different from the original function's parameters.

8. The original function usually contains the task being
   decorated, while the wrapper adds or controls behavior.
   Both can contain logic depending on the program's purpose.

9. The outer function is called when Python processes the
   decorated function definition. The wrapper executes when
   the decorated function is called.

Topic 17: Decorators
Sections 17.1, 17.2, and 17.3
"""