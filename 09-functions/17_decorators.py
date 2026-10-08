
"""
# ============================================================
# TOPIC 17 — DECORATORS
# ============================================================

17.0 Overview
17.1 Introduction to Decorators
17.2 Understanding the @ Syntax
17.3 Decorators with Parameters
17.4 Decorators with Arguments and Return Values
17.5 Practical Examples and Exercises
"""


# ============================================================
# 17.0 OVERVIEW
# ============================================================

"""
Decorators are an important feature of Python that allow us to
extend or modify the behavior of functions without changing
their original source code.

Learning progression:

17.1 — Understand what a decorator is.

17.2 — Understand the @ syntax and how it works.

17.3 — Learn how to create decorators that accept parameters.

17.4 — Learn how wrappers handle function arguments and
       return values.

17.5 — Apply decorators to practical real-world situations.

Important concepts covered in Topic 17:

- Functions as objects
- Passing functions as arguments
- Returning functions
- Nested functions
- Closures
- The @ syntax
- Parameterized decorators
- Function arguments in decorators
- *args and **kwargs
- Return values from decorated functions
- Practical decorator use cases
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


# ------------------------------------------------------------
# Example 1: A Simple Decorator
# ------------------------------------------------------------

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
#
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


# ------------------------------------------------------------
# Example 2: Using the @ Syntax
# ------------------------------------------------------------

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
#
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


# ------------------------------------------------------------
# Example 3: Applying a Decorator Manually
# ------------------------------------------------------------

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
#
# Manual application performs the same basic function
# as using @greeting_decorator above the function.


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
#
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
#
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
#
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
#
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
#
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


# ============================================================
# 17.4 DECORATORS WITH ARGUMENTS AND RETURN VALUES
# ============================================================

"""
In this section, the arguments and return values belong to
the function being decorated.

This is different from 17.3.

17.3:
The decorator itself receives customization parameters.

17.4:
The wrapper receives the arguments of the decorated function
and passes them to the original function.

The wrapper can also receive the return value from the
original function and return it to the caller.


General pattern:

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper
"""


# ============================================================
# Example 9 — Decorator with Function Arguments and
# Return Value
# ============================================================

def addition_decorator(func):

    def wrapper(a, b):
        print("Function started")

        result = func(a, b)

        print("Function finished")

        return result

    return wrapper


@addition_decorator
def calculate_addition(a, b):
    return a + b


result = calculate_addition(10, 20)

print("Result:", result)

# Output:
# Function started
# Function finished
# Result: 30


# Explanation:
#
# calculate_addition(10, 20) actually calls wrapper(10, 20).
#
# wrapper() passes a and b to the original function.
#
# The original function returns 30.
#
# result stores the returned value.
#
# wrapper() then returns that value to the caller.


# ============================================================
# Example 10 — Decorator with a Function Argument and
# Return Value
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


# Explanation:
#
# square(5) calls wrapper(5).
# wrapper() passes 5 to the original square() function.
# square() returns 25.
# result stores 25.
# wrapper() returns 25 to the caller.


# ============================================================
# Example 11 — Decorator with Function Arguments and
# Return Value
# ============================================================

def calculator_decorator(func):

    def wrapper(a, b):
        print("Calculation started")

        result = func(a, b)
        print (result)

        print("Calculation completed")

        return result

    return wrapper


@calculator_decorator
def multiply(a, b):
    return a * b


result = multiply(6, 7)



# Output:
# Calculation started
# Calculation completed
# Result: 42


# ============================================================
# Example 12 — Decorator with *args, **kwargs and
# Return Value
# ============================================================

"""
*args collects positional arguments into a tuple.

**kwargs collects keyword arguments into a dictionary.

When calling the original function:

func(*args, **kwargs)

the * and ** unpack those collected arguments and pass them
to the original function.
"""


def flexible_log_decorator(func):

    def wrapper(*args, **kwargs):
        print("Function started")

        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)

        result = func(*args, **kwargs)
        print(result)

        print("Function completed")

        return result

    return wrapper


@flexible_log_decorator
def create_message(name, age, city):
    return f"{name} is {age} years old and lives in {city}."


message = create_message(
    "John Smith",
    age=30,
    city="Kabul"
)



# Output:
# Function started
# Positional arguments: ('John Smith',)
# Keyword arguments: {'age': 30, 'city': 'Kabul'}
# Function completed
# Message: John Smith is 30 years old and lives in Kabul.


# Explanation:
#
# "John Smith" is passed positionally.
#
# age=30 and city="Kabul" are passed as keyword arguments.
#
# Therefore:
#
# args = ('John Smith',)
#
# kwargs = {'age': 30, 'city': 'Kabul'}
#
# func(*args, **kwargs) reconstructs the original function call.


# ============================================================
# Example 13 — Parameterized Decorator with Arguments
# and Return Value
# ============================================================

def message_decorator_with_result(message):

    def decorator(func):

        def wrapper(*args, **kwargs):
            print(message)

            result = func(*args, **kwargs)

            print(f"Final result is {result}")
            print("Function completed")

            return result

        return wrapper

    return decorator


@message_decorator_with_result("Starting calculation...")
def divide(a, b):
    return a / b


result = divide(700, 7)

# Output:
# Starting calculation...
# Final result is 100.0
# Function completed


# Explanation:
#
# @message_decorator_with_result("Starting calculation...")
# first passes the message to the outer function.
#
# The outer function returns the actual decorator.
#
# The actual decorator receives divide().
#
# The wrapper receives 700 and 7.
#
# func(*args, **kwargs) calls divide(700, 7).
#
# divide() returns 100.0.
#
# The wrapper stores that value in result and returns it.


# ============================================================
# 17.5 PRACTICAL EXAMPLES AND EXERCISES
# ============================================================

"""
Decorators are commonly used in real applications to add
behavior that is separate from the main task of a function.

Common practical uses include:

- Logging
- Measuring execution time
- Validation
- Authentication and access control
- Caching
- Authorization
- Monitoring
- Error handling
"""


# ============================================================
# 17.5.1 PRACTICAL EXAMPLE — LOGGING
# ============================================================

"""
A logging decorator can display information about which
function is being called and when it has completed.
"""


def practical_log_decorator(func):

    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Function {func.__name__} completed")

        return result

    return wrapper


@practical_log_decorator
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print("Result:", result)

# Output:
# Calling function: add_numbers
# Function add_numbers completed
# Result: 30


# Explanation:
#
# func.__name__ gives the name of the original function.
#
# The decorator logs information before and after the
# original function executes.
#
# The original return value is preserved.


# ============================================================
# 17.5.2 PRACTICAL EXAMPLE — TIMING
# ============================================================

"""
A timing decorator can measure how long a function takes
to execute.

time.perf_counter() is suitable for measuring short durations.
"""


import time


def timing_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print(f"Execution time: {execution_time:.6f} seconds")

        return result

    return wrapper


@timing_decorator
def calculate_sum():
    total = sum(range(1_000_000))
    return total


result = calculate_sum()

print("Result:", result)

# Output:
# Execution time: <execution time will vary> seconds
# Result: 499999500000


# Explanation:
#
# start_time records the time before the function executes.
#
# end_time records the time after the function executes.
#
# The difference gives the approximate execution time.
#
# The exact execution time can be different on different
# computers and at different times.


# ============================================================
# 17.5.3 PRACTICAL EXAMPLE — VALIDATION
# ============================================================

"""
A validation decorator can check whether function arguments
meet certain conditions before allowing the original function
to execute.
"""


def positive_number(func):

    def wrapper(number):

        if number <= 0:
            print("Error: Number must be positive.")
            return None

        return func(number)

    return wrapper


@positive_number
def calculate_square(number):
    return number ** 2


result = calculate_square(5)

print("Result:", result)

# Output:
# Result: 25


# Example with an invalid value:
#
# result = calculate_square(-5)
#
# Output:
# Error: Number must be positive.


# Explanation:
#
# The wrapper checks the argument before calling the original
# function.
#
# If the value is invalid, the original function is not called.
#
# If the value is valid, the wrapper passes it to the original
# function.


# ============================================================
# 17.5.4 PRACTICAL EXAMPLE — AUTHENTICATION
# ============================================================

"""
A decorator can be used to control access to a function.

This simplified example checks whether a user is logged in
before allowing the function to execute.
"""


def require_login(func):

    def wrapper(is_logged_in):

        if not is_logged_in:
            print("Access denied. Please log in.")
            return None

        return func(is_logged_in)

    return wrapper


@require_login
def view_profile(is_logged_in):
    print("Profile information displayed.")


view_profile(True)

# Output:
# Profile information displayed.


# Example with a user who is not logged in:
#
# view_profile(False)
#
# Output:
# Access denied. Please log in.


# Explanation:
#
# The wrapper checks the login status.
#
# If is_logged_in is False, access is denied and the original
# function is not executed.
#
# If is_logged_in is True, the original function executes.


# ============================================================
# 17.5.5 PRACTICAL EXERCISE — CREATE YOUR OWN DECORATOR
# ============================================================


# Exercise:


def uppercase_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result.upper()

    return wrapper


@uppercase_decorator
def get_message():
    return "hello, John Smith!"


message = get_message()
print(message)

# Output:
# HELLO, JOHN SMITH!



# ============================================================
# IMPORTANT CONCEPTS AND SUMMARY
# ============================================================

"""
1. A decorator receives the original function and returns
   a function, usually a wrapper.

2. A decorator can add or modify behavior without changing
   the original function's source code.

3. The @ syntax is a shorter way of applying a decorator.

4. The following:

       @decorator
       def function():
           pass

   is equivalent to:

       function = decorator(function)

5. A parameterized decorator uses an additional outer function
   to receive customization parameters.

6. The actual decorator receives the original function.

7. The wrapper adds or controls behavior around the original
   function.

8. A closure allows the wrapper to access variables from its
   enclosing scope.

9. Decorator parameters are different from the parameters
   of the decorated function.

10. The wrapper can receive arguments of the decorated function.

11. *args collects positional arguments into a tuple.

12. **kwargs collects keyword arguments into a dictionary.

13. *args and **kwargs allow a decorator to work with functions
    having different argument structures.

14. The wrapper can store the original function's return value
    in a variable.

15. The wrapper can return the original function's return value
    to the caller.

16. Decorators can execute code before the original function.

17. Decorators can execute code after the original function.

18. Practical uses of decorators include:

    - Logging
    - Timing
    - Validation
    - Authentication
    - Caching
    - Monitoring
    - Error handling

19. The original function usually contains the main task,
    while the wrapper adds or controls additional behavior.

20. Both the original function and wrapper can contain logic
    depending on the purpose of the program.


Topic 17: Decorators
Sections 17.1, 17.2, 17.3, 17.4, and 17.5
"""