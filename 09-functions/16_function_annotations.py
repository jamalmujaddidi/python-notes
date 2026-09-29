# ============================================================
# Topic 16: Function Annotations
# ============================================================

# 16.1 Introduction to Function Annotations
# ------------------------------------------
# Function annotations are expressions associated with a function's
# parameters and return value to provide additional information.
# They are commonly used to indicate expected data types.
# Annotations do not automatically enforce type checking.

# Basic syntax:
# def function_name(parameter: annotation) -> return_annotation:
#     return expression

# Example:
def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))
# Output:
# 30


# 16.2 Parameter Annotations
# --------------------------
# Parameter annotations are written after a parameter name using a colon.

# Example: Annotating multiple parameters

def introduce(name: str, age: int, height: float):
    print(f"My name is {name}.")
    print(f"I am {age} years old.")
    print(f"My height is {height} meters.")

introduce("John Smith", 25, 1.75)
# Output:
# My name is John Smith.
# I am 25 years old.
# My height is 1.75 meters.

# Annotations do not enforce parameter types.

def greet(name: str):
    print("Hello", name)

greet(100)
# Output:
# Hello 100


# 16.3 Return Annotations
# -----------------------
# Return annotations are written after the parameter list using ->.
# They describe the expected return value.

# Example:
def calculate_area(length: float, width: float) -> float:
    return length * width

print(calculate_area(5.0, 3.0))
# Output:
# 15.0

# Return annotations do not enforce the return type.

def get_age() -> int:
    return "twenty-five"

print(get_age())
# Output:
# twenty-five


# 16.4 Accessing the __annotations__ Attribute
# --------------------------------------------
# A function's __annotations__ attribute stores its annotations
# in a dictionary.

# Example: Parameter annotations

def multiply(a: int, b: int):
    return a * b

print(multiply.__annotations__)
# Output:
# {'a': <class 'int'>, 'b': <class 'int'>}

# Example: Parameter and return annotations

def divide(a: float, b: float) -> float:
    return a / b

print(divide.__annotations__)
# Output:
# {'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}

# Example: Only return annotation

def get_number() -> int:
    return 25

print(get_number.__annotations__)
# Output:
# {'return': <class 'int'>}

# Example: No annotations

def greet_user(name):
    print("Hello", name)

print(greet_user.__annotations__)
# Output:
# {}

# Accessing individual annotations

def example(name: str, age: int) -> str:
    return f"{name} is {age} years old."

print(example.__annotations__['name'])
print(example.__annotations__['age'])
print(example.__annotations__['return'])
# Output:
# <class 'str'>
# <class 'int'>
# <class 'str'>

# Using dict.get() to access an annotation safely
print(example.__annotations__.get('city'))
# Output:
# None


# ============================================================
# Key Takeaways
# ============================================================
# 1. Function annotations are optional.
# 2. Parameter annotations use a colon (:).
# 3. Return annotations use an arrow (->).
# 4. Annotations do not automatically enforce types.
# 5. Annotations are accessible through __annotations__.
# 6. The return annotation is stored under the key 'return'.
# 7. A function without annotations has an empty annotation dictionary.
