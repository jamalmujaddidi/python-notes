# ============================================================
# 14. CLOSURES
# ============================================================


# ------------------------------------------------------------
# 14.1 Introduction to Closures
# ------------------------------------------------------------

# A closure is an inner function that retains access to
# variables from its enclosing function scope, even after
# the enclosing function has finished executing.

def outer_function():
    message = "Hello, John Smith"

    def inner_function():
        print(message)

    return inner_function


greet = outer_function()

greet()

# Output:
# Hello, John Smith


# Note:
# return inner_function returns the function itself.
# It does not call the function.
#
# greet now refers to the returned inner function.
# The inner function still has access to message.


# ------------------------------------------------------------
# 14.2 How Closures Capture Enclosing Variables
# ------------------------------------------------------------

# A closure can access variables from its enclosing scope.

def outer_function():
    message = "Hello"

    def inner_function():
        print(message)

    message = "Welcome"

    return inner_function


greet = outer_function()

greet()

# Output:
# Welcome


# The inner function uses the current binding of message
# when it is called.
#
# The value of message was changed from "Hello" to "Welcome"
# before outer_function() returned the inner function.


# Example: Capturing multiple enclosing variables

def create_profile():
    name = "John Smith"
    age = 30

    def show_profile():
        print("Name:", name)
        print("Age:", age)

    return show_profile


profile = create_profile()

profile()

# Output:
# Name: John Smith
# Age: 30


# ------------------------------------------------------------
# 14.3 Returning Inner Functions and Preserving State
# ------------------------------------------------------------

# Preserving state means that a closure remembers the current
# value of a variable between function calls, rather than
# starting from the initial value each time.

def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)

    return increment


counter = create_counter()

counter()
counter()
counter()
counter()

# Output:
# 1
# 2
# 3
# 4


# Note:
# nonlocal allows the inner function to rebind a variable
# in the nearest enclosing function scope.


# Example: Returning the updated state

def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = create_counter()

print(counter())
print(counter())
print(counter())
print(counter())

# Output:
# 1
# 2
# 3
# 4


# ------------------------------------------------------------
# 14.4 Function Factory with User Input
# ------------------------------------------------------------

def create_discount_calculator(discount):

    def calculate(price):
        return price - (price * discount / 100)

    return calculate


discount = float(input("Enter discount percentage: "))
price = float(input("Enter product price: "))

discount_calculator = create_discount_calculator(discount)

final_price = discount_calculator(price)

print("Final price:", final_price)

# Sample Input:
# Enter discount percentage: 10
# Enter product price: 1000
#
# Output:
# Final price: 900.0


# Explanation:
#
# 1. The user enters the discount percentage.
#
# 2. The user enters the product price.
#
# 3. create_discount_calculator(discount) creates a closure.
#
# 4. The closure retains access to the discount variable.
#
# 5. discount_calculator(price) calls the inner function.
#
# 6. The discounted price is returned and stored in final_price.


# ============================================================
# KEY POINTS ABOUT CLOSURES
# ============================================================

# 1. A closure is an inner function that retains access to
#    variables from its enclosing function scope.
#
# 2. The outer function can finish executing, but the closure
#    can still access the enclosing variables.
#
# 3. Returning the inner function allows the closure to be
#    used outside the outer function.
#
# 4. nonlocal allows an inner function to rebind a variable
#    from the nearest enclosing function scope.
#
# 5. Closures can preserve state between function calls.
#
# 6. Each call to an outer function can create a separate
#    closure with its own independent state.
#
# 7. Closures are useful for function factories and creating
#    functions with specific configurations.