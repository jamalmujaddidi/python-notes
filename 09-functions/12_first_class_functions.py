# ============================================================
# 12. FIRST-CLASS FUNCTIONS
# ============================================================
# In Python, functions are first-class objects.
#
# This means a function can be:
# 1. Assigned to a variable
# 2. Passed as an argument to another function
# 3. Returned from a function
# 4. Stored in data structures


# ============================================================
# 12.1 ASSIGNING A FUNCTION TO A VARIABLE
# ============================================================

def greet():
    print("Hello Mr Smith")


# Assigning the function object to another variable.
# Parentheses are NOT used because we are not calling the function.
message = greet

# Calling the function through the new variable.
message()

# Output:
# Hello Mr Smith


# Both names refer to the same function object.
print(greet is message)

# Output:
# True


# ------------------------------------------------------------
# Difference between a function and calling a function
# ------------------------------------------------------------

def add_numbers(a, b):
    return a + b


# 'add_numbers' refers to the function object.
operation = add_numbers

# 'operation()' calls the function.
result = operation(10, 90)

print(result)

# Output:
# 100


# ============================================================
# 12.2 PASSING A FUNCTION AS AN ARGUMENT
# ============================================================


# ------------------------------------------------------------
# Example 1: Passing a function that takes no arguments
# ------------------------------------------------------------

def demo():
    print("Hello Mr Smith")


def display(func):
    func()


display(demo)

# Output:
# Hello Mr Smith


# ------------------------------------------------------------
# Example 2: Passing another function that takes no arguments
# ------------------------------------------------------------

def add():
    print(10 + 30)


def execute(operation):
    operation()


execute(add)

# Output:
# 40


# ------------------------------------------------------------
# Example 3: Passing a function that requires arguments
# ------------------------------------------------------------

def mul(a, b):
    print(a * b)


def execute_with_values(operation):
    operation(200, 8)


execute_with_values(mul)

# Output:
# 1600


# ------------------------------------------------------------
# Example 4: Passing a function that returns a value
# ------------------------------------------------------------

def bonus():
    bon = 2000
    return bon


def salary(calculation):
    sal = 45000
    total = calculation() + sal
    print(total)


salary(bonus)

# Output:
# 47000


# ------------------------------------------------------------
# Example 5: Passing different functions to the same function
# ------------------------------------------------------------

def addition():
    return 10 + 20


def multiplication():
    return 10 * 20


def calculate(operation):
    print(operation())


calculate(addition)
calculate(multiplication)

# Output:
# 30
# 200