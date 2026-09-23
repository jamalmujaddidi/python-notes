# ============================================================
# 11. Scope of Variables
# ============================================================
# The location or region of a program where we can find and
# also access a variable if required is called the scope of a
# variable.

# ============================================================
# 11.1 Local Scope
# ============================================================

# Example 1: Local variable

def sub():
    interest = "I Love Python"
    print(interest)


sub()

# Output:
# I Love Python


# Example 2: Accessing a local variable outside its function

def test():
    x = 20
    print(x)


test()

# Output:
# 20

# A local variable cannot normally be accessed directly
# outside the function in which it is defined.

# print(x)

# Output:
# NameError: name 'x' is not defined


# Example 3: Local and global variables can have the same name

x = 100


def example():
    x = 20
    print(x)


example()
print(x)

# Output:
# 20
# 100


# ============================================================
# 11.2 Global Scope
# ============================================================

# Example 1: Accessing a global variable inside a function

name = "Python"


def display():
    print(name)


display()
print(name)

# Output:
# Python
# Python


# Example 2: Reading a global variable

x = 100


def show():
    print(x)


show()

# Output:
# 100



# ============================================================
# 11.3 global Statement
# ============================================================

# Example 1: Reassigning a global variable using global

x = 10


def change():
    global x
    x = 20


change()
print(x)

# Output:
# 20


# Example 2: Modifying a global counter

counter = 0


def increment():
    global counter
    counter += 1


increment()
increment()
increment()

print(counter)

# Output:
# 3


# Example 3: Creating a global name inside a function

def create_variable():
    global y
    y = 345


create_variable()

print(y)

# Output:
# 345


# The function must execute before y exists globally.

# If the following statement were placed BEFORE
# create_variable(), it would produce:
#
# NameError: name 'y' is not defined


# Example 4: global is not required just to read a global variable

number = 50


def display_number():
    print(number)


display_number()

# Output:
# 50


# ============================================================
# 11.4 Enclosing Scope
# ============================================================

# Example 1: Inner function accessing a name
# from its enclosing function

def outer():
    x = 10

    def inner():
        print(x)

    inner()


outer()

# Output:
# 10


# Example 2: Another enclosing-scope example

def outer_message():
    message = "Hello from outer"

    def inner_message():
        print(message)

    inner_message()


outer_message()

# Output:
# Hello from outer


# Example 3: Inner function has its own local variable

def outer_number():
    x = 10

    def inner_number():
        x = 20
        print(x)

    inner_number()
    print(x)


outer_number()

# Output:
# 20
# 10


# Example 4: Outer function can access the inner function itself

def outer_function():

    def inner_function():
        print("Hello from inner")

    inner_function()


outer_function()

# Output:
# Hello from inner


# An outer function cannot access a local name
# defined inside its inner function.

# Example:

def outer_example():

    def inner_example():
        value = 10

    # print(value)
    # NameError: name 'value' is not defined

    inner_example()


outer_example()


# ============================================================
# 11.5 nonlocal Statement
# ============================================================

# Example 1: Without nonlocal

def outer_without_nonlocal():
    x = 10

    def inner():
        x = 20

    inner()
    print(x)


outer_without_nonlocal()

# Output:
# 10


# Example 2: Using nonlocal

def outer_with_nonlocal():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)


outer_with_nonlocal()

# Output:
# 20


# Example 3: nonlocal with multiple function calls

def counter_function():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)

    increment()
    increment()
    increment()


counter_function()

# Output:
# 1
# 2
# 3


# Example 4: nonlocal refers to the nearest
# enclosing function scope containing the name

def outer_level():
    x = 10

    def middle_level():
        x = 20

        def inner_level():
            nonlocal x
            x = 30

        inner_level()
        print(x)

    middle_level()
    print(x)


outer_level()

# Output:
# 30
# 10


# ============================================================
# 11.6 LEGB Rule
# ============================================================

# LEGB:
#
# L → Local
# E → Enclosing
# G → Global
# B → Built-in


# Example 1: Local scope has priority

x = "global"


def local_example():
    x = "local"
    print(x)


local_example()

# Output:
# local


# Example 2: Enclosing scope

x = "global"


def enclosing_example():

    x = "enclosing"

    def inner():
        print(x)

    inner()


enclosing_example()

# Output:
# enclosing


# Example 3: Global scope

x = "global"


def global_example():
    print(x)


global_example()

# Output:
# global


# Example 4: Built-in scope

def builtin_example():
    print(len("Python"))


builtin_example()

# Output:
# 6


# Example 5: Complete LEGB example

x = "global"


def outer():

    x = "enclosing"

    def inner():

        x = "local"
        print(x)

    inner()


outer()

# Output:
# local


# Search order:
#
# Local      → x = "local"       ✓
# Enclosing  → not searched
# Global     → not searched
# Built-in   → not searched


# Example 6: LEGB without a local variable

x = "global"


def outer_without_local():

    x = "enclosing"

    def inner():
        print(x)

    inner()


outer_without_local()

# Output:
# enclosing


# Search order:
#
# Local      → not found
# Enclosing  → x = "enclosing"   ✓
# Global     → not searched
# Built-in   → not searched


# Example 7: LEGB without local and enclosing variables

x = "global"


def outer_without_enclosing():

    def inner():
        print(x)

    inner()


outer_without_enclosing()

# Output:
# global


# Search order:
#
# Local      → not found
# Enclosing  → not found
# Global     → x = "global"       ✓
# Built-in   → not searched


# ============================================================
# Built-in Namespace Examples
# ============================================================

# Python provides many built-in variables names.

print("Python")
print(len("Python"))
print(type(100))
print(int("25"))
print(str(100))
print(list("ABC"))
print(sum([10, 20, 30]))
print(max([10, 20, 30]))
print(min([10, 20, 30]))
print(range(3))
print(abs(-25))
print(round(3.14159, 2))
print(sorted([30, 10, 20]))

# Output:
# Python
# 6
# <class 'int'>
# 25
# 100
# ['A', 'B', 'C']
# 60
# 30
# 10
# range(0, 3)
# 25
# 3.14
# [10, 20, 30]