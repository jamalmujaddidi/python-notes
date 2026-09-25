"""
Python Notes
Topic 13: Nested Functions
Subtopics 13.1–13.4

A nested function is a function defined inside another function.
The outer function contains the inner function and can call it.
"""

# ============================================================
# 13.1 - Introduction to Nested Functions
# ============================================================

# A function defined inside another function is called a nested function.
# Defining the inner function does not automatically call it.

def outer_function():
    def inner_function():
        print("I am the inner function")

    print("I am the outer function")


outer_function()

# Output:
# I am the outer function


# Calling the inner function from inside the outer function:

def outer_function():
    def inner_function():
        print("I am the inner function")

    print("I am the outer function")
    inner_function()


outer_function()

# Output:
# I am the outer function
# I am the inner function


# ============================================================
# 13.2 - Calling Inner Functions and Their Behavior
# ============================================================

# An inner function can be called from within its outer function.
# Its name is local to the outer function, so it cannot normally
# be called directly from outside that function.

def greet():
    def say_hello():
        print("Hello")

    say_hello()


greet()

# Output:
# Hello


# Calling an inner function multiple times:

def show_messages():
    def display_message():
        print("Python is interesting")

    display_message()
    display_message()
    display_message()


show_messages()

# Output:
# Python is interesting
# Python is interesting
# Python is interesting


# ============================================================
# 13.3 - Nested Functions with Parameters
# ============================================================

# The inner function can have its own parameters.

def greet_person():
    def inner_function(name):
        print("Hello", name)

    inner_function("John Smith")


greet_person()

# Output:
# Hello John Smith


# Example: An inner function that adds two numbers:

def calculate_sum():
    def add(a, b):
        return a + b

    result = add(10, 20)
    print(result)


calculate_sum()

# Output:
# 30


# ============================================================
# 13.4 - Why and When Nested Functions Are Useful
# ============================================================

# 1. Code organization:
# Keep a helper function close to the code that uses it.

def greet_person():
    def get_greeting(name):
        return "Hello, " + name

    message = get_greeting("John Smith")
    print(message)


greet_person()

# Output:
# Hello, John Smith


# 2. Reusing a helper function:
# Define the helper once and call it multiple times.

def calculate_squares():
    def square(number):
        return number ** 2

    print(square(5))
    print(square(8))


calculate_squares()

# Output:
# 25
# 64


# 3. Encapsulating internal logic:
# Keep a helper function local to the operation that needs it.

def calculate_final_price(price):
    def apply_discount(amount):
        return amount * 0.90  # 10% discount

    final_price = apply_discount(price)
    print("Final price:", final_price)


calculate_final_price(1000)

# Output:
# Final price: 900.0


# 4. Data validation helper:
# Validate data before processing it.

def process_user(name):
    def is_valid_name(value):
        return value.strip() != ""

    if is_valid_name(name):
        print("Hello,", name)
    else:
        print("Invalid name")


process_user("John Smith")
process_user("")

# Output:
# Hello, John Smith
# Invalid name


# ============================================================
# 13.5 - Nested Functions and Scope
# ============================================================

# Example 1: Accessing an outer function's variable

def outer_function():
    message = "Hello, John Smith"

    def inner_function():
        print(message)

    inner_function()


outer_function()

# Output:
# Hello, John Smith


# Example 2: Accessing multiple outer variables

def calculate_total():
    price = 1000
    tax = 100

    def calculate():
        return price + tax

    total = calculate()
    print("Total:", total)


calculate_total()

# Output:
# Total: 1100


# Example 3: Inner function with its own local variable

def outer_function():
    message = "Hello from outer function"

    def inner_function():
        greeting = "Hello from inner function"
        print(greeting)
        print(message)

    inner_function()


outer_function()

# Output:
# Hello from inner function
# Hello from outer function


# Example 4: Same variable name in both functions

def outer_function():
    message = "Outer message"

    def inner_function():
        message = "Inner message"
        print(message)

    inner_function()
    print(message)


outer_function()

# Output:
# Inner message
# Outer message


# Example 5: Practice - Local scope in nested functions

def outer():
    x = 10

    def inner():
        x = 20
        print(x)

    inner()
    print(x)


outer()

# Output:
# 20
# 10


# ============================================================
# Key Points to Remember
# ============================================================

# 1. A nested function is defined inside another function.
# 2. Defining an inner function does not execute its body.
# 3. The inner function can be called from inside the outer function.
# 4. The inner function's name is local to the outer function.
# 5. Inner functions can have parameters and return values.
# 6. Nested functions can organize helper logic and keep it local.
# 7. Use a top-level function when the helper needs to be shared
#    across multiple parts of a program.